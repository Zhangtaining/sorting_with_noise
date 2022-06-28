class BubbleSort:
    def __init__(self, reading_err_rate, sorting_err_rate):
        self.init_str = ""
        self.reading_err_rate = reading_err_rate
        self.sorting_err_rate = sorting_err_rate
        self.current_array = list(self.init_str)
        self.current_sorting_index = 0
    
    def set_initial_str(self, initial_str):
        self.init_str = initial_str

    def reading_value(self, index):
        return self.current_array[index] - '0'

    def swap(self, i, j):
        c = self.current_array[i]
        self.current_array[i] = self.current_array[j]
        self.current_array[j] = c

    def current_array_to_str(self):
        return "".join(self.current_array)
    
    def interate(self):
        if self.current_sorting_index == len(self.current_array):
            return self.current_array_to_str()
        
        size = len(self.current_array)
        for i in range(size - self.current_sorting_index - 1):
            if self.current_array[i] > self.current_array[i + 1]:
                swap(self, i, i + 1)
        
        current_sorting_index += 1
        return self.current_array_to_str()

     
