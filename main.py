'''

Calculating the accuracy of the TI-36X Pro calculator using Taylor & Maclaurin series expansions.

NOTE: constraint, calculator can represent max of 9 digits to the right of the decimal

Functions to test:
- exponential (e^x)

https://en.wikipedia.org/wiki/Taylor_series

'''

import math


def calculate_exponential():

    '''
    exponential function e^x

    Maclaurin series:
        e^x = x^n / n! = 1 + x + x^2/2! + x^3/3! + ...

    for this test, x = 2

    --------------------------------------
    | TI-36X | e^2         | 7.389056099 |
    | Python | math.exp(2) | 7.389056099 |
    --------------------------------------
    '''

    x = 2
    expected = round(math.exp(x), 9)

    num_tries = 0
    loops = 99
    result = 0

    for loop in range(loops):

        numerator = x ** loop
        denominator = math.factorial(loop)

        result += numerator / denominator
        rounded_result = round(result, 9)

        num_tries += 1

        if(rounded_result == expected):
            print(f'exponential function e^x:\nneeded {num_tries} terms to reach result of {rounded_result}')
            break


if __name__ == '__main__':
    calculate_exponential()