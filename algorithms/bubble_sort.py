# Bubble sort an unsorted array
# Efficiency O(N^2)


def bubble_sort(array):
    sort = False
    for i in range(len(array)):
        if not sort:
            sort = True
            for j in range(len(array)-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    sort = False
        else:
            return array
    return array


array = [19, 3, 1, 17, 15, 4]
array_sorted = bubble_sort(array)
print(array_sorted)
