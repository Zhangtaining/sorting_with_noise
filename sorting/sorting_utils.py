from sorting_algorithms import selection_sort, insertion_sort, bubble_sort, quick_sort, merge_sort

def get_sorting_algorithm(algo_name, initial_str, reading_error_rate, sorting_error_rate, max_steps):
    if algo_name == "insertion sort":
        return insertion_sort.InsertionSort(initial_str, reading_error_rate, sorting_error_rate, max_steps)

    if algo_name == "selection sort":
        return selection_sort.SelectionSort(initial_str, reading_error_rate, sorting_error_rate, max_steps)

    if algo_name == "bubble sort":
        return bubble_sort.BubbleSort(initial_str, reading_error_rate, sorting_error_rate, max_steps)

    if algo_name == "quick sort":
        return quick_sort.QuickSort(initial_str, reading_error_rate, sorting_error_rate, max_steps)
    
    if algo_name == "merge sort":
        return merge_sort.MergeSort(initial_str, reading_error_rate, sorting_error_rate, max_steps)

