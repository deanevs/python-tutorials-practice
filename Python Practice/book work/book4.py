#problem 4-1 file copying
import shutil



#new_file_path = shutil.copy('test.csv','test.csv.bak')

fd1 = open('test.csv')

# read line by line - good if files are large
for line in fd1:
    print (line.upper(),end='')

fd1.close()

fd1 = open('test.csv')
# read whole file
filelist = fd1.readlines()
print (filelist[2])
fd1.close()
"""
from pathlib import Path
p = Path('.')
for x in p.iterdir():
    if x.is_dir():
        print (x)
p.joinpath('subdir1')
p.mkdir()
"""
import pathlib
p = pathlib.Path('.')
modifiedtime = p.stat().st_mtime
print (modifiedtime)