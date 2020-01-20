# Selection sort an unordered array
# efficiency - O(N^2)


def selection_sort(array):
    for i in range(len(array)-1):
        index_min = i
        for j in range(i+1, len(array), 1):
            if array[j] < array[index_min]:
                index_min = j
        if index_min != i:
            array[i], array[index_min] = array[index_min], array[i]
    return array


array = [19, 3, 1, 17, 15, 4]
array_sorted = selection_sort(array)
print(array_sorted)
