from utils import compare_dates
import datetime
from time import process_time


class MergeSort:

    def __init__(self):
        pass

    def sort(self, file_input):
        start = process_time()
        if len(file_input) > 1:
            mid = len(file_input)//2

        # Dividing the array elements
            L = file_input[:mid]
            R = file_input[mid:]
            self.sort(L)
            self.sort(R)
            i = j = k = 0

        # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if not compare_dates(L[i], R[j]):
                    file_input[k] = L[i]
                    i += 1
                else:
                    file_input[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                file_input[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                file_input[k] = R[j]
                j += 1
                k += 1
        end = process_time()
        return file_input, (end-start)
