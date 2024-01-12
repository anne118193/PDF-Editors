import os
from pathlib import Path
from PyPDF2 import PdfMerger, PdfFileReader 

folderPath = '/Users/anne1/Downloads/txtbook/' #change this (put all the files you want to merge into 1 folder)
file_dir = os.listdir(folderPath)
file_dir = sorted(file_dir) #sort files alphabetically

merger = PdfMerger()

for item in file_dir:
    if item.endswith('pdf'):    #if the file is a pdf
        pdfFile = folderPath + item       #gets the file (basically)
        merger.append(open(pdfFile, 'rb'))  #adds the file to the "back"

#change this if you want to, im lazy so i probs wont
merger.write('/Users/anne1/Downloads/mergedPDF.pdf') #name of the new mergered file 
merger.close()


