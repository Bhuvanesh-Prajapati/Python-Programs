# function to find out which words can be formed with mWord
def compare(mWord,numWord,dictWord):
    l = len(mWord) #length of mWord
    for i in range(numWord): # loop for all the words in dictWord
        w_len = len(dictWord[i]) # length of each word in dictWord
        index = 0
        f = 1 #flag
        for j in range(w_len): # loop for each word in dictWord
            ch = dictWord[i][j] # character of the word in dictWord

            for k in range(index,l): # loop to compare the mWord and the word in dictWord
                if ch == mWord[k]:
                    break
                elif k == l-1:
                    f = 0
            if f==0:
                break
            else: # increment in index of mWord
                index = k+1
        if f==1:
            print(dictWord[i])

compare("bhuvanesh",5,["bhuvi","bhuvan","ravi","bhuvesh","bhuvnesh"])
