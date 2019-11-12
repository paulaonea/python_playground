
def convert_from_roman(value):
    # Go through Roman number letter by letter starting from the end
    # If current letter is smaller in value than the previous letter, the final value decreases (IV, IX, etc)
    # If current letter is larger in value than the previous letter, the final value increases

    roman_letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = len(value)
    number = roman_letters[value[-1]]
    if len(value) > 1:
        for i in range(2, n+1):
            if roman_letters[value[n-i]] < number:
                number -= roman_letters[value[n-i]]
            else: number += roman_letters[value[n-i]]
    return number


def convert_to_roman(number):
    roman_letters = {'M': 1000, 'CM': 900,
                     'D': 500, "CD": 400,
                     'C': 100, 'XC': 90,
                     'L': 50, 'XL': 40,
                     'X': 10, 'IX': 9,
                     'V': 5, 'IV': 4, 'I': 1
                     }
    roman_number = ''
    for key, val in roman_letters.items():
        while number >= val:
            roman_number += key
            number -= val
    return roman_number
