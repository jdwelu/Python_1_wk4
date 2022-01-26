# Creating a 10 element list that tests for randomly generated 3's and
# then increments that position by 1. A 3 has about a 10 pecent chance
# of showing up in any position, so after 1000 tries each of these
# numbers should be somewhere close to 100. 

# Need the random library
import random

# Creates a list of ten zeroes and prints to confirm
numregister = [0] * 10
# print(numregister)
# print()
print("The empty list is: ", numregister)

# This is needed to loop the whole array
bigloop = 0
while bigloop < 1000:
    
    # Loops through each element and tests for a 3, then adds 1
    smloop = 0
    while smloop < 10:
        # print()
        x = random.randint(1,10)
        # print(x)
        if x == 3:
            numregister[smloop] = numregister[smloop] + 1
        # print(numregister[count])
        # print()
        smloop = smloop + 1

    bigloop = bigloop + 1
    
print()
print("After testing for random 3's: ", numregister)
print()






