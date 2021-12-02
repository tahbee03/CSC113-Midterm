from time import process_time_ns
import numpy as np


def fill_array(size, array, range_array):  # Fills the number array with user input

    for i in range(1, size + 1):
        prompt = "Element " + str(i) + ": "
        temp = int(input(prompt))
        while temp >= range_array[i - 1]:
            print("Your number goes out of range.",
                  "[" + str(temp) + " >= " + str(range_array[i - 1]) + "]")
            prompt = "Element " + str(i) + ": "
            temp = int(input(prompt))
        array = np.append(array, temp)
    return array


def fill_range_array(size, array):  # Fills the range array with user input

    for i in range(1, size + 1):
        prompt = "Element " + str(i) + ": "
        temp = int(input(prompt))
        array = np.append(array, temp)
    return array


def func1(num_list, range_list):  # Converts a list of numbers into its equivalent integer address; list--> address
    N = len(num_list)
    address = 0

    for i in range(0, N):
        temp = num_list[i]
        for j in range(i + 1, N):
            temp *= range_list[j]
        address += temp
    return address


def func2(address, range_list):  # Converts an integer address into its equivalent list of numbers;  address -> list
    N = len(range_list)
    num_list = np.array([], dtype=int)
    for i in range(0, N):
        num_list = np.append(num_list, 0)
    for i in range(N - 1, -1, -1):
        num_list[i] = address % range_list[i]
        address //= range_list[i]
    return num_list


def max_addresses(range_list):  # Returns the maximum number of addresses for the given range array
    max_a = 1
    for i in range_list:
        max_a *= i
    return max_a


def list_generator(range_list):  # Returns all the lists associated with the given range array
    array_list = np.array([], dtype=int)
    for i in range(0, max_addresses(range_list)):
        array_list = np.append(array_list, func2(i, range_list))
    return array_list.reshape(max_addresses(range_list), len(range_list))


# verification 1 (list -> address -> list)
def verif1(array, rangea):
    if (np.array_equal(array, func2(func1(array, rangea), rangea))):
        return True
    else:
        return False

# verification 2 (address -> list -> address)
def verif2(address, rangea):
    if (address == -1):
        return False
    elif (address == func1(func2(address, rangea), rangea)):
        return True
    else:
        return False

def verifAll(rangea):
    newArray = np.array(list_generator(rangea))
    for i in range(0, len(newArray)):
        if (verif1(newArray[i], rangea) == False) or (verif2(i, rangea) == False):
            return False
    return True

def verifAll2(array, rangea):
    for i in range(0, len(array)):
        if (verif1(array[i], rangea) == False) or (verif2(i, rangea) == False):
            return False
    return True

A = np.array([3, 4, 5], dtype=int)
RA = np.array([4, 5, 6], dtype=int)
A = np.array([], dtype=int)
RA = np.array([], dtype=int)

start_time = process_time_ns()              # Records start time of function
size = int(input("What is the size of your array? "))
end_time = process_time_ns()                # Records end time of function
time_elapsed = end_time - start_time        # Time elapse is the difference between start and end times
print("Time elapsed in operation:", time_elapsed, "ns.")
print()


print("Size:", size)
start_time = process_time_ns()              # Records start time of function
print("Enter the elements for the range array.")
RA = fill_range_array(size, RA)
end_time = process_time_ns()                # Records end time of function
time_elapsed = end_time - start_time        # Time elapse is the difference between start and end times
print("Time elapsed in operation:", time_elapsed, "ns.")
print()

print("Size:", size)
start_time = process_time_ns()              # Records start time of function
print("Enter the elements for the number array.")
A = fill_array(size, A, RA)
end_time = process_time_ns()                # Records end time of function
time_elapsed = end_time - start_time        # Time elapse is the difference between start and end times
print("Time elapsed in operation:", time_elapsed, "ns.")
print()

print("Array:", A)
print("Range Array:", RA)

print()
start_time = process_time_ns()              # Records start time of function
address = func1(A, RA)
print("Array -> Linear Address:", A, "->", address)
end_time = process_time_ns()                # Records end time of function
time_elapsed = end_time - start_time        # Time elapse is the difference between start and end times
print("Time elapsed in operation:", time_elapsed, "ns.")

print()
start_time = process_time_ns()              # Records start time of function
A = func2(address, RA)
print("Linear Address -> Array:", address, "->", A)
end_time = process_time_ns()                # Records end time of function
time_elapsed = end_time - start_time        # Time elapse is the difference between start and end times
print("Time elapsed in operation:", time_elapsed, "ns.")

print()
start_time = process_time_ns()              # Records start time of function
print("Maximum Number of Addresses for", RA, ":", max_addresses(RA))
end_time = process_time_ns()                # Records end time of function
time_elapsed = end_time - start_time        # Time elapse is the difference between start and end times
print("Time elapsed in operation:", time_elapsed, "ns.")

print()
start_time = process_time_ns()              # Records start time of function
all_lists = list_generator(RA)
end_time = process_time_ns()                # Records end time of function
time_elapsed = end_time - start_time        # Time elapse is the difference between start and end times
print("Time elapsed in operation:", time_elapsed, "ns.")
print("All possible number lists for", RA, ":")
start_time = process_time_ns()              # Records start time of function
for i in range(len(all_lists)):
    print(all_lists[i])
end_time = process_time_ns()                # Records end time of function
time_elapsed = end_time - start_time        # Time elapse is the difference between start and end times
print("Time elapsed in operation:", time_elapsed, "ns.")

print()
print("Verification 1: Performs the verification between the list -> address -> list")
start_time = process_time_ns()              # Records start time of function
print(verif1(A, RA))
end_time = process_time_ns()                # Records end time of function
time_elapsed = end_time - start_time        # Time elapse is the difference between start and end times
print("Time elapsed in operation:", time_elapsed, "ns.")

print()
print("Verification 2: Performs the verification between the address -> list -> address")
start_time = process_time_ns()              # Records start time of function
print(verif2(func1(A, RA), RA))
end_time = process_time_ns()                # Records end time of function
time_elapsed = end_time - start_time        # Time elapse is the difference between start and end times
print("Time elapsed in operation:", time_elapsed, "ns.")

print()
print("Verification ( Generating all possible number lists for", RA, ") by running Verifications 1 and 2:")
start_time = process_time_ns()              # Records start time of function
print(verifAll(RA))
end_time = process_time_ns()                # Records end time of function
time_elapsed = end_time - start_time        # Time elapse is the difference between start and end times
print("Time elapsed in operation:", time_elapsed, "ns.")

print()
print("Verification ( Using generated all possible number lists for", RA, ") by running Verifications 1 and 2:")
start_time = process_time_ns()              # Records start time of function
print(verifAll2(all_lists, RA))
end_time = process_time_ns()                # Records end time of function
time_elapsed = end_time - start_time        # Time elapse is the difference between start and end times
print("Time elapsed in operation:", time_elapsed, "ns.")
