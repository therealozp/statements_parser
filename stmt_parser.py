import csv
import camelot
from zipfile import ZipFile

file_name = str(input("Enter the file name: "))

tables = camelot.read_pdf(f'{file_name}.pdf', flavor='stream', pages='3-5')
# tables.export(f'{file_name}.csv', f='csv', compress=True)

csv_to_write = open(f'{file_name}.csv', 'w')

writer = csv.writer(csv_to_write)

for table in tables: 
    print("Table contents: ")
    for row in table:
        # writer.writerow(row)
        print(row)

csv_to_write.close()
# for table in tables: 
#     print(table.df)

