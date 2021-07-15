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
Fpath = './Aper.xlsx'
df = pd.read_excel(Fpath)
data = df.dropna()


aov = pg.rm_anova(dv='space', within=['board', 'session'], 
                  subject='user',data=df,correction=True,
             detailed=True, effsize='np2')

print(aov)

# aov = pg.rm_anova(dv='number', within=['board', 'session'], 
#                   subject='user',data=df,correction=True,
#              detailed=True, effsize='np2')

# print(aov)

###KS正态性检验
# from scipy import stats

# u = data['type'].mean() # 计算均值
# std = data['type'].std() # 计算标准差

# print(stats.kstest(data['type'], 'norm', (u, std)))

# u = data['select'].mean() # 计算均值
# std = data['select'].std() # 计算标准差

# print(stats.kstest(data['select'], 'norm', (u, std)))

# u = data['delete'].mean() # 计算均值
# std = data['delete'].std() # 计算标准差

# print(stats.kstest(data['delete'], 'norm', (u, std)))

# u = data['others'].mean() # 计算均值
# std = data['others'].std() # 计算标准差

# print(stats.kstest(data['others'], 'norm', (u, std)))