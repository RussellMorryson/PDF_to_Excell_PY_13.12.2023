# Script to export tables from PDF files
# Requirements:
# Pandas (cmd --> pip install pandas)
# Java   (https://www.java.com/en/download/)
# Tabula (cmd --> pip install tabula-py)
# openpyxl (cmd --> pip install openpyxl) to export to Excel from pandas dataframe

import tabula
#import pandas

pdf_in = "file1.pdf"
PDF = tabula.read_pdf(pdf_in, pages='all', multiple_tables=True)
with open('new_text_file.txt', 'a') as f:
    for line in PDF:        
        f.write(str(line))
#PDF = pandas.DataFrame(PDF)
#pdf_out_xlsx = "From_PDF.xlsx"
#pdf_out_csv = "From_PDF.csv"

#PDF.to_excel(pdf_out_xlsx,index=False) 

#tabula.convert_into (input_PDF, pdf_out_csv, pages='all',multiple_tables=True)
print("Done")