from typing import List, Tuple
from multiprocessing import Process

from code_loader import LeapLoader
import multiprocessing

from code_loader.contract.enums import DataStateEnum


class LeapLoaderParallelized:
    def __init__(self, code_path: str, code_entry_name: str, n_workers=2):
        self.code_entry_name = code_entry_name
        self.code_path = code_path

        self._samples_to_process = multiprocessing.Queue()
        self._ready_samples = multiprocessing.Queue()

        self.processes = [Process(target=LeapLoaderParallelized._process_func, args=(
            code_path, code_entry_name, self._samples_to_process,
            self._ready_samples)) for i in range(n_workers)]
        for proc in self.processes:
            proc.start()

        # self.preserve_order_get_lock = multiprocessing.Lock()
        # self.preserve_order_put_lock = multiprocessing.Lock()

    @staticmethod
    def _process_func(code_path: str, code_entry_name: str,
                      samples_to_process: multiprocessing.Queue, ready_samples: multiprocessing.Queue):
        leap_loader = LeapLoader(code_path, code_entry_name)
        leap_loader.exec_script()
        while True:
            try:
                state, idx = samples_to_process.get(block=True)
                sample = leap_loader.get_sample(state, idx)
                ready_samples.put(sample)
            except Exception as e:
                x = 1

    def generate_samples(self, sample_identities: List[Tuple[DataStateEnum, int]]) -> multiprocessing.Queue:
        for sample in sample_identities:
            self._samples_to_process.put(sample)

        return self._ready_samples
