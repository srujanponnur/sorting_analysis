import time
from os import path
import os
from insertion_sort import InsertionSort
from utils import is_sorted

data_path = path.join('data', 'C')
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
    #files -= 1







