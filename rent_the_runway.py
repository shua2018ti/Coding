"""
Multiply two numbers represented as lists
"""

def multiply_numbers(number_1, number_2):
    zero_pad = 0
    running_sum = []
    if len(number_1) < len(number_2):
        number_1, number_2 = number_2, number_1
