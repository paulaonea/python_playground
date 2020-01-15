# Linear search = search every element of the array starting with position 0, until the value is found or until the end.
# Efficiency O(log(N))


def binary_search(array, number):
    start_index = 0
    end_index = len(array)-1
    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        if array[middle_index] == number:   # The search stops here, no need to go to the end
            return f'Value {number} was found at position {middle_index + 1}.'
        elif array[middle_index] < number:
            start_index = middle_index + 1
        else:
            end_index = middle_index - 1
    return f'Value {number} was not found in the array.'


array = [1, 12, 14, 18, 30]
value = 2
print(binary_search(array, value))
