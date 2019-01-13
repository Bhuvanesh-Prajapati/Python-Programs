# two.py

import one

print('Top level indentation in two.py')

one.func()

if __name__ == '__main__':
    print('two.py is Being Run Directly')
else:
    print('two.py has been imported')
