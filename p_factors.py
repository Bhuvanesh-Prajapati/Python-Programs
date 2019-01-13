# function to find out prime factors of a number
def factor(n):
        for i in range(2, n):
            while n % i == 0:
                n = n // i
                # f-string method
                print(f"prime factors are: {i}")
                # .format method
                # print("prime factors are: {}".format(i))

factor(int(input()))
