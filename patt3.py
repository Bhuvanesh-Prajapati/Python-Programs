# Number Pattern in alternate order of increasing and deceasing form 

n = int(input())
#straight form
for i in range(1,n+1,1):
    if i % 2 == 0:
        for j in range(i,0,-1):
            print(j, end=",")
        print()
    else:
        for k in range(1,i+1,1):
            print(k, end=",")
        print()
print()
#opposite form
for i in range(n,0,-1):
    if i % 2 == 0:
        for j in range(1,i+1,1):
            print(j, end=",")
        print()
    else:
        for k in range(i,0,-1):
            print(k, end=",")
        print()
