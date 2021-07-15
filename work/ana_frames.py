# import fileinput 
# import pandas as pd
# import xlrd
# import openpyxl as op
# import re
# import docx

# work_book = xlrd.open_workbook('Aframes.xlsx')
# wb = op.load_workbook("Aframes.xlsx")
# sh=wb["Sheet1"]

# id = 2

# for line in fileinput.input("tmp.txt"):
#     datalist = line.split(' ')
#     sh.cell(id, 1, datalist[0])
#     sh.cell(id, 3, datalist[1])
#     sh.cell(id, 4, datalist[2])
#     sh.cell(id, 5, datalist[2])
#     id += 1
# wb.save("Aframes.xlsx")



import pingouin as pg
import pandas as pd
Fpath = './Aframes.xlsx'
df = pd.read_excel(Fpath)
data = df.dropna()


aov = pg.rm_anova(dv='accuracy', within=['frames'], 
                  subject='user',data=df,correction=True,
             detailed=True, effsize='np2')

print(aov)

# from scipy import stats
# u = data['accuracy'].mean() # 计算均值
# std = data['accuracy'].std() # 计算标准差

# print(stats.kstest(data['accuracy'], 'norm', (u, std)))