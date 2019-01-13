# TO CHECK WHETHER A NUMBER IS A PALLINDROME OR NOT ?
num = int(input())
temp = num
rev = 0
while(num > 0):
    dig = num % 10
    rev *= 10 + dig
    num //= 10
print(temp == rev)

# TO CHECK WHETHER A STRING IS A PALLINDROME OR NOT ?
def chk_str(mystr):
    print(mystr == mystr[::-1])

chk_str("helleh")
