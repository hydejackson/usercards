import shutil
import math
from docxcompose.composer import Composer
from docx import Document as Document_compose
import os
import re
import stat
from datetime import datetime

# https://stackoverflow.com/questions/24872527/combine-word-document-using-python-docx
# Filename_master is the name of the file you want to merge all the documents into
# filesList is a list containing all the filenames of the docx files to be merged
def combine_all_docx(filenameMaster, filesList, outputFile):
    number_of_sections = len(filesList)
    master = Document_compose(filenameMaster)
    composer = Composer(master)
    for i in range(number_of_sections):
        doc_temp = Document_compose(os.path.join(os.path.dirname(__file__), "temp", filesList[i]))
        composer.append(doc_temp)
    composer.save(outputFile)

# For Example
# filenameMaster = "file1.docx"
# filesList = ["file2.docx", "file3.docx", "file4.docx", "file5.docx"]
# Calling the function
# combine_all_docx(filenameMaster, filesList, "combined_file.docx")
# This function will combine all the documents in the array filesList into the file1.docx and save the merged document into combined_file.docx

# Properties of the page are based on the namecards we use
# 5 rows, 2 columns
# top 0.5", bottom 0.42", left 0.84", right 0.31"
# portrait 8.5" x 11"

# Table properties
# row height 2", col width 3.5"
# center vertical alignment width 3.5"

# Create a Word .docx file to make namecards from
# in:  string filename, int cards
# out: string master file name
def createFile(fileName, cards):
    fileName = re.split(r'[\\/]', fileName)[-1]
    numPages = math.ceil(cards / 10) - 1
    tempName = "tempworddoc"
    dirName = "temp"
    outputDir = "output"
    masterTempDoc = os.path.join(os.path.dirname(__file__), "templates", tempName + ".docx")
    tempFiles = []

    # Create temporary and output directories if they don't exist
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    # Create temporary files
    for i in range(numPages):
        tempFilePath = os.path.join(os.path.dirname(__file__), dirName, tempName + str(i) + ".docx")
        tempFiles.append(tempFilePath)
        shutil.copy2(masterTempDoc, tempFilePath)

    # Combine temporary files into the final output file
    today_date = datetime.now().strftime("%m%d%y")
    outputFilePath = os.path.join(os.path.dirname(__file__), outputDir, today_date + "_" + fileName)
    combine_all_docx(masterTempDoc, tempFiles, outputFilePath)

    # Clean up temporary files
    shutil.rmtree(os.path.join(os.path.dirname(__file__), dirName), onerror=lambda func, path, _: (os.chmod(path, stat.S_IWRITE), func(path)))

    return outputFilePath