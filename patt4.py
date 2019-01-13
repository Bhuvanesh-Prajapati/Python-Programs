# Star Pattern in Triangle Shape

n = int(input())

#to print triangle with *
for i in range(n):
    for j in range(i+1):
        print("* ", end="")
    print()
print()

#to print opposite triangle with *
for i in range(n):
    for j in range(n,i,-1):
        print("* ", end="")
    print()
