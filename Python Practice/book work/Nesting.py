import pandas as pd
import pathlib
import pathlib

#dean = pathlib.WindowsPath("C:\Users\Dean\Dropbox\Brand Elevate\6 Website\7 UTF8 Supplier Data")


path = ("C:\\Users\\Dean\\Dropbox\\Brand Elevate\\6 Website\\7 UTF8 Supplier Data\\")

p = pathlib.Path(path)

print (p)
for child in p.iterdir():
    print (child)
# setup display options for debugging
desired_width = 320
pd.set_option('display.width', desired_width)
pd.options.display.max_colwidth = 200

p = pathlib.Path("C:\Users\Dean\Dropbox\Brand Elevate\6 Website\7 UTF8 Supplier Data")
for child in p.iterdir():


df = pd.read_csv('BIC - BIC.csv')


colset = set()

#print (df.loc[:,'colours_available_supplier'])
for x in df.loc[:,'colours_available_supplier']:

    if (type(x) == float):
        continue
    tmp = x.split("|")
    for y in tmp:
        colset.add(y.strip())

for l in colset:
    print (l)
