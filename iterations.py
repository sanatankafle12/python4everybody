total=0
count=0
z=[]
while True:
    inp=raw_input('Enter a no: ')
    if inp=='done':
        break
    try:
        i=float(inp)
        z.append(i)
    except:
        print('please Enter a numerical value')
        continue
    count=count+1
    total=total+i
print(total/count)
print(z)
print(max(z))
print(min(z))
print(len(z))
print(sum(z))
print(sum(z)/len(z))
