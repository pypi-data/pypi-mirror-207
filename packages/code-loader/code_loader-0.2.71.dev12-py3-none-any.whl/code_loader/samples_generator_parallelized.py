# mypy: ignore-errors

import traceback
from dataclasses import dataclass
from functools import lru_cache
from typing import List, Tuple, Optional
from multiprocessing import Process, Queue

from code_loader.leaploader import LeapLoader
from code_loader.contract.enums import DataStateEnum


@dataclass
class GetSampleSerializableError:
    state: DataStateEnum
    index: int
    leap_script_trace: str
    exception_as_str: str


class SamplesGeneratorParallelized:
    def __init__(self, code_path: str, code_entry_name: str,
                 n_workers: int = 2, max_samples_in_queue: int = 128) -> None:
        self.code_entry_name = code_entry_name
        self.code_path = code_path

        if n_workers <= 0:
            raise Exception("need at least one worker")
        self.n_workers = n_workers
        self.max_samples_in_queue = max_samples_in_queue

        self._samples_to_process: Optional[Queue] = None  # type: ignore
        self._ready_samples: Optional[Queue] = None
        self.processes: Optional[List[Process]] = None

    @lru_cache()
    def start(self) -> None:
        self._samples_to_process = Queue()
        self._ready_samples = Queue(self.max_samples_in_queue)

        self.processes = [
            Process(target=SamplesGeneratorParallelized._process_func,
                    args=(self.code_path, self.code_entry_name, self._samples_to_process, self._ready_samples))
            for _ in range(self.n_workers)]

        for proc in self.processes:
            proc.start()

        # needed in order to make sure the preprocess func runs once in nonparallel
        self._generate_samples([(DataStateEnum.training, 0)])
        self._ready_samples.get()

    @staticmethod
    def _process_func(code_path: str, code_entry_name: str,
                      samples_to_process: Queue, ready_samples: Queue) -> None:
        leap_loader = LeapLoader(code_path, code_entry_name)
        leap_loader.exec_script()
        while True:
            state, idx = samples_to_process.get(block=True)
            try:
                sample = leap_loader.get_sample(state, idx)
            except Exception as e:
                leap_script_trace = traceback.format_exc().split('File "<string>"')[-1]
                ready_samples.put(GetSampleSerializableError(state, idx, leap_script_trace, str(e)))
                continue

            ready_samples.put(sample)

    def _generate_samples(self, sample_identities: List[Tuple[DataStateEnum, int]]) -> Queue:
        assert self._samples_to_process is not None
        assert self._ready_samples is not None

        for sample in sample_identities:
            self._samples_to_process.put(sample)

        return self._ready_samples

    def generate_samples(self, sample_identities: List[Tuple[DataStateEnum, int]]) -> Queue:
        self.start()
        return self._generate_samples(sample_identities)

    @staticmethod
    def _release_queue(queue: Queue):
        assert queue is not None
        while not queue.empty():
            queue.get()
        queue.close()
        queue.join_thread()

    def release(self) -> None:
        if self.processes is None:
            return
        for process in self.processes:
            process.terminate()
            process.kill()
            process.join()
            process.close()

        self._release_queue(self._samples_to_process)
        self._release_queue(self._ready_samples)

        self.processes = None

    def __del__(self) -> None:
        self.release()
