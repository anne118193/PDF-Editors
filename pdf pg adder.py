import os
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfFileMerger


folderPath = '/Users/Anne/Downloads/' #change this (put all the files you want to merge into 1 folder)
file_dir = os.listdir(folderPath)

infile1 = PdfReader(folderPath + 'new1.pdf', 'rb') #origional pdf
infile2 = PdfReader(folderPath + 'pg44.pdf') #page that you want to insert
output = PdfWriter()

merger = PdfFileMerger()

pgNum = 42 #the page you want the inserted page to come after

merger.append(infile1)
merger.merge(pgNum, infile2)

#change this if you want to, im lazy so i probs wont
merger.write('/Users/Anne/Downloads/new.pdf') #name of the new mergered file 
merger.close()
