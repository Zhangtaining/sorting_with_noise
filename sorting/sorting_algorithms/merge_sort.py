from .sort import Sort

class MergeSort(Sort):
    def __init__(self, initial_str, reading_err_rate, sorting_err_rate, max_step):
        super().__init__(initial_str, reading_err_rate, sorting_err_rate, max_step)
    
    def start_sorting(self):
        self.sort(0, len(self.current_array) - 1)
    
    def sort(self, l, r):
        if self.should_stop or l >= r:
            return 
        split = l + int((r- l) / 2)
        self.sort(l, split)
        self.sort(split + 1, r)
        self.merge(l, r, split)

    def merge(self, l, r, s):
        p1 = l
        p2 = s + 1
        while p1 <= s and p2 <= r:
            if self.reading_value(p1) > self.reading_value(p2):
                p = p2
                while p > p1:
                    self.swap(p-1, p)
                    p -= 1
                p1 += 1
                p2 += 1
                s += 1
            else:
                p1 += 1
