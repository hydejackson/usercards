#write data to Word file
#in:  string filename (to edit), list details[[name, id, password]...]
#out: 

import docx as dx

def putData(filename, details: list):
    document = dx.Document(filename)
    docTable = document.tables
    counterVar = 0
    tempTextList = []

    print(details)
    print(len(docTable[0].rows))
    print(len(docTable[0].columns))

    for d in range(len(details)):
        tempText = \
        "Name: " + details[d][0] + "\n" + \
        "Username: " + details[d][1] + "\n" + \
        "Password: " + details[d][2]

        tempTextList.append(tempText)

    for i in range(len(docTable[counterVar//10].rows)):
        for j in range(len(docTable[counterVar//10].columns)):
            docTable[counterVar//10].cell(i, j).text = tempTextList[counterVar]
            counterVar = counterVar + 1
            if counterVar > len(details):
                break
            print(counterVar)
        counterVar = counterVar + 1
        if counterVar > len(details):
            break
        print(counterVar)
        
    document.save(filename)
