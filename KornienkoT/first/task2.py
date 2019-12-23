sentence = input()
print (sentence)

CapLetters = sentence.split(" ")
print (CapLetters)

for word in CapLetters:
    for symb in word:
        if (symb.isupper()):
            print (word)

#Користувая вводить текст, вивести усі слова цього тексту, що містять велику букву, у вигляді списку