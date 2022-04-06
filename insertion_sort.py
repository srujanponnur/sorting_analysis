from utils import compare_dates
import datetime
from time import process_time


class InsertionSort:

    def __init__(self):
        pass

    def sort(self, file_input):
        length = len(file_input)
        start = process_time()
        for i in range(length-1):
            key = file_input[i]
            j = i-1
            while j >= 0 and compare_dates(file_input[j], key):
                file_input[j+1] = file_input[j]
                j -= 1
            file_input[j+1] = key
        end = process_time()
        return file_input, (end-start)

