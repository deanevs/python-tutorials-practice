from BrandElevate_old import mylib

import pandas as pd

df2 = pd.DataFrame({'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]})
print (df2)
mylib.print_line()


s_len = len(df2['AAA'])
#df2['DDD'] = pd.Series(np.random.randn(s_len), index=df2.index)
df2['DDD'] = pd.Series('empty', index=df2.index)
print (df2)
mylib.print_line()

df2.set_value(0,'DDD',3)
print (df2)
mylib.print_line('Y')

for index,row in df2.iterrows():
    #print (row['BBB'])
    df2.set_value(index,'DDD',5)

print (df2)
mylib.print_line()

df2['EEE'] = 9

print (df2)
mylib.print_line()

print (df2.columns)
mylib.print_line('Y')
df22 = df2.duplicated
print (df22)

df2.insert(loc=3,column='FFF',value=99)
print(df2)

df2.to_csv('testfile.csv',index=False)