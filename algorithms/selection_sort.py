# Selection sort an unordered array
# efficiency - O(N^2)


def selection_sort(array):
    for i in range(len(array)-1):
        minim, index = array[i], i
        for j in range(i+1, len(array), 1):
            if array[j] < minim:
                minim, index = array[j], j
        array[i], array[index] = array[index], array[i]
    return array


array = [19, 3, 1, 17, 15, 4]
array_sorted = selection_sort(array)
print(array_sorted)
