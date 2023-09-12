import openpyxl
import pandas as pd

workbook = openpyxl.load_workbook('lab_pi_101.xlsx')
worksheet = workbook['Лист1']

data = []

for row in worksheet.iter_rows(values_only=True):
    data.append(row)

df = pd.DataFrame(data)
df.columns = df.iloc[0]
df = df.iloc[1:]

pi101_row = df[df['Группа']=='ПИ101']


unique_student_count = pi101_row['Личный номер студента'].unique()

unique_student_count_str = [str(number) for number in unique_student_count]

unique_student_numbers_str = ', '.join(unique_student_count_str)

print (unique_student_numbers_str)


#посмотреть как доделать через запятую 