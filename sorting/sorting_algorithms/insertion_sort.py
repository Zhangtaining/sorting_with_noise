import random  

class InsertionSort:
    def __init__(self, reading_err_rate, sorting_err_rate):
        self.init_str = ""
        self.reading_err_rate = reading_err_rate
        self.sorting_err_rate = sorting_err_rate
        self.current_array = list(self.init_str)
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
    
    # This function is take a full round of comparison as a step. 
    def interate(self):
        if self.current_sorting_index == len(self.current_array):
            return self.current_array_to_str()
        
        key = self.reading_value(self.current_sorting_index)

        index_before = self.current_sorting_index - 1
        while index_before >= 0 and key < self.reading_value(index_before):
            self.swap(index_before, index_before + 1)
            index_before -= 1
        
        self.current_sorting_index += 1
        return self.current_array_to_str()
    
    # This function is to take each swap as a step.
    def interate_swap_as_step(self):
        if self.current_sorting_index == len(self.current_array):
            return self.current_array_to_str()
        
        key = self.reading_value(self.current_index)
        index_before = self.current_index - 1
        if (index_before < 0) or (key >= self.reading_value(index_before)):
            self.current_sorting_index += 1 
            self.current_index = self.current_sorting_index
            return self.current_array_to_str()
        
        if key < self.reading_value(index_before):
            self.swap(index_before, self.current_index)
            self.current_index -= 1

        return self.current_array_to_str()

     
