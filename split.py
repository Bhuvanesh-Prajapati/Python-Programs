# split on set of strings if the word starts with 'B'
st = "Bhuvi Bhuvanesh Bhuvan bombay bangalore Mumbai Delhi Hyderabd Chennai"
for word in st.split():
    if word[0].lower() == 'b':
        print(word)
