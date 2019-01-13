# range(start,stop,step(optional))
# 500 is not included here, because it goes upto not included
for num in range(100,500):
    sum = 0
    temp = num
    while temp > 0:
        dig = temp % 10
        sum += dig ** 3 # shortcut for sum = sum + dig ** 3
        temp //= 10 # similar to temp = temp // 10

    if num == sum:
        print(num,"is an Armstrong Number.")
