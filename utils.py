import datetime
from os import path, listdir
from insertion_sort import InsertionSort
from merge_sort import MergeSort
from tim_sort import TimSort
import os


def create_dir(input_path):
    if not path.exists(input_path):
        os.mkdir(input_path)


def compare_dates(file_input1, file_input2):
    iso_string1 = file_input1.split(b' ')[0].decode('utf-8')
    iso_string2 = file_input2.split(b' ')[0].decode('utf-8')
    datetime1 = datetime.datetime.fromisoformat(iso_string1)
    datetime2 = datetime.datetime.fromisoformat(iso_string2)
    return datetime1 > datetime2


def is_sorted(file_input):
    length = len(file_input)
    index = 0
    while 0 <= index-1 < length:
        if compare_dates(file_input[index], file_input[index+1]):
            return False
        index += 1
    return True


def get_sort_object(algo):
    ret_obj = None
    if algo == 0:
        ret_obj = InsertionSort()
    elif algo == 1:
        ret_obj = MergeSort()
    elif algo == 2:
        ret_obj = TimSort()
    return  ret_obj


