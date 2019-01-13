# import random built-in function

import random

# define a function with start and end range
def Rand(start, end):
# A list to store numbers
    n = []

# loop to iterate in the range
    for i in range(100):
# inserting the numbers in list
         n.append(random.randint(start, end))

# returning the list of random numbers
    return n

# printing out the result by calling the function
print(Rand(1, 100))
