import numpy as np

A = np.array([0,6])
RangeA = np.array([1,7])


def listToAddress(a, rangeA):
    N = len(rangeA)
    sumtotal = 0
    for i in range(0, N):
        if a[i] < rangeA[i] and a[i] >= 0:
            multitotal = a[i]
            for j in range(i + 1, N):
                multitotal *= rangeA[j]
            sumtotal += multitotal
        else:
            sumtotal = -1
            break
    return sumtotal

def generateMaxN(rangea):
    maxN = 1
    for i in rangea:
        maxN *= i
    return maxN

def addressToList(address, rangeA):
    newList = np.array([])
    if (address >= 0 and address < generateMaxN(rangeA)):
        for i in range(len(rangeA) - 1, -1, -1):
            newList = np.insert(newList, 0, int(address % rangeA[i]))
            address //= int(rangeA[i])
    else:
        for i in range(len(rangeA)):
            newList = np.append(newList,-1)
    return newList.astype(int)

def generateArray(rangeA, N):
    newList = np.array([])
    if (N < generateMaxN(rangeA)):
        for i in range(len(rangeA) - 1, -1, -1):
            newList = np.insert(newList, 0, int(N % rangeA[i]))
            N //= int(rangeA[i])
        return newList.astype(int)
    else:
        return 0

def generateAllArrays(rangeA1):
    allArrays = np.array([])
    for i in range (0, generateMaxN(rangeA1)):
        allArrays = np.append(allArrays, [generateArray(rangeA1, i)])
    return allArrays.reshape(generateMaxN(rangeA1),len(rangeA1)).astype(int)

def printAllArrays(rangea):
    newArray = np.array(generateAllArrays(rangea))
    for i in range (0,len(newArray)):
        print(newArray[i])

def verif1(array, rangea):
    if (np.array_equal(array,addressToList(listToAddress(array, rangea), rangea))):
        return True
    else:
        return False

def verif2(N, rangea):
    if (N == -1):
        return False
    elif (N == listToAddress(addressToList(N, rangea), rangea)):
        return True
    else:
        return False

def verifAll(rangea):
    newArray = np.array(generateAllArrays(rangea))
    for i in range (0, len(newArray)):
        if (verif1(newArray[i], rangea) == False) or (verif2(i, rangea) == False):
            return False
    return True

print('Array =', A, 'Range array =', RangeA)
print('\tCall list to address =', listToAddress(A, RangeA))
print('\tCall address to list =', addressToList(listToAddress(A, RangeA), RangeA),'\n')
print('For A and RangeA:')
print('\tVerif1 return value:', verif1(A,RangeA))
print('\tVerif2 return value:', verif2(listToAddress(A,RangeA),RangeA),'\n')
print('For all possible arrays within range:')
print('\tVerification for all:', verifAll(RangeA),'\n')
print('All possible arrays within range')
printAllArrays(RangeA)
