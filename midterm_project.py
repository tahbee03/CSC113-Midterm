# CSC 113 MIDTERM PROJECT
# GROUP MEMBERS:
#   Talike Bennett
#   Deepankar Chakraborty
#   Suhaima Islam
#   Raynel Sanchez

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


A = [3, 4, 5]
RA = [4, 5, 6]

print("A:", A)
print("RA:", RA)
print("Linear Address:", func1(A, RA))
print("Original List:", func2(func1(A, RA), RA))
