# CSC 113 MIDTERM PROJECT
#
# GROUP MEMBERS:
#   Talike Bennett
#   Deepankar Chakraborty
#   Suhaima Islam
#   Raynel Sanchez
#
# FUNCTIONS 1 AND 2

def fill_array(size, array, range_array):
    for i in range(1, size + 1):
        prompt = "Element " + str(i) + ": "
        temp = int(input(prompt))
        while temp >= range_array[i - 1]:
            print("Your number goes out of range.",
                  "[" + str(temp) + " >= " + str(range_array[i - 1]) + "]")
            prompt = "Element " + str(i) + ": "
            temp = int(input(prompt))
        array.append(temp)
        
        
def fill_range_array(size, array):
    for i in range(1, size + 1):
        prompt = "Element " + str(i) + ": "
        temp = int(input(prompt))
        array.append(temp)
        

def func1(num_list, range_list): # FIX?
    N = len(num_list)
    address = 0

    for i in range(0, N):
        temp = num_list[i]
        for j in range(i + 1, N):
            temp *= range_list[j]
        address += temp

    return address


def func2(address, range_list): # FIX?
    N = len(range_list)
    num_list = []

    for i in range(0, N):
        num_list.append(0)

    for i in range(N - 1, -1, -1):
        num_list[i] = address % range_list[i]
        address //= range_list[i]

    return num_list


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
