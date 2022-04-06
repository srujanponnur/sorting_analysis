from utils import compare_dates
from time import process_time
import functools


class TimSort:

    def __init__(self):
        pass

    def sort(self, file_input):
        start_adaptive = process_time()
        sorted_lines = sorted(file_input, key=functools.cmp_to_key(compare_dates))
        end_adaptive = process_time()
        time_taken = end_adaptive - start_adaptive
        return sorted_lines, (end_adaptive - start_adaptive)