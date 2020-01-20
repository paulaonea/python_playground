# Check an array for duplicates


# 1. Quadratic solution:
# Efficiency of this algorithm is O(N^2) as it has two nested for loops.
def check_duplicates_algorithm1(array):
    for i in range(len(array) -1):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                return f'The array contains duplicates'
    return f'The array does not contain duplicates'


def check_duplicates_algorithm2(array):
    # Efficiency of this algorithm is O(N) as there are two separate for loops.
    a = []
    for i in range(max(array)+1):
        a.append(0)
    for i in range(len(array)):
        if a[array[i]] == 1:
            return f'The array contains duplicates'
        else:
            a[array[i]] = 1
    return f'The array does not contain duplicates'


array = [1, 4, 8, 3, 5, 7, 9, 9]
print(check_duplicates_algorithm2(array))
print(max(array))