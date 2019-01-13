# pass, break, continue
## pass keyword
def later():
    pass    # it will allow the program to run syntactically correct

later()
## break keyword
for i in range(10):
    if i == 7:
        break
    else:
        print('Using break: ',i)

## continue keyword
for j in range(10):
    if j in range(3,7):
        continue       ## skipping interation from j = 3 to 7(exclusive)-till 6.
    print('Using continue: ',j)
