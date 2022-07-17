
import random
from .sort import Sort

class QuickSort(Sort):
    def __init__(self, initial_str, reading_err_rate, sorting_err_rate, max_step):
        super().__init__(initial_str, reading_err_rate, sorting_err_rate, max_step)
    
    def start_sorting(self):
        self.sort(0, len(self.current_array) - 1)
    
    def sort(self, l, r):
        if self.should_stop or l >= r:
            return 
        pivot = random.randint(l, r)
        small_index = l 
        max_index = r 
        pivot_value = self.reading_value(pivot)
        while small_index < max_index:
            if self.reading_value(small_index) > pivot_value:
                self.swap(small_index, max_index)
                if max_index == pivot:
                    pivot = small_index
                max_index -= 1
            else: 
                small_index += 1
        new_pivot_index = small_index if int(self.current_array[small_index]) <= pivot_value else small_index - 1
        self.swap(pivot, new_pivot_index)

        self.sort(l, new_pivot_index - 1)
        self.sort(new_pivot_index + 1, r)
