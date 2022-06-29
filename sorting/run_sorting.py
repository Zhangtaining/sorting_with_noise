import sys, getopt, sorter
import matplotlib.pyplot as plt
import numpy as np

INITIAL_STR = "437856679345753982938982467285649218649979789798128374981324701298347129812341238928"
MAX_SORTING_STEPS = 100
READING_NOISE_RATE = [0, 0.01, 0.1, 0.5]
SORTING_ALGORITHMS = ['insertion sort', 'selection sort']

def build_sorting_experiment(algo):
    sorting_records = {}
    for reading_noise_rate in READING_NOISE_RATE:
        s = sorter.Sorter(
            INITIAL_STR,
            algo,
            MAX_SORTING_STEPS,
            reading_noise_rate,
            0)
        s.run()
        sorting_records[reading_noise_rate] = [r['current_monotonicity'] for r in s.records]
    return sorting_records

def visualize_results_by_noise(records):
    _, axis = plt.subplots(4, 1)
    chart_index = 0
    # show results by noise rate
    for reading_noise_rate in READING_NOISE_RATE:
        axis[chart_index].set_title(f"reading noise = {reading_noise_rate}")
        axis[chart_index].set_xlabel("Sorting steps")
        axis[chart_index].set_ylabel("Monotonicity Score")
        for a, r in records.items():
            record = np.array(r[reading_noise_rate])
            axis[chart_index].plot(record, label=a)
        chart_index += 1
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
            axis[chart_index].plot(record, label=noise_rate)
        chart_index += 1
    plt.legend()
    plt.show()
    

def main(argv):
    reading_noise_rate = 0
    sorting_noise_rate = 0
    
    sorting_records = {}
    for algo in SORTING_ALGORITHMS:
        sorting_records[algo] = build_sorting_experiment(algo)

    visualize_results_by_noise(sorting_records)
    visualize_results_by_algo(sorting_records)
    

if __name__ == "__main__":
    main(sys.argv[1:])