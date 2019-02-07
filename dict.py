
counts={}
line=input('Enter a text: ')
words=line.split()
print('Words', words)
for word in words:
    counts[word]=counts.get(word,0)+1

print(counts)



# for loop in dictionary
for k in counts:
    print(k,counts[k])
print(counts.keys())
z=counts.values()
print(max(z))
print(counts.items())


# for understanding two iteration variable

jjj={'sanatan':2,'sudip':3,'ds':34}
for key,value in jjj.items():
    print(key,value)




#understanding dictionary and files

name=input('Enter a file: ')
handle=open(name)

counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)


z=list(counts.keys())
print(z.reverse())
