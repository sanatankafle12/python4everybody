import random

for i in range(10):
    x = random.randint(1,10)
    print(x)







# #ex_1
# def computepay(hours,rate):
#     if hours>40:
#         pay=hours*rate*1.5
#     else:
#         pay=hours*rate
#
#     print(pay)
# computepay(77,2)
# #ex_2
# def computegrade(score):
#     try:
#         score=float(score)
#         if score>1:
#             return('Out of range')
#         elif score>=0.9:
#             return('A')
#         elif score>=0.8:
#             return('B')
#         elif score>=0.7:
#             return('C')
#         elif score<0.7:
#             return('D')
#     except:
#         return('Plese Enter a numeric value')
# print(computegrade(0.8))
