lis = ["h","t", 3, 7, 9, {}]

number = []
string = []

for i in lis:
    elem = type(i)
    if (elem == float or elem == int):
        number.append(i)

    elif (elem == str):
        string.append(i)

print ( sum (number))