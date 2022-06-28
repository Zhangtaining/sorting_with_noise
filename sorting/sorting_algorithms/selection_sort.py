import random

class SelectionSort:
    def __init__(self, reading_err_rate, sorting_err_rate):
        self.init_str = ""
        self.reading_err_rate = reading_err_rate
        self.sorting_err_rate = sorting_err_rate
        self.current_sorting_index = 0
    
    def set_initial_str(self, initial_str):
        self.init_str = initial_str
        self.current_array = list(self.init_str)

    def _get_wrong_number(self, actual_value):
        r = random.randint(0, 10)
        while r == actual_value:
            r = random.randint(0, 10)
        return r

    def reading_value(self, index):
        actual_value = int(self.current_array[index])
        r = random.random()
        if r < self.reading_err_rate:
            return self._get_wrong_number(actual_value)
        return int(self.current_array[index])

    def swap(self, i, j):
        c = self.current_array[i]
        self.current_array[i] = self.current_array[j]
        self.current_array[j] = c

    def current_array_to_str(self):
        return "".join(self.current_array)
    
    def interate(self):
        if self.current_sorting_index == len(self.current_array):
            return self.current_array_to_str()
        
        min_index = self.current_sorting_index
        p = self.current_sorting_index + 1 
        while p < len(self.current_array):
            if (self.reading_value(min_index) > self.reading_value(p)):
                min_index = p  
            p += 1 
        
        self.swap(self.current_sorting_index, min_index)
        self.current_sorting_index += 1
        return self.current_array_to_str()
