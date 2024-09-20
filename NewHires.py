""" 
put new hire info into the word template for me
probably needs like
turn rows into classes
duplicate a master word file
identify where to put the data
put the data, maybe on a loop?

Word
https://python-docx.readthedocs.io/en/latest/

Excel
https://pandas.pydata.org/docs/reference/index.html#api 
"""

import ReadExcel as rE
import ColClass as cC
import RowClass as rC
import CreateFile as cF
import PasswordGenerator as pG
import PutData as pD

with open('config', 'r', encoding='utf-16') as c:
    excel = c.readline()[0:-1]
    word = c.readline()

sourceExcel = excel
sourceWord = word

testobj = cC.colClass(rE.readExcel(sourceExcel), ['User ID', 'Requested for'])

rows = rC.rowClass(testobj)

details = rows
passwords = pG.passwordGenerator("randomwords.csv", len(rows))
for i in range(len(rows)):
    details[i].append(passwords[i])

newFile = cF.createFile(sourceWord, len(details))
pD.putData(newFile, details)