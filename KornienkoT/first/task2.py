sentence = input()
print (sentence)

CapLetters = sentence.split(" ")
print (CapLetters)

for word in CapLetters:
    for symb in word:
        if (symb.isupper()):
            print (word)