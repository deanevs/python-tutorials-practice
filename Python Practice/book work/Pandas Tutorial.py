import numpy as np
import pandas as pd

# A structured array
my_array = np.ones(3, dtype=([('foo', int), ('bar', float)]))
print(my_array['foo'])

# A record array
my_array2 = my_array.view(np.recarray)
print(my_array2.foo)
print ('*******************')

data = np.array([['', 'Col1', 'Col2','Col3'],
                 ['Row1', 1, 2,3],
                 ['Row2', 13, 14,15]])


print (pd.DataFrame(data))
print ('*******************')
df = pd.DataFrame(data)

# Use the `shape` property
print(df.shape)

# Or use the `len()` function with the `index` property
print(len(df.index))
print ('*******************')

print (list(df.columns.values))
print ('*******************')

print (df)
print ('*******************')

print (df.iloc(2))


