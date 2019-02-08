#ex1
chop=[1,2,3,4,5,6]
middle=[]
for i in chop:
    if i not in [1,6]:
        middle.append(i)
print(middle)

#ex2
fhand = open('mbox.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) != 0 and words[0] == 'From':
        print(words[2])

ex03
file=open('romeo.txt')
list=[]
fhand=file.read()
words=fhand.split()
for word in words:
    if word not in list:
        list.append(word)
list.sort()
print(list)

ex04
file=input('Enter a file name: ')
hand=open(file)
count=0


for lines in hand:

    if lines.startswith('From: '):
        count=count+1
        line=lines.split()
        print(line[1])
print(count)


#ex05
z=[]
while True:
    inp=input('Enter a no: ')
    if inp=='done':
        break
    try:
        i=float(inp)
        z.append(i)
    except:
        print('please Enter a numerical value')
        continue
print(max(z))
print(min(z))
