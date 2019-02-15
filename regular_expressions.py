import re
# file=open('mbox.txt')
# for line in file:
#     line=line.rstrip()
#     if re.search('^X.*:', line):
#         print(line)

# x='my name is 23 and i habe 09 as jdoias 23'
# y=re.findall('[m-y]+',x)
# print(y)
x='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y=re.findall('@([^ ]*)',x)

print(y)
