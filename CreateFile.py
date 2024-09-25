#create a word .docx file to make namecards from
#in:  string filename, int cards
#out: 

import shutil
import math
from docxcompose.composer import Composer
from docx import Document as Document_compose
import os

# https://stackoverflow.com/questions/24872527/combine-word-document-using-python-docx
#Filename_master is the name of the file you want to merge all the document into
#filesList is a list containing all the filename of the docx file to be merged
def combine_all_docx(filenameMaster,filesList, outputFile):
    number_of_sections=len(filesList)
    master = Document_compose(filenameMaster)
    composer = Composer(master)
    for i in range(0, number_of_sections):
        doc_temp = Document_compose("./temp/" + filesList[i])
        composer.append(doc_temp)
    composer.save(outputFile)
#For Example
#filenameMaster="file1.docx"
#filesList=["file2.docx","file3.docx","file4.docx",file5.docx"]
#Calling the function
#combine_all_docx(filenameMaster,filesList)
#This function will combine all the document in the array filesList into the file1.docx and save the merged document into combined_file.docx

#properties of the page are based on the namecards we use
#5 rows, 2 columns
#top 0.5", bottom 0.42", left 0.84", right 0.31"
#portrait 8.5" x 11"

# table properties
# row height 2", col width 3.5"
# center vertical alignment width 3.5"

#in:  string original template file
#out: string master file name

def createFile(fileName, cards):
    numPages = math.ceil(cards / 10) - 1
    tempName = "tempworddoc"
    dirName = "temp"
    if not os.path.exists(dirName):
        os.makedirs(dirName)

    for i in range(numPages):
        shutil.copy2(fileName, "./" + dirName + "/" + tempName + str(i) + ".docx")

    combine_all_docx(fileName, os.listdir("./" + dirName), "new" + fileName)

    shutil.rmtree("./temp/")

    return ("new" + fileName)