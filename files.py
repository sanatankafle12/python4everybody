fhand=input('Enter a file name: ')
handle=open(fhand)
for line in handle:
    print(line.upper())
