# CREATE A PIG WORD IF THE FIRST LETTER OF A WORD IS A VOWEL
def pig_latin(word):
    f_letter = word[0]
    if f_letter in 'aeiou':
        pig_word = word +'ay'
    else:
        pig_word = word[1:] + f_letter +'ay'
    print(pig_word)

pig_latin(input())
