#write data to Word file
#in:  string filename (to edit), list details[[name, id, password],...]
#out: null

import docx as dx

#filename is the word doc we're putting text in
#details is just a list of lists of strings containing name and id
def putData(filename, details: list):
    #read in word doc
    document = dx.Document(filename)
    #list of tables in doc (basically the pages for our case)
    docTable = document.tables
    counterVar = 0
    tempTextList = []

    #make list of string of text to add to each cell
    for d in range(len(details)):
        tempText = \
        "Name: " + details[d][0] + "\n\n" + \
        "Username: " + details[d][1] + "\n\n" + \
        "Password: " + details[d][2]

        tempTextList.append(tempText)

    #idea for this is to cycle through each row/column coord and change text to an entry in the tempTextList
    #I'm using the counterVar to keep track but it doesn't seem to be working well
    for d in docTable:
        for i in range(len(d.rows)):
            for j in range(len(d.columns)):
                d.cell(i, j).text = tempTextList[counterVar]
                if counterVar > len(details) - 1:
                    break
                else:
                    counterVar = counterVar + 1
            if counterVar > len(details) - 1:
                break
        
    document.save(filename)
