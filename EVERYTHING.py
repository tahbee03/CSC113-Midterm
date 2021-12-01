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


def func1(num_list, range_list):  # Converts a list of numbers into its equivalent integer address
    start_time = process_time_ns()

    N = len(num_list)
    address = 0

    for i in range(0, N):
        temp = num_list[i]
        for j in range(i + 1, N):
            temp *= range_list[j]
        address += temp

    end_time = process_time_ns()
    time_elapsed = end_time - start_time
    print("[Function 1 Process Time:", time_elapsed, "ns]")  # Prints the process time of func1()

    return address


def func2(address, range_list):  # Converts an integer address into its equivalent list of numbers
    start_time = process_time_ns()

    N = len(range_list)
    num_list = np.array([], dtype=int)
    for i in range(0, N):
        num_list = np.append(num_list, 0)

    for i in range(N - 1, -1, -1):
        num_list[i] = address % range_list[i]
        address //= range_list[i]

    end_time = process_time_ns()
    time_elapsed = end_time - start_time
    print("[Function 2 Process Time:", time_elapsed, "ns]")  # Prints the process time of func2()

    return num_list


def max_addresses(range_list):  # Returns the maximum number of addresses for the given range array
    start_time = process_time_ns()
    
    max_a = 1
    for i in range_list:
        max_a *= i
        
    end_time = process_time_ns()
    time_elapsed = end_time - start_time
    print("[max_addresses() Process Time:", time_elapsed, "ns]")  # Prints the process time of max_addresses()
    
    return max_a


def list_generator(range_list):  # Returns all the lists associated with the given range array
    start_time = process_time_ns()
    
    array_list = np.array([], dtype=int)
    for i in range(0, max_addresses(range_list)):
        array_list = np.append(array_list, func2(i, range_list))
        
    end_time = process_time_ns()
    time_elapsed = end_time - start_time
    print("[List Generator Process Time:", time_elapsed, "ns]")  # Prints the process time of max_addresses()
    
    return array_list.reshape(max_addresses(range_list), len(range_list))


# verification 1 (list -> address -> list)
# verification 2 (address -> list -> address)

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

print()
address = func1(A, RA)
print("Array -> Linear Address:", A, "->", address)

print()
A = func2(address, RA)
print("Linear Address -> Array:", address, "->", A)

print()
print("Maximum Number of Addresses for", RA, ":", max_addresses(RA))

print()
all_lists = list_generator(RA)
print("All possible number lists for", RA, ":")
for i in range(len(all_lists)):
    print(all_lists[i])

