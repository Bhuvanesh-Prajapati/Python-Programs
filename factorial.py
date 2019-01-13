# Factorial of a number
## Naive Method
n = int(input())
fact = 1

for i in range(1,n+1):
	fact = fact * i

print ("The factorial of",n "is : ",end="")
print (fact)

## Without using recursion
def fact(n):
    result = 1
    if( n <= 1):
      print(1)
    for i in range(2, n + 1):
      result = result * i
    print ("The factorial of",n "is : ",end="")
    print(result)

fact(6)
