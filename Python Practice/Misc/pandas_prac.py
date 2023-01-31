import pandas as pd

df = pd.read_csv('Automobile_data.csv')

print(df.head(5))
print(df.tail(5))

df.replace(['?'])