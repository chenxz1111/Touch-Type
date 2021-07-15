# import fileinput 
# import pandas as pd
# import xlrd
# import openpyxl as op
# import re
# import docx

# work_book = xlrd.open_workbook('Atask.xlsx')
# wb = op.load_workbook("Atask.xlsx")
# sh=wb["Sheet1"]

# id = 2

# for line in fileinput.input("unintentional_touches.txt"):
#     task = 1
#     datalist = line.split(' ')
#     sh.cell(id, 1, datalist[0])
#     sh.cell(id, 2, task)
#     #print(datalist[1] + datalist[5])
#     sh.cell(id, 3, float(datalist[1]) + float(datalist[5]))
#     sh.cell(id, 4, float(datalist[1]))
#     task += 1

#     sh.cell(id+16, 1, datalist[0])
#     sh.cell(id+16, 2, task)
#     sh.cell(id+16, 3, float(datalist[2]) + float(datalist[6]))
#     sh.cell(id+16, 4, float(datalist[2]))
#     task += 1

#     sh.cell(id + 32, 1, datalist[0])
#     sh.cell(id + 32, 2, task)
#     sh.cell(id + 32, 3, float(datalist[3]) + float(datalist[7]))
#     sh.cell(id+32, 4, float(datalist[3]))
#     task += 1

#     sh.cell(id + 48, 1, datalist[0])
#     sh.cell(id + 48, 2, task)
#     sh.cell(id + 48, 3, float(datalist[4]) + float(datalist[8]))
#     sh.cell(id+48, 4, float(datalist[4]))

#     id += 1
# wb.save("Atask.xlsx")

#显著性分析
import pingouin as pg
import pandas as pd
Fpath = './Atask.xlsx'
df = pd.read_excel(Fpath)
data = df.dropna()


aov = pg.rm_anova(dv='d', within=['task'], 
                  subject='user',data=df,correction=True,
             detailed=True, effsize='np2')

print(aov)

# aov = pg.rm_anova(dv='number', within=['board', 'session'], 
#                   subject='user',data=df,correction=True,
#              detailed=True, effsize='np2')

# print(aov)

##KS正态性检验
# from scipy import stats

# u = data['ut'].mean() # 计算均值
# std = data['ut'].std() # 计算标准差

# print(stats.kstest(data['ut'], 'norm', (u, std)))

# u = data['select'].mean() # 计算均值
# std = data['select'].std() # 计算标准差

# print(stats.kstest(data['select'], 'norm', (u, std)))

# u = data['delete'].mean() # 计算均值
# std = data['delete'].std() # 计算标准差

# print(stats.kstest(data['delete'], 'norm', (u, std)))

# u = data['others'].mean() # 计算均值
# std = data['others'].std() # 计算标准差

# print(stats.kstest(data['others'], 'norm', (u, std)))