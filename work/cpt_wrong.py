import pandas as pd
import xlrd
import openpyxl as op


path = 'data.xlsx'
data = pd.DataFrame(pd.read_excel(path))


work_book = xlrd.open_workbook('time.xlsx')
wb = op.load_workbook("time.xlsx")
sh=wb["Sheet1"]

for i in range(225):
    sh.cell(2 + (i % 15) * 15 + int(i / 15), 10, data['wrong'][i])
    print(data['wrong'][i])
wb.save("time.xlsx")
