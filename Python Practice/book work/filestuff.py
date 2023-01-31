from shutil import copyfile
import pathlib
import pandas as pd
import csv




#p = pathlib.WindowsPath('.')

#copyfile('Legend Life.csv','Legend Life BE.csv')



fieldnames = []

# with open('Legend Life.csv','r',encoding='utf-8') as fd:
#     reader = csv.DictReader(fd)
#     fieldnames = reader.fieldnames
#
#
# df = pd.read_csv('test.csv',index_col=0)
# print (df)

infile = 'Legend Life.csv'
outfile = 'Testout.csv'

fin = open(infile,'r',encoding='utf-8')
dr = csv.DictReader(fin, delimiter=',')
lst = dr.fieldnames

BE_columns = lst + ['BE_code','BE_colour','BE_size','BE_category']


with open(outfile,'w',encoding='utf8',newline='') as fou:
    dw = csv.DictWriter(fou, delimiter=',', fieldnames=BE_columns,extrasaction='ignore')
    headers = {}
    for n in dw.fieldnames:
        headers[n] = n
    dw.writerow(headers)
    for row in dr:
        dw.writerow(row)






