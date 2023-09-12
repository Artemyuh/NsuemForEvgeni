import openpyxl


workbook = openpyxl.load_workbook('lab_pi_101.xlsx')

worksheet = workbook['Лист1']

for row in worksheet.iter_rows(values_only=True):
    print(row)