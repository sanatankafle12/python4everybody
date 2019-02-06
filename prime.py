from math import sqrt

def prime_or_not_prime(num):
    if num==0 or num==1:
        return(False)
    for i in range(2,num):
        if num%i==0:
             return(False)
    return(True)



def prime_or_not_prime_sqrt(num):
    if num==0 or num==1:
        return(False)
    for i in range(2,int(sqrt(num)):
        if num%i==0:
             return(False)
    return(True)

for num in range(1,21):
    print(num,prime_or_not_prime_sqrt(num))
