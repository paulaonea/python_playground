# Bubble sort an unsorted array
# Efficiency O(N^2)


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


array = [19, 3, 1, 17, 15, 4]
array_sorted = bubble_sort(array)
print(array_sorted)
