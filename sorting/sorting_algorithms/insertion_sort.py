import random 
from .sort import Sort

class InsertionSort(Sort):
    def __init__(self, initial_str, reading_err_rate, sorting_err_rate, max_step):
        super().__init__(initial_str, reading_err_rate, sorting_err_rate, max_step)
    
    def start_sorting(self):
        for i in range(0, len(self.current_array)):
            index_before = i - 1
            while index_before >= 0:
                if self.reading_value(index_before + 1) <= self.reading_value(index_before):
                    self.swap(index_before, index_before + 1)
                    index_before -= 1
                else:
                    break

     
