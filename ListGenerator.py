'''
CSC 113 MIDTERM PROJECT

GROUP MEMBERS:
- Talike Bennett
- Deepankar Chakraborty
- Suhaima Islam
- Raynel Sanchez

LIST GENERATOR
'''

def list_generator(RA):
    
    list_of_lists = []
    
    for i in range(RA[0]):
        for j in range(RA[1]):
            newList = []
            newList.append(i)
            newList.append(j)
            list_of_lists.append(newList)
    
    return list_of_lists

# Test 1: RA = [3,1]
RA1=[3,1] 
A1 = list_generator(RA1);
for i in range(len(A1)):
    print(A1[i], end=" ")
