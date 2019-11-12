
def convert_from_roman(value):
    roman_letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = len(value)
    number = roman_letters[value[-1]]

    if len(value) > 1:
        for i in range(2, n+1):
            if roman_letters[value[n-i]] < number:
                number -= roman_letters[value[n-i]]
            else: number += roman_letters[value[n-i]]
    return number

