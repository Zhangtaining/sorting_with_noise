from .sort import Sort

class BubbleSort(Sort):
    def __init__(self, initial_str, reading_err_rate, sorting_err_rate, max_step):
        super().__init__(initial_str, reading_err_rate, sorting_err_rate, max_step)
    
    def start_sorting(self):
        top_index = len(self.current_array) - 1
        i = 0
        while top_index > 0:
            j = 1
            while j <= top_index:
                if self.reading_value(j - 1) > self.reading_value(j):
                    self.swap(j - 1, j)
                j += 1
            top_index -= 1
            i += 1

     
