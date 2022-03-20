from utils import compare_dates
import datetime


class InsertionSort:

    def __init__(self):
        pass

    def sort(self, file_input):
        length = len(file_input)
        for i in range(length-1):
            key = file_input[i]
            j = i-1
            while j >= 0 and file_input[j] > key:
                file_input[j+1] = file_input[j]
                j -= 1
            file_input[j+1] = key

