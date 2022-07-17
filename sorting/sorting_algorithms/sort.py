import random

class Sort(object):
    def __init__(self, initial_str, reading_err_rate, sorting_err_rate, max_step):
        self.init_str = initial_str
        self.current_array = list(self.init_str)
        self.reading_err_rate = reading_err_rate
        self.sorting_err_rate = sorting_err_rate
        self.max_step = max_step
        self.current_sorting_index = 0
        self.records = []
        self.should_stop = False

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
        if self.should_stop:
            return
        r = random.random()
        if r < self.sorting_err_rate:
            self.record_stats()
            return 
        c = self.current_array[i]
        self.current_array[i] = self.current_array[j]
        self.current_array[j] = c
        self.record_stats()

    def current_array_to_str(self):
        return "".join(self.current_array)

    def _get_current_monotonicity(self):
        monotonicity_value = 0
        current_str = self.current_array_to_str()
        l = list(current_str)
        if len(current_str) == 0:
            return monotonicity_value
        prev = l[0]
        for i in range(1, len(current_str)):
            if l[i] < prev:
                monotonicity_value += 1
            prev = l[i]
        return monotonicity_value
    
    def record_stats(self):
        self.records.append(self._get_current_monotonicity())
        if len(self.records) == self.max_step:
            self.should_stop = True
    
