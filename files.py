# Reading a file
with open('new_text.txt', mode='r') as f:
    contents=f.read()
    print(contents)

# Appending a file
with open('new_text.txt', mode='a') as f:
    f.write('\nNew Text Inserted\n')

with open('new_text.txt', mode='r') as f:
    contents=f.read()
    print(contents)

# Writing a file:-
# it will overwrite an existing file
# or
# create a new one
with open('new_text_1.txt', mode='w') as f:
    f.write('Text 1 Inserted')
    f.write('\nText 2 Inserted')

with open('new_text_1.txt', mode='r') as f:
    contents=f.read()
    print(contents)
