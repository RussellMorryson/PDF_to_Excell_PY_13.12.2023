# Script to export tables from PDF files
# Requirements:
# Pandas (cmd --> pip install pandas)
# Java   (https://www.java.com/en/download/)
# Tabula (cmd --> pip install tabula-py)
# openpyxl (cmd --> pip install openpyxl) to export to Excel from pandas dataframe

import tabula
#import pandas

def convert_pdf_to_excell():
    pdf_in = "File.pdf"
    
    # Блок кода для линейной конвертации pdf в xlsx
    #PDF = tabula.read_pdf_with_template(input_path = pdf_in)
    #PDF = pandas.DataFrame(data = PDF)
    #pdf_out_xlsx = "From_PDF.xlsx"
    #PDF.to_excel(excel_writer = pdf_out_xlsx, index = False)
    
    # Блок кода для линейной конвертации pdf в csv
    pdf_out_csv = "From_PDF.csv" 
    tabula.convert_into(input_path = pdf_in, output_path = pdf_out_csv, pages = 'all')

    with (open('From_PDF.csv', 'r') as csv_in,
          open('Result_convertation.csv', 'a') as csv_out):

    for line in csv_in:
        word_line = line
        word_line = word_line.replace('\"', ';') #Используется для разделения строки на столбцы
        csv_out.write(word_line)    
    print("Done")

if __name__ == '__main__':
    convert_pdf_to_excell()
