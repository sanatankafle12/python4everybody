name=input('Enter youe name : ')
print('Welcome ',name,'\nHere are some exercises that consists of various use of list to perform various tasks. \nLets get started.')
#ex1 extracting a list of middle values of the given list.
print('This prints out all the values in list excluding the first and last value')
chop=[1,2,3,4,5,6]
middle=[]
for i in chop:
    if i not in [1,6]:
        middle.append(i)
print(middle)

#ex2 Using list and file
print('This prints out the third word from line that starts with "From" in given file.')
fhand = open('mbox.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) != 0 and words[0] == 'From':
        print(words[2])
        count=count+1
print(count)
#ex03 Using list to remove repeated words in a file
print('This prints out a list of words in a file without duplicates')

file=open('romeo.txt')
list=[]
fhand=file.read()
words=fhand.split()
for word in words:
    if word not in list:
        list.append(word)
list.sort()
print(list)

#ex04 Same as ex_02
print('This prints the total number of lines starting with "From: "')
file=input('Enter a file name: ')
hand=open(file)
count=0


for lines in hand:

    if lines.startswith('From: '):
        count=count+1
        line=lines.split()
        line[1]
print(count)


#ex05 Using lists to find out highest and lowest values
print('This prints out the max and min value of entered numbers. \nPlease Enter done when your list is completed.')
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
