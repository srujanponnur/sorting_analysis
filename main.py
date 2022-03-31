import functools
import time
from os import path
import os
from insertion_sort import InsertionSort
from merge_sort import MergeSort
from utils import compare_dates, is_sorted

data_path = path.join('data', 'B')
# files = 6
for file in os.listdir(data_path):
    file_path = path.join(data_path, file)
    # if not files:
    #     break
    print("\n-----------------------------\n")
    start = time.time()
    with open(file_path, 'rb') as fp:
        lines = fp.readlines()
        print("Number of lines are",  len(lines))
        end = time.time()
        print("Time taken to load input is", end-start)
        sorted_list, time_taken = InsertionSort().sort(lines)
        print(is_sorted(sorted_list), time_taken)
        sorted_list, time_taken = MergeSort().sort(lines)
        print(is_sorted(sorted_list), time_taken)
        start_adaptive = time.time()
        sorted(lines,key=functools.cmp_to_key(compare_dates))
        end_adaptive = time.time()
        time_taken = end_adaptive - start_adaptive
        print(is_sorted(lines), time_taken)
        
        
    #files -= 1







