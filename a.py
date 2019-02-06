# a=dict()
# a['sana']=23
# a['tan0']=3
# a['apple']=24
# list=[]
# for (k,v) in a.items():
#     list.append((v,k))
#
# print(sorted(list,reverse=True))
#
file=raw_input('Enter a file: ')
counts=dict()
for line in file:
    words=line.split()
    counts.append(words)
lst=[]
for k,v in counts.items():
    lst.append((v,k))
lst=sorted(lst,reverse=True)
for v,k in lst[:10]:
    print(k,v)
