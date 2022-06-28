import sorting_utils
import numpy as np

class Sorter:
    def __init__(
        self,
        initial_str,
        algorithm,
        max_steps,
        reading_err_rate,
        sorting_err_rate):
        self.current_str = initial_str
        self.max_steps = max_steps
        self.reading_err_rate = reading_err_rate 
        self.sorting_err_rate = sorting_err_rate
        self.current_step = 0
        self.records = []
        self.sorter = sorting_utils.get_sorting_algorithm(algorithm, reading_err_rate, sorting_err_rate) 
        self.sorter.set_initial_str(initial_str)
    
    def next_step(self):
        self.current_str = self.sorter.interate()
    
    def get_current_monotonicity(self):
        monotonicity_value = 0
        l = list(self.current_str)
        if len(self.current_str) == 0:
            return monotonicity_value
        prev = l[0]
        for i in range(1, len(self.current_str)):
            if l[i] < prev:
                monotonicity_value += 1
            prev = l[i]
        return monotonicity_value

    def record_stats(self):
        self.records.append({"current_str": self.current_str, "current_monotonicity": self.get_current_monotonicity()})

    def is_current_str_sorted(self):
        sorted_str = "".join(sorted(self.current_str))
        return self.current_str == sorted_str

    def run(self):
        while self.current_step < self.max_steps and not self.is_current_str_sorted():
            self.next_step()
            self.record_stats()
            self.current_step += 1

    