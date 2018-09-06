NumbersToLettersMap = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i',
                       '10': 'j', '11': 'k', '12': 'l', '13': 'm','14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r',
                       '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'}

keys = NumbersToLettersMap.keys()

def NumberOfUniqueStrings(InputNumberString):
    number = NumberOfSubStrings(InputNumberString, len(InputNumberString))
    return number

def NumberOfSubStrings(InputString, Length):
    if InputString == '':
        return 1
    elif InputString[0] == '0':
        return 0

    FirstTwoLettersOfString = InputString[0:2]
    if FirstTwoLettersOfString in keys and len(InputString) > 1:
        return NumberOfUniqueStrings(InputString[2:]) + NumberOfUniqueStrings(InputString[1:])

    return NumberOfUniqueStrings(InputString[1:])

string = '1111'
print(NumberOfUniqueStrings(string))
