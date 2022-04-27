str = "the quick brown fox"

def translator(str):
    strList = str.split()
    for i in range(len(strList)):
        strElem = list(strList[i])
        print(strElem)
        newStrElem = []
        for j in range(1, len(strElem)):
            newStrElem.append(strElem[j])
        newStrElem.append(strElem[0])
        newStrElem.append('a')
        newStrElem.append('y')

        strList[i] = ""
        for j in newStrElem:
            strList[i] += j

    strList[0] = strList[0].capitalize()

    str = ' '.join(strList)

    return str

print(translator(str))