# Diamond Pattern
n = int(input())

# loop for upper half
for i in range(n-1):
    print((n-i) * ' ' + (2*i+1) * '*')

# loop for lower half
for j in range(n-1, -1, -1):
    print((n-j) * ' ' + (2*j+1) * '*')
