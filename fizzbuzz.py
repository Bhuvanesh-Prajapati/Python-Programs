# FizzBuzz Program
for n in range(1,101):
    #check the divisibility of 'n' by '3' and '5'
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz") # if n is divisible by both '3' & '5'
    elif n % 3 == 0:
        print("fizz") # if n is divisible by only '3'
    elif n % 5 == 0:
        print("buzz") # if n is divisible by 5
    else:
        print(n) # if n is neither divisible by 3 nor by 5
