# Number Patterns in Triangle Shape

n = int(input())
# print numbers in increasing order in triangle shape
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print(j, end=",")
    print()
print()
# print numbers in increasing order in opposite triangle shape
for i in range(n):
    for j in range(n,i,-1):
        print(j, end=",")
    print()
