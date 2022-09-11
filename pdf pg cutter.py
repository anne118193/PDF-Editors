import os
import numpy as np
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

folderPath = '/Users/Anne/Downloads/' #change this (put all the files you want to merge into 1 folder)
file_dir = os.listdir(folderPath)

#keep a few pages
pages_to_keep = np.append([183, 185], list(np.linspace(187, 203, num=(203-187+1), dtype=int))) # page numbering starts from 0
pages_to_keep = np.append(pages_to_keep, list(np.linspace(204, 225, num=(225-204+1), dtype=int)))
pages_to_keep = np.append(pages_to_keep, list(np.linspace(227, 289, num=(289-227+1), dtype=int)))
infile = PdfReader(folderPath + 'Yoni Kahn, Adam Anderson - Conquering the physics GRE (2018, Cambridge University Press) - libgen.lc.pdf', 'rb')
output = PdfWriter()

print('Included Pages:')
print(pages_to_keep)
print('# pages:', len(pages_to_keep))

for i in pages_to_keep:
    p = infile.pages[int(i)]
    output.add_page(p)

with open(folderPath + 'newfile.pdf', 'wb') as f:
    output.write(f)


##delete a few pages
#pages_to_delete = [3, 4, 5] # page numbering starts from 0
#infile = PdfReader('source.pdf', 'rb')
#output = PdfWriter()

#for i in range(len(infile.pages) ):
#    if i not in pages_to_delete:
#        p = infile.get_page(i)
#        output.add_page(p)

#with open('newfile.pdf', 'wb') as f:
#    output.write(f)