#coding:utf8
import pandas as pd
from scipy import stats


def eta_squared(aov):
    aov['eta_sq'] = 'NaN'
    aov['eta_sq'] = aov[:-1]['sum_sq']/sum(aov['sum_sq'])
    return aov


Fpath = './rm.xlsx'
df = pd.read_excel(Fpath)
data = df.dropna()
print(df)

# from statsmodels.formula.api import ols
# from statsmodels.stats.anova import anova_lm

# formula = 'speed~C(session)+C(board)+C(session):C(board)'
# anova_results = anova_lm(ols(formula,df).fit())

# anova_results = eta_squared(anova_results)

# print(anova_results)
import pandas as pd
import pingouin as pg

aov = pg.rm_anova(dv='uer', within=['session', 'board'], 
                  subject='user',data=df,correction=True,
             detailed=True, effsize='np2')

print(aov)
