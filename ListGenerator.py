'''
CSC 113 MIDTERM PROJECT

GROUP MEMBERS:
- Talike Bennett
- Deepankar Chakraborty
- Suhaima Islam
- Raynel Sanchez

LIST GENERATOR
'''

def list_generator(RA) :
    
    for i in range(RA[0]):
        
        for j in range(RA[1]):
            print(i, j, end="\n")

print("Test 1: RA=[3,1]")    
RA1=[3,1] 
list_generator(RA1);
print("\n")

print("Test 2: RA=[3,2]")
RA2=[3,2] 
list_generator(RA2);
print("\n")

print("Test 3: RA=[3,2]")
RA3=[2,3] 
list_generator(RA3);
