# Selection sort an unordered array
# efficiency - O(N^2)


def selection_sort_asc(array):
    for i in range(len(array)-1):
        index_min = i
        for j in range(i+1, len(array), 1):
            if array[j] < array[index_min]:
                index_min = j
        if index_min != i:
            array[i], array[index_min] = array[index_min], array[i]
    return array


def selection_sort_dsc(array):
    for i in range(len(array)-1):
        index_max = i
        for j in range(i+1, len(array), 1):
            if array[j] > array[index_max]:
                index_max = j
        if index_max != i:
            array[i], array[index_max] = array[index_max], array[i]
    return array


array_unsorted = [19, 3, 1, 17, 15, 4]
array_sorted_asc = selection_sort_asc(array_unsorted)
print(array_sorted_asc)
array_sorted_dsc = selection_sort_dsc(array_unsorted)
print(array_sorted_dsc)
