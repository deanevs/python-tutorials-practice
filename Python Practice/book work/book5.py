
"""
import pandas as pd
data = [1,2,3,4]
data_pd = pd.Series(data)
print (data_pd)


import numpy as np


print (data_pd.dtype)

data_pd2 = pd.Series(data,dtype=np.float64)
print (data_pd2)

print (2* data_pd)

d1 = {'cola':[1,2,3,4],'colb':[5,6,7,8],'colc':[9,10,11,12]}
df1 = pd.DataFrame(d1)
print (df1)
print ()
print ("ColB, row 2 = ",df1['colb'][2])
print ()
print (df1.irow(2))
"""
import pandas as pd
csv_data = pd.read_csv('test.csv')
print (csv_data)

