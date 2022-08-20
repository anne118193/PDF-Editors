import os
from pathlib import Path
from PyPDF2 import PdfFileMerger, PdfFileReader 

folderPath = '/Users/Anne/Downloads/New Folder/' #change this (put all the files you want to merge into 1 folder)
file_dir = os.listdir(folderPath)

merger = PdfFileMerger()

for item in file_dir:
    if item.endswith('pdf'):
        pdfFile = folderPath + item
        merger.append(open(pdfFile, 'rb'))

merger.write('/Users/Anne/Downloads/mergedPDF.pdf') #change this if you want to, im lazy so i probs wont
merger.close()


