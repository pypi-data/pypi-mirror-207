import traceback
from dataclasses import dataclass
from functools import lru_cache
from typing import List, Tuple, Optional
from multiprocessing import Process

from code_loader import LeapLoader
import multiprocessing

from code_loader.contract.enums import DataStateEnum


@dataclass
class GetSampleSerializableError:
    state: DataStateEnum
    index: int
    leap_script_trace: str
    exception_as_str: str


class SamplesGeneratorParallelized:
    def __init__(self, code_path: str, code_entry_name: str, n_workers=2):
        self.code_entry_name = code_entry_name
        self.code_path = code_path
        self.n_workers = n_workers

        self._samples_to_process: Optional[multiprocessing.Queue()] = None
        self._ready_samples: Optional[multiprocessing.Queue()] = None
        self.processes: Optional[List[Process]] = None

    @lru_cache()
    def start(self) -> None:
        self._samples_to_process = multiprocessing.Queue()
        self._ready_samples = multiprocessing.Queue()

        self.processes = [
            Process(target=SamplesGeneratorParallelized._process_func,
                    args=(self.code_path, self.code_entry_name, self._samples_to_process,self._ready_samples))
            for _ in range(self.n_workers)]

        for proc in self.processes:
            proc.start()

    @staticmethod
    def _process_func(code_path: str, code_entry_name: str,
                      samples_to_process: multiprocessing.Queue, ready_samples: multiprocessing.Queue) -> None:
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

    def generate_samples(self, sample_identities: List[Tuple[DataStateEnum, int]]) -> multiprocessing.Queue:
        self.start()
        for sample in sample_identities:
            self._samples_to_process.put(sample)

        return self._ready_samples
