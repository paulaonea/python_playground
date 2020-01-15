# Linear search = search every element of the array starting with position 0, until the value is found or until the end.


def linear_search(array, number):
    for i in range(len(array)-1):
        if array[i] == number:                          # The search stops here, no need to go to the end
            return f'Value {number} was found at position {i+1}.'
    return f'Value {number} was not found in the array.'


array = [1, 12, 14, 18, 30]
value = 18
print(linear_search(array, value))
