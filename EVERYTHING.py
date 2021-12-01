"""
CSC 113 MIDTERM PROJECT

GROUP MEMBERS:
    Talike Bennett
    Deepankar Chakraborty
    Suhaima Islam
    Raynel Sanchez

* NumPy information: https://numpy.org/doc/stable/reference/generated/numpy.array.html
* Timestamp derivation: https://www.geeksforgeeks.org/time-process_time-function-in-python/
"""
from time import process_time_ns
import numpy as np


def fill_array(size, array, range_array):  # Fills the number array with user input
    start_time = process_time_ns()

    for i in range(1, size + 1):
        prompt = "Element " + str(i) + ": "
        temp = int(input(prompt))
        while temp >= range_array[i - 1]:
            print("Your number goes out of range.",
                  "[" + str(temp) + " >= " + str(range_array[i - 1]) + "]")
            prompt = "Element " + str(i) + ": "
            temp = int(input(prompt))
        array = np.append(array, temp)

    end_time = process_time_ns()
    time_elapsed = end_time - start_time
    print("[fill_array() Process Time:", time_elapsed, "ns]")  # Prints the process time of fill_array()

    return array


def fill_range_array(size, array):  # Fills the range array with user input
    start_time = process_time_ns()

    for i in range(1, size + 1):
        prompt = "Element " + str(i) + ": "
        temp = int(input(prompt))
        array = np.append(array, temp)

    end_time = process_time_ns()
    time_elapsed = end_time - start_time
    print("[fill_range_array() Process Time:", time_elapsed, "ns]")  # Prints the process time of fill_range_array()

    return array
  
  
# blah blah blah

A = np.array([], dtype=int)
RA = np.array([], dtype=int)

size = int(input("What is the size of your array? "))
print()

print("Size:", size)
print("Enter the elements for the range array.")
RA = fill_range_array(size, RA)
print()

print("Size:", size)
print("Enter the elements for the number array.")
A = fill_array(size, A, RA)
print()

print("Array:", A)
print("Range Array:", RA)
