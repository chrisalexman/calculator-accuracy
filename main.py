'''
Calculating the accuracy of the TI-36X Pro calculator using Taylor & Maclaurin series expansions.

NOTE: constraint, calculator can represent max of 9 digits to the right of the decimal

Functions to test:
- exponential (e^x)
- trigonometric (sin x)

https://en.wikipedia.org/wiki/Taylor_series
'''

import math


# get expected sum for exponential function
def get_expected_exponential(x):
    return round(math.exp(x), 9)


# get expected sum for sine function
def get_expected_sine(x):
    return round(math.sin(x), 9)


# approximate the sum of the exponential function
def calculate_exponential(x, loop):

    '''
    exponential function e^x

    Maclaurin series:
        e^x = x^n / n! = 1 + x + x^2/2! + x^3/3! + ...

    --------------------------------------
    | TI-36X | e^2         | 7.389056099 |
    | Python | math.exp(2) | 7.389056099 |
    --------------------------------------
    '''

    numerator = x ** loop
    denominator = math.factorial(loop)

    return numerator / denominator


# approximate the sum of the sine function
def calculate_sine(x, loop):

    '''
    trigonometric function sin(x)

    Maclaurin series:
        sin(x) = [(-1^n) * x^(2n + 1)] / (2n + 1)! = x - (x^3)/3! + (x^5)/5! - ...

    --------------------------------------
    | TI-36X | sin(2)      | 0.909297427 |
    | Python | math.sin(2) | 0.909297427 |
    --------------------------------------
    '''
    
    numerator = ((-1) ** loop) * (x ** (2 * loop + 1))
    denominator = math.factorial(2 * loop + 1)

    return numerator / denominator


# dictionary of functions to test
functions_to_test = {
    'exponential': {
        'expected'  : get_expected_exponential,
        'calculate' : calculate_exponential
    },
    'sine': {
        'expected'  : get_expected_sine,
        'calculate' : calculate_sine
    }
}


# iterate through dictionary of functions to calculate the accuracy of the TI-36X Pro calculator
def calculate_accuracies():

    x = 2
    loops = 99
    num_tries = 0
    result_sum = 0.0

    for key, value in functions_to_test.items():

        expected = value['expected'](x)

        for loop in range(loops):

            result_sum += value['calculate'](x, loop)
            rounded_result = round(result_sum, 9)
            num_tries += 1

            if(rounded_result == expected):
                print(f'{key} function:\nneeded {num_tries} terms to reach result of {rounded_result}\n')
                break
        
        result_sum = 0.0
        num_tries = 0


if __name__ == '__main__':
    calculate_accuracies()
