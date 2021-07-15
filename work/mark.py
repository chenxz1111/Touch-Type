import pandas as pd
import numpy as np
import scipy
 
# 自定义函数
def level_avg(data, x_name, y_name):
    df = data.groupby([x_name]).agg(['mean'])
    df = df[y_name]
    dict_ = dict(df["mean"])
    return dict_
 
def SST(Y):
    sst = sum(np.power(Y - np.mean(Y), 2))
    return sst
 
def SSA(data, x_name, y_name):
    total_avg = np.mean(data[y_name])
    df = data.groupby([x_name]).agg(['mean', 'count'])
    df = df[y_name]
    ssa = sum(df["count"]*(np.power(df["mean"] - total_avg, 2)))
    return ssa
 
def SSE(data, y_name):
    
    data_ = data.copy()
    total_avg = np.mean(data[y_name])
    x_var = set(list(data.columns))-set([y_name])
   
    cnt=1
    for i in x_var:
        dict_ = level_avg(data, i, y_name)
        var_name = 'v_avg_{}'.format(cnt)
        data_[var_name] = data_[i].map(lambda x: dict_[x])
        cnt += 1
   
    sse = sum(np.power(data_[y_name] - data_["v_avg_1"] - data_["v_avg_2"] + total_avg, 2))
    return sse
 
def two_way_anova(data, row_name, col_name, y_name, alpha=0.05):
    """无重复双因素方差分析"""
    print(data)
    n = len(data)
    print(n)                       # 总观测值数
    k = len(data[row_name].unique())
    print(k)    # 行变量水平个数
    r = len(data[col_name].unique())
    print(r)    # 列变量水平个数
    
    sst = SST(data[y_name])             # 总平方和
    ssr = SSA(data, row_name, y_name)   # 行变量平方和
    ssc = SSA(data, col_name, y_name)   # 列变量平方和
    sse = SSE(data, y_name)             # 误差平方和
    
    msr = ssr / (k-1)
    msc = ssc / (r-1)
    mse = sse / ((k-1)*(r-1))
    
    Fr = msr / mse  # 行变量 统计量F
    Fc = msc / mse  # 列变量 统计量F
    pfr = scipy.stats.f.sf(Fr, k-1, (k-1)*(r-1))  # 行变量 统计量F的P值
    pfc = scipy.stats.f.sf(Fc, r-1, (k-1)*(r-1))  # 列变量 统计量F的P值
    
    Far = scipy.stats.f.isf(alpha, dfn=k-1, dfd=(k-1)*(r-1))   #行 F临界值
    Fac = scipy.stats.f.isf(alpha, dfn=r-1, dfd=(k-1)*(r-1))   #列 F临界值
    
    r_square = (ssr+ssc) / sst      # 联合效应/总效应
    
    table = pd.DataFrame({'差异源':[row_name, col_name, '误差', '总计'],
                          '平方和SS':[ssr, ssc, sse, sst],
                          '自由度df':[k-1, r-1, (k-1)*(r-1), k*r-1],
                          '均方MS':[msr, msc, mse, '_'],
                          'F值':[Fr, Fc, '_', '_'],
                          'P值':[pfr, pfc, '_', '_'],
                          'F临界值':[Far, Fac, '_', '_'],
                          'R^2':[r_square, '_', '_', '_']})
    
    return table
# 导入数据
df = pd.read_excel("mark.xlsx", sheet_name='Sheet1')
 
# 输出方差分析结果
two_way_anova(df, 'board', 'session', 'speed', alpha=0.05)