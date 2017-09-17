import keyword
stringsToCheck = []

def keywordSearch():
    for keyIn in stringsToCheck:
        if keyword.iskeyword(keyIn):
            print(keyIn + ' is a python keyword')
        else:
            print(keyIn + ' is not a python keyword')

if __name__ == '__main__':

    addString = str(raw_input('Enter string to analyze: '))

    stringsToCheck.append(addString)

    keywordSearch()
