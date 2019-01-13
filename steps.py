# FIND OUT THE COMMON STEPS OF FATHER AND SON IF THEIR SPEEDS AND POSITIONS ARE GIVEN
def commonSteps(f_pos,s_pos,speed,steps):
    v1 = speed[0]
    v2 = speed[1]
    l1 = []
    l2 = []
    l3 = []

    print("\nFather's Steps:")
    for i in range(steps):
        f_pos+=v1
        l1.append(f_pos)
        print(l1[i], end=",")
    print()

    print("\nSon's Steps:")
    for i in range(steps):
        s_pos+=v2
        l2.append(s_pos)
        print(l2[i], end=",")
    print()

    for i in range(steps):
        for j in range(steps):
            if(l1[i]==l2[j]):
                l3.append(l1[i])
                break

    print("\nCommon Steps")
    for i in range(len(l3)):
        print(l3[i], end=",")
    print()

    print("\nNumber of Common Steps")
    print(len(l3))

commonSteps(2,3,[2,1],20)
