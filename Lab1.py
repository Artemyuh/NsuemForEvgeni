import openpyxl
import Pandas

workbook = openpyxl.load_workbook('lab_pi_101.xlsx')

worksheet = workbook.active ('Лист1') 

for row in worksheet.iter_rows(values_only=True):
    print(row)