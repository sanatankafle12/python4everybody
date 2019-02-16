
#ex_1
def computepay(hours,rate):

    if hours>40:
        pay=hours*rate*1.5
    else:
        pay=hours*rate

    print(pay)
while True:

    hours=input('Enter number of hours: ')
    rate=input('Enter rate per hour: ')
    try:
        hours=float(hours)
        rate=float(rate)
        break
    except:
        print('Please Enter a numerical value.')
        continue

print(computepay(hours,rate))
#ex_2
def computegrade(score):

        if score>1:
            return('Out of range')
        elif score>=0.9:
            return('A')
        elif score>=0.8:
            return('B')
        elif score>=0.7:
            return('C')
        elif score<0.7:
            return('D')
while True:
    score=input('Enter the score received: ')
    try:
        score=float(score)
        break
    except:
        print('Please Enter a numerical value.')
        continue
print(computegrade(0.8))
