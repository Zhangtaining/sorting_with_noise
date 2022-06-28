from sorting_algorithms import selection_sort, insertion_sort

def get_sorting_algorithm(algo_name, reading_error_rate, sorting_error_rate):
    if algo_name == "insertion sort":
        return insertion_sort.InsertionSort(reading_error_rate, sorting_error_rate)

    if algo_name == "selection sort":
        return selection_sort.SelectionSort(reading_error_rate, sorting_error_rate)
