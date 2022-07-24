import sys, getopt
from sorting_utils import get_sorting_algorithm
import matplotlib.pyplot as plt
import numpy as np

INITIAL_STR = "437856679345753982938982467285649218649979789798128374981324701298347129812341238928"
MAX_SORTING_STEPS = 100000
READING_NOISE_RATE = [0, 0.01, 0.1, 0.5]
SORTING_ALGORITHMS = ['insertion sort', 'selection sort', 'quick sort', 'merge sort', 'bubble sort']

def build_sorting_experiment(algo):
    sorting_records = {}
    for reading_noise_rate in READING_NOISE_RATE:
        s = get_sorting_algorithm(
            algo,
            INITIAL_STR,
            0,
            reading_noise_rate,
            MAX_SORTING_STEPS
        )
        s.start_sorting()
        sorting_records[reading_noise_rate] = [r for r in s.records]
    return sorting_records

def _get_chart_position(chart_num, width):
    return int(chart_num / width), chart_num % width

def visualize_results_by_noise(records):
    fig, axis = plt.subplots(2, 2)
    chart_num = 0
    # show results by noise rate
    for reading_noise_rate in READING_NOISE_RATE:
        row, col = _get_chart_position(chart_num, 2)
        axis[row][col].set_title(f"reading noise = {reading_noise_rate}")
        axis[row][col].set_xlabel("Sorting steps")
        axis[row][col].set_ylabel("Monotonicity Score")
        for a, r in records.items():
            record = np.array(r[reading_noise_rate])
            axis[row][col].plot(record, label=a)
        chart_num += 1
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    plt.legend()

def visualize_results_by_algo(sorting_records):
    _, axis = plt.subplots(len(SORTING_ALGORITHMS), 1)
    chart_index = 0
    # show results by algorithms
    for algo, records in sorting_records.items():
        axis[chart_index].set_title(f"Algorithm = {algo}")
        axis[chart_index].set_xlabel("Sorting steps")
        axis[chart_index].set_ylabel("Monotonicity Score")
        for noise_rate, r in records.items():
            record = np.array(r)
            axis[chart_index].plot(record, label=f"reading_err={noise_rate}")
        chart_index += 1
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    plt.legend()
    

def main(argv):
    reading_noise_rate = 0
    sorting_noise_rate = 0
    
    sorting_records = {}
    for algo in SORTING_ALGORITHMS:
        sorting_records[algo] = build_sorting_experiment(algo)

    visualize_results_by_noise(sorting_records)
    visualize_results_by_algo(sorting_records)
    plt.show()
    

if __name__ == "__main__":
    main(sys.argv[1:])