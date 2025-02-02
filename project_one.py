import pandas as pd
import numpy as np
import math

def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(number)


try:
    num = float(input("Enter a number to find its square root: "))
    result = calculate_square_root(num)
    print(f"The square root of {num} is {result}")
except ValueError as e:
    print(e)

