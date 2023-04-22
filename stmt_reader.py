import pandas as pd

file_name = str(input("Enter the file name: "))
df = pd.read_csv(f'secrets/{file_name}.csv')
print(df)