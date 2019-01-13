# program 1
def numbers(a,b):
    if a % 2 == 0 and b % 2 == 0:
        print(min(a,b))
    else:
        print(max(a,b))

numbers(10,12)

#program 2
def animal(text):
    wordlist = text.lower().split()
    print(wordlist[0][0] == wordlist[1][0])

animal('lion leopard')
animal('fox kangaroo')

#program 3
def sum_int(a,b):
    print(a+b == 20 or a+b > 20 or a == 20 or b == 20)

sum_int(5,17)
