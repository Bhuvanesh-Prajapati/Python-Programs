# Return count of upper case or lower case letters in a file
c1 = 0
c2 = 0
name1 = 'new_text.txt'
## for the file at same location where the program file is:
with open('new_text.txt') as t:
    for i in t.read():
        if i.isupper():
            c1 += 1
        elif i.islower():
            c2 += 1
        else:
            pass

    ### .format method
    print('The no of upper case letters in {} is: '.format(name1),c1)
    print('The no of lower case letters in {} is: '.format(name1),c2)

## for the file at different location on a machine
import os
os.chdir('F:\\')

c3 = 0
c4 = 0
name2 = 'doc.txt'
with open('doc.txt') as d:
    for j in d.read():
        if j.isupper():
            c3 += 1
        elif j.islower():
            c4 += 1
        else:
            pass

    ### f-string method
    print(f'The no of upper case letters in {name2} is: ',c3)
    print(f'The no of lower case letters in {name2} is: ',c4)
