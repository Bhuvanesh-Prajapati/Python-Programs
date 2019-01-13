# Old MacDonald Problem
def old_macdonald(name):

    #using .upper method
    l1 = name[0]
    between = name[1:3]
    l4 = name[3]
    rest = name[4:]
    print(l1.upper() + between + l4.upper() + rest)

    #using .capatalize method
    half1 = name[:3]
    half2 = name[3:]
    print(half1.capitalize() + half2.capitalize())

old_macdonald('macdonald')

# Master Yoda Problem
def master_yoda(msg):
    # method 1
    print(msg.split()[-1::-1])

    # method 2 using .join()
    w_list = msg.split()
    reverse = w_list[::-1]
    print(' '.join(reverse))

master_yoda('Here i am')
master_yoda('i am home')

# Almost There:- return true if a number is 10 nearby with 100 or 200
def almost(n):
    print(abs(100-n) <= 10 or abs(200-n) <= 10)

almost(210)
