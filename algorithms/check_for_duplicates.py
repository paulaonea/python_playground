# Check an array for duplicates
# Efficiency O(N^2)


def check_duplicates(array):
    for i in range(len(array) -1):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                return f'The array contains duplicates'
    return f'The array does not contain duplicates'


array = [12, 14, 18, 30, 32, 52, 22, 22]
print(check_duplicates(array))
