"""
Put new hire info into the word template.
Steps:
1. Read data from Excel.
2. Generate passwords.
3. Create a new Word file.
4. Insert data into the Word file.

References:
Word: https://python-docx.readthedocs.io/en/latest/
Excel: https://pandas.pydata.org/docs/reference/index.html#api
"""

import os
import argparse
import CreateFile as cF
import PasswordGenerator as pG
import PutData as pD
import ReadExcel as rE
import ColClass as cC
import RowClass as rC

def main(excel, word=None):
    sourceExcel = excel
    if word is None:
        sourceWord = os.path.join(os.path.dirname(__file__), 'templates', 'cards.docx')
    else:
        sourceWord = word
    sourceRandomWords = os.path.join(os.path.dirname(__file__), 'templates', 'randomwords.csv')

    # Read data from Excel and extract relevant columns
    testobj = cC.colClass(rE.readExcel(sourceExcel), ['User ID', 'Requested for'])
    rows = rC.rowClass(testobj)

    # Generate passwords and append to details
    details = rows
    passwords = pG.passwordGenerator(sourceRandomWords, len(rows))
    for i in range(len(rows)):
        details[i].append(passwords[i])

    # Create a new Word file and insert data
    newFile = cF.createFile(sourceWord, len(details))
    pD.putData(newFile, details)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process Excel and Word files.')
    parser.add_argument('excel', type=str, help='Path to the Excel file')
    parser.add_argument('--word', type=str, help='Path to the Word file (default: templates/cards.docx)')
    args = parser.parse_args()
    
    main(args.excel, args.word)
