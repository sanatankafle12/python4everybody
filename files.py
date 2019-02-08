# fhand=input('Enter a file name: ')
# handle=open(fhand)
# for line in handle:
#     print(line.upper())
# # ex 03
file=input('Enter a file name: ')
if file=="na na boo boo":
    print('You have been punked')
else:
    handle=open(file)
    total=0
    count=0
    for lines in handle:
        lines=lines.rstrip()
        if lines.startswith('X-DSPAM-Confidence: '):
            z=lines.find(':')
            numbers=float(lines[z+1:])
            count=count+1
            total=total+numbers
    print(total)
    print(count)
    print(total/count)
