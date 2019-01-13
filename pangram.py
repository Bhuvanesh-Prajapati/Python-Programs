import string

def pangram(mystr,alphabet=string.ascii_lowercase):
    # store values of alphabet into alphaset in the form of set
    alphaset = set(alphabet)
    # compare whether or not alphaset has all the values of mystr.lower()
    # if 'Yes' return 'True' else 'False'
    print(alphaset <= set(mystr.lower()))

pangram("The Quick Brown Fox Jumps Over a Lazy Dog")
