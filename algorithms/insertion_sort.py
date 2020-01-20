# Insertion sort an unsorted array
# Remove a value from index one and shift to the right all higher values on the left of the gap


def insertion_sort_asc(array):
    for i in range(1, len(array)):
        value = array[i]
        index_to_insert = i
        while index_to_insert > 0 and array[index_to_insert - 1] > value:
            array[index_to_insert] = array[index_to_insert -1]
            index_to_insert -=1
        array[index_to_insert] = value
    return array


def insertion_sort_dsc(array):
    for i in range(1, len(array)):
        value = array[i]
        index_to_insert = i
        while index_to_insert > 0 and array[index_to_insert - 1] < value:
            array[index_to_insert] = array[index_to_insert -1]
            index_to_insert -=1
        array[index_to_insert] = value
    return array


array_unsorted = [19, 3, 1, 17, 15, 4]
array_sorted_asc = insertion_sort_asc(array_unsorted)
print(array_sorted_asc)
array_sorted_dsc = insertion_sort_dsc(array_unsorted)
print(array_sorted_dsc)
