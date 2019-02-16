name=input('Enter your name: ')
print('Welcome ', name ,'\n Here we are learning about conditional statements.')
#ex_1 and ex_2
while True:
    hours=input('Enter no of hours: ')
    rate=input('Enter rate: ')
    try:
        hours=float(hours)
        rate=float(rate)
        if hours>40:
            pay=rate*hours*1.5
        else:
            pay=rate*hours
        print(pay)
        break
    except:
        print('Please Enter Numerical Value .')
        continue
#ex_3
while True:
    s=input('Enter a score: ')
    try:
        s=float(s)
        if s>1.0:
            print('Score out of range ')
        elif s>=0.9:
            print('A')
        elif s>=0.8:
            print('B')
        elif s>=0.7:
            print('C')
        elif s>=0.6:
            print('D')
        elif s<0.6:
            print('F')
        break
    except:
        print('Please Enter a numeric value')
        continue
