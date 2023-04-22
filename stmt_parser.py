import csv
import camelot
# import pandas as pd

file_name = str(input("Enter the file name: "))
output_name = str(input('Enter the output file name: '))
page_range = str(input("Enter the page range in number-number format: "))

tables = camelot.read_pdf(f'secrets/{file_name}.pdf', flavor='stream', pages=page_range)
csv_to_write = open(f'secrets/{output_name}.csv', 'w', newline='')

writer = csv.writer(csv_to_write)

for index in range(len(tables)):
    table = tables[index]
    # if index == 0: 
    tabledf = table.df
    # set new header right away
    new_header = ['Date', 'Description', 'Amount']
    tabledf.columns = new_header
    
    # create the drop condition for rows
    dropCondition = tabledf[(tabledf['Date'] == '') | (tabledf['Date'].str.contains('[a-zA-Z]'))].index
    tabledf.drop(dropCondition, inplace=True)
    print(tabledf.columns)


    # writes everything to csv file, header True if index == 0 else false
    if index == 0: 
        tabledf.to_csv(csv_to_write, index=False, header=True)
    else: 
        tabledf.to_csv(csv_to_write, index=False, header=False)
    # print(tabledf)

csv_to_write.close()
# for table in tables: 
#     print(table.df)

