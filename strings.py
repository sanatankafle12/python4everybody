str = 'X-DSPAM - Confidence : 0.8475'
z=str.find(':')
print(float(str[z+1:]))
