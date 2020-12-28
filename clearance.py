import PyPDF2
import tabula
import pandas as pd

file = '/Users/siddhantagarwal/Desktop/clearance1.pdf'
pdfFileObj = open(file,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#print(pdfReader.numPages)
pageobj = pdfReader.getPage(0)

text = [pdfReader.getPage(0).extractText()]
text = text[0].split('\n')
pg = []
for i in text:
    if i.strip():
        pg.append(i)
        
print(pg)
'''
########### DATE ####################
months = ['january','february','march','april','may','june','july','august', 'september','october','november','december']
brackets = ['(',')']
date = []
i = 0
while (i <= len(pg)):
    if pg[i] in brackets:
        date.append(pg[i])
        flag = True
        while flag==True:
            i = i+1
            if not(pg[i] in brackets):
                date.append(pg[i])
            else:
                date.append(pg[i])
                flag = False
    

print("DATE: ",date)
####################################################
'''
############# TITLE ####################
index = 0
number_dict = {}
for i in range(len(pg)):
    if pg[i] == 'Press Release No. 1':
        index = i
        
del pg[0:index+1]
print(index)
print(pg)

# ONCE YOU GET COMPANY LIST, CHECK FOR THE NAME OF THE COMPANY 
# IN THE LIST PG
# TITLE IS THE JUST "MARKET WIDE POSITION LIMIT IN <COMPANY NAME>

###########################################


    