# CSC 113 MIDTERM PROJECT
#
# GROUP MEMBERS:
#   Talike Bennett
#   Deepankar Chakraborty
#   Suhaima Islam
#   Raynel Sanchez
#
# FUNCTIONS 1 AND 2

# NOTE: Timestamp printing derived from
# GeeksforGeeks (https://www.geeksforgeeks.org/time-process_time-function-in-python/)
from time import process_time_ns
import numpy as np

def fill_array(size, array, range_array): # Fills the number array with user input
    start_time = process_time_ns()
    
    for i in range(1, size + 1):
        prompt = "Element " + str(i) + ": "
        temp = int(input(prompt))
        while temp >= range_array[i - 1]:
            print("Your number goes out of range.",
                  "[" + str(temp) + " >= " + str(range_array[i - 1]) + "]")
            prompt = "Element " + str(i) + ": "
            temp = int(input(prompt))
        array.append(temp)
        
    end_time = process_time_ns()
    time_elapsed = end_time - start_time
    print("[fill_array() Process Time:", time_elapsed, "ns]") # Prints the process time of fill_array()
        
        
def fill_range_array(size, array): # Fills the range array with user input
    start_time = process_time_ns()
    
    for i in range(1, size + 1):
        prompt = "Element " + str(i) + ": "
        temp = int(input(prompt))
        array.append(temp)
        
    end_time = process_time_ns()
    time_elapsed = end_time - start_time
    print("[fill_range_array() Process Time:", time_elapsed, "ns]") # Prints the process time of fill_range_array()
        

def func1(num_list, range_list): # Converts a list of numbers into its equivalent integer address
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
    print("[Function 1 Process Time:", time_elapsed, "ns]") # Prints the process time of func1()

    return address


def func2(address, range_list): # Converts an integer address into its equivalent list of numbers
    start_time = process_time_ns()
    
    N = len(range_list)
    num_list = []
    for i in range(0, N):
        num_list.append(0)

    for i in range(N - 1, -1, -1):
        num_list[i] = address % range_list[i]
        address //= range_list[i]
        
    end_time = process_time_ns()
    time_elapsed = end_time - start_time
    print("[Function 2 Process Time:", time_elapsed, "ns]") # Prints the process time of func2()

    return num_list

def generateMaxN(rangea):
    maxN = 1
    for i in rangea:
        maxN *= i
    return maxN

def generateArray(rangeA, N):
    newList = np.array([])
    if (N < generateMaxN(rangeA)):
        for i in range(len(rangeA) - 1, -1, -1):
            newList = np.insert(newList, 0, int(N % rangeA[i]))
            N //= int(rangeA[i])
        return newList.astype(int)
    else:
        return 0

def listGenerator(rangeA1):
    start_time = process_time_ns()
    
    allArrays = np.array([])
    for i in range (0, generateMaxN(rangeA1)):
        allArrays = np.append(allArrays, [generateArray(rangeA1, i)])
    return allArrays.reshape(generateMaxN(rangeA1),len(rangeA1)).astype(int)
    
    end_time = process_time_ns()
    time_elapsed = end_time - start_time
    print("[List Generator Process Time:", time_elapsed, "ns]") # Prints the process time of list generator

def printAllArrays(rangea):
    newArray = np.array(listGenerator(rangea))
    for i in range (0,len(newArray)):
        print(newArray[i])

def verif1(array, rangea):
    if (np.array_equal(array,func2(func1(array, rangea), rangea))):
        return True
    else:
        return False

def verif2(N, rangea):
    if (N == -1):
        return False
    elif (N == func1(func2(N, rangea), rangea)):
        return True
    else:
        return False

def verifAll(rangea):
    newArray = np.array(listGenerator(rangea))
    for i in range (0, len(newArray)):
        if (verif1(newArray[i], rangea) == False) or (verif2(i, rangea) == False):
            return False
    return True

A = []
RA = []
size = int(input("What is the size of your array? "))
print()

print("Size:", size)
print("Enter the elements for the range array.")
fill_range_array(size, RA)
print()

print("Size:", size)
print("Enter the elements for the number array.")
fill_array(size, A, RA)
print()

print("Array:", A)
print("Range Array:", RA)
address = func1(A, RA)
print("Array -> Linear Address:", A, "->", address)
print("Linear Address -> Array:", address, "->", func2(address, RA))

print('\nFor A and Range Array:')
print('\tVerif1 return value:', verif1(A,RA))
print('\tVerif2 return value:', verif2(func1(A,RA),RA),'\n')
print('For all possible arrays within range:')
print('\tVerification for all:', verifAll(RA),'\n')
print('All possible arrays within range')
printAllArrays(RA)
