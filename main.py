from time import time
import time
from os import path, listdir
import os
from optparse import OptionParser
from insertion_sort import InsertionSort
from merge_sort import MergeSort
from utils import compare_dates, is_sorted

parser = OptionParser()
parser.add_option('-p', '--path', default=path.join(os.getcwd(), 'data'), help='the path of the dataset', type='string',
                  dest='data_path')
parser.add_option('-t', '--tries', default='0', help='The number of dummy tries', type='int',
                  dest='tries')
parser.add_option('-d', '--dest', default=path.join(os.getcwd(), 'sorted_data'), help='the path of the sorted dataset',
                  type='string', dest='sorted_data_path')

(options, args) = parser.parse_args()

print(options.data_path, options.tries, options.sorted_data_path)

if not path.exists(options.sorted_data_path):
    os.mkdir(options.sorted_data_path)

# data_path = path.join('data', 'C')
# files = 6
for dir_name in listdir(options.data_path):
    cur_dir = path.join(options.data_path, dir_name)
    dest_dir = path.join(options.sorted_data_path, dir_name)
    time_map = {}
    print(f"Sorting in the Directory--{dir_name}")
    if not path.exists(dest_dir):
        os.mkdir(dest_dir)
    for file in listdir(cur_dir):
        file_path = path.join(cur_dir, file)
        dest_file_path = path.join(dest_dir, file)
        start = time()
        with open(file_path, 'rb') as fp:
            lines = fp.readlines()
            print("Number of lines are",  len(lines))
            end = time()
            print("Time taken to load input is", end-start)
            for i in range(options.tries+1):
                unsorted_data = [i for i in lines]
                sorted_list, time_taken = InsertionSort().sort(unsorted_data)
                print(f" Try-{i} time_taken is {time_taken}")
            with open(dest_file_path, 'wb+') as fp2:
                fp2.writelines(sorted_list)
        #files -= 1







