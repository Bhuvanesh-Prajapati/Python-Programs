# find 33 problem
def find33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            print(True)
    else:
        print(False)

find33([1,3,3])

# # Paper Doll Problem
# def p_doll(str):
#     result = ''
#     for i in str:
#         result += i * 3
#     print(result)
#
# p_doll("Hello")
#
# # BlackJack Problem
# def blackjack(a,b,c):
#     if sum([a,b,c]) <= 21:
#         print(sum([a,b,c]))
#     elif sum([a,b,c]) > 21 and 11 in [a,b,c]:
#         print(sum([a,b,c])-10)
#     elif sum([a,b,c]) > 21:
#         print("Bust")
#     else:
#         pass
#
# blackjack(6,8,11)
#
# # Summer of 69
# def summer(arr):
#     sum = 0
#     add = True
#     for num in arr:
#         # to check whether the num is 6
#         while add:
#             if num != 6:
#                 sum += num
#                 break
#             else:
#                 add = False
#         # waiting for the 9 & continue the sum further 9
#         while not add:
#             if num != 9:
#                 break
#             else:
#                 add = True
#                 break
#
#     print(sum)
#
# summer([1,5,6,12,9,11])
