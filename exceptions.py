## try,except block
try:
    for i in ['a','b','c']:
        print(i ** 2)
except TypeError:
    print('TypeError: Operation is not supported on strings')
    print('Tip: But you can print string multiple times by using * symbol, as follows:-')
    for i in ['a','b','c']:
        print(i * 2)

## try, except and finally block
a = 5
b = 0
try:
    c = a / b
except ZeroDivisionError:
    print('ZeroDivisionError: Wrong Operation Performed, It will return infinite.')
finally:
    print('Exception Handled Successfully !')

## try, except, else and finally block
def ask_in():

    while True:
        try:
            n = int(input("Input a number: "))
            sq = n ** 2
        except:
            print('ValueError: Wrong Input ! Try Again...')
            continue
        else:
            print(f'Square of the Number is: {sq}')
            break
        finally:
            print('Exception Handling was Successful !')

ask_in()
