import sys, getopt, sorter
import matplotlib.pyplot as plt
import numpy as np

INITIAL_STR = "437856679345753982938982467285649218649979789798128374981324701298347129812341238928"
MAX_SORTING_STEPS = 10000


def main(argv):
    reading_noise_rate = 0
    sorting_noise_rate = 0
    
    sorting_algorithm_list = ['insertion sort', 'selection sort']
    sorting_records = {}
    for algo in sorting_algorithm_list:
        s = sorter.Sorter(
            INITIAL_STR,
            algo,
            MAX_SORTING_STEPS,
            reading_noise_rate,
            sorting_noise_rate)
        s.run()
        sorting_records[algo] = np.array([r['current_monotonicity'] for r in s.records])
    
    for algo, records in sorting_records.items():
        plt.plot(records, label=algo)
    
    plt.legend()
    plt.title(f"reading noise = {reading_noise_rate}")
    plt.xlabel("Sorting steps")
    plt.ylabel("Monotonicity Score")
    plt.show()
    

if __name__ == "__main__":
    main(sys.argv[1:])