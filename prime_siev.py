# from prime import prime_or_not_prime_sqrt, prime_or_not_prime
# import sys
# import time
#
# def primes(num):
#     primes_upto_num=[2]
#     for i in range(3,num+1, 2):
#         if prime_or_not_prime_sqrt(i) is True:
#             primes_upto_num.append(i)
#     return(primes_upto_num)
#
# def primes_seiv(num):
#     primes=[]
#     for i in range(2,num+1):
#         if i not in primes:
#             if prime_or_not_prime(i) is True:
#                 for j in range(i*i,num+1,i):
#                     del primes[j]
#     return(primes)
#
#
#
# print(primes(num))


pp = 2
ps = [pp]
lim = raw_input("Generate prime numbers up to what number? : ")
while pp < int(lim):
    pp += 1
    for a in ps:
        if pp%a==0:
            break
        else:
            ps.append(pp)


# print set(ps)
