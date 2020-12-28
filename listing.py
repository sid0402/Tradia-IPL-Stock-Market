import PyPDF2
import tabula
import pandas as pd

file = '/Users/siddhantagarwal/Desktop/example2.pdf'
pdfFileObj = open(file,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#print(pdfReader.numPages)
pageobj = pdfReader.getPage(0)
#print(pageobj.extractText()) 

months = ['january','february','march','april','may','june','july','august', 'september','october','november','december']
months = [i.capitalize() for i in months]
numbers = []
for i in range(1,32):
    numbers.append(i)

pages = []
for page in range(pdfReader.numPages):
    pages.append(pdfReader.getPage(page).extractText())
   
pg = pages[0].split('\n')
print("PG")
print(pg)
text =[]
for i in pg:
    if i.strip():
        text.append(i)
print(text)
'''
for i in pg:
    if i.isspace() == True or i.isalpha() == True:
        pg.remove(i)
        '''

dates = []
for i in pg:
    for j in months:
        if j in i:
            date = i
            #print(date)
            dates.append(date)
            '''
print(pg)
print(len(pg))
print(dates)
'''
date = dates[0]      
print("DATE: ",date)
##### EXTRACTING TABLE ############

tables = tabula.read_pdf(file,multiple_tables = True)
print("NUMBER OF TABLES: ",len(tables))
writer = pd.ExcelWriter('listings.xlsx', engine='xlsxwriter')
for i in range(len(tables)):
    df = pd.DataFrame(tables[i])
    number = "Sheet"+str(i+1)
    df.to_excel(writer,sheet_name=number)
writer.save()
#print(df)
#print(pd.DataFrame(tables[1]))
#print(len(tables))
#print(tables)

#### EXTRA NONSENSE ##########
'''
def splitSentence(pages):
    sentences = []
    sentence = []
    ls1 = []
    for i in pages.split(' '):
        i.replace('\n',' ')
        ls1.append(i.replace('\n',' '))
    #print(ls1)
    for j in ls1:
        if not(' ' in j):
            sentence.append(j)
        else:
            sentence.append(j.split(' ')[0])
            sentences.append(sentence)
            sentence = []
            sentence.append(j.split(' ')[1])
    return sentences
splitSentence(pages)


AllSentences = []
for i in range(pdfReader.numPages):
    AllSentences.append(splitSentence(pages[i]))
#print(AllSentences[0:4])
AllSentences = AllSentences[0]
 
def filtered(sentences):
    flag = False
    for i in sentences:
        if i.isdigit() == True:
            flag = True
    return flag

for sentence in AllSentences:
    if filtered(sentence) == False:
        AllSentences.remove(sentence)
        '''