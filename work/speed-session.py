import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
data = pd.read_csv(u'test.csv') #读取存放的文件
plt.figure(figsize=(5, 5))
sns.regplot(x="session",y="speed",col="board",data=data)
plt.show()
#plt.savefig(u'test.pdf')