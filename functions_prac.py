# function to check whether a number is in the given range(inclusive) or not ?
def check_range(num,low,high):
    print(num in range(low,high+1),'\nYes ! It\'s in the given range')

check_range(70,50,70)

# function to check the upper case and lower case letters in the given string:
def up_low(mystring):
    d = {'upper': 0,'lower': 0}
    for i in mystring:
        if i.isupper():
            d['upper'] += 1
        elif i.islower():
            d['lower'] += 1
        else:
            pass
    print('No of upper case letters: ',d['upper'])
    print('No of lower case letters: ',d['lower'])

up_low("Hey There ! It's Bhuvanesh Here.")

# function to return a unique list of items out of a list having duplicate items
def unique(items):
    #shortcut method
    print(list(set(items)))

    #simplified method
    x = []
    for a in items:
        if a not in x:
            x.append(a)
    print(x)

unique([1,2,2,3,3,3,4,4,4,4])

# function to multiply all the numbers in the list:
def multiply(nos):
    mult = 1
    for e in nos:
        mult *= e
    print(mult)

multiply([5,2,3,-4])
