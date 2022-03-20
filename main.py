import time
from os import path
import os
from insertion_sort import InsertionSort

data_path = path.join('data', 'C')

for file in os.listdir(data_path):
    file_path = path.join(data_path, file)
    start = time.time()
    with open(file_path, 'rb') as fp:
        lines = fp.readlines()
        end = time.time()
        sorted_list, time_taken = InsertionSort().sort(lines)
    break







