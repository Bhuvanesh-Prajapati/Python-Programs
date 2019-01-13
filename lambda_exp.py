my_nums = [2,3,4,5,6,7,8]
names = ['Bhuvanesh','James','Andrew']

# Square of each number in the list:
def square(num):
    return num**2

# Method 1 using for loop:

for i in my_nums:
    square(i)

# Method 2 using map() with for loop:
# Note:- map() can not be used alone because it'll return the memory location

for item in map(square,my_nums):
    print(item)

# Method 3 usimg map with list object:
print(list(map(square,my_nums)))

# filter the even number from my_nums:
def check_even(num):
    return num % 2 == 0

print(list(filter(check_even,my_nums)))

# Simple lambda expression:-known as Anonymous Function
square = lambda n:n ** 2
print(square(7))

# lambda exp with map():
print(list(map(lambda num:num ** 2,my_nums)))

# lambda exp with filter():
print(list(filter(lambda i:i % 2 == 0,my_nums)))

# lambda exp for string operations
print(list(map(lambda s:s[0],names)))
print(list(map(lambda s:s[::-1],names)))
