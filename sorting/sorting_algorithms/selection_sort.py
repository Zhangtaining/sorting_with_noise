import random
from .sort import Sort

class SelectionSort(Sort):
    def __init__(self, initial_str, reading_err_rate, sorting_err_rate, max_step):
        super().__init__(initial_str, reading_err_rate, sorting_err_rate, max_step)
    
    def start_sorting(self):
        for i in range(0, len(self.current_array)):
            if self.should_stop:
                return 
            p = i + 1
            for p in range(i + 1, len(self.current_array)):
                if (self.reading_value(i) > self.reading_value(p)):
                    self.swap(i, p)
                p += 1


