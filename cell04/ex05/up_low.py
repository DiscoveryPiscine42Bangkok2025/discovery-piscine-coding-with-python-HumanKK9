word=input("Give me a word: ")
for x in word:
    if x.isupper():
        print(x.lower(),end="")
    else:
        print(x.upper(),end="")