# Insertion sort an unsorted array
# Remove a value from index one and shift to the right all higher values on the left of the gap


def insertion_sort(array):
    for i in range(1, len(array)):
        value = array[i]
        index_to_insert = i
        for j in range(i-1, -1, -1):
            if j >= 0:
                if array[j] > value:
                    array[j+1] = array[j]
                    index_to_insert = j
                else:
                    array[j+1] = value
                    break
        array[index_to_insert] = value
    return array


array_unsorted = [19, 3, 1, 17, 15, 4]
array_sorted = insertion_sort(array_unsorted)
print(array_sorted)

