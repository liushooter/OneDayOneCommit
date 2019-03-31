import numpy as np
import tushare as ts
import matplotlib.pyplot as plt

data = ts.get_hist_data('000001').head(10)

# 每日收盘价
# 折线图

close_val = data.loc[:,'close']

plt.plot(close_val)
plt.show()

# 散点图
plt.scatter(data.loc[:,'close'].index, data.loc[:,'close'], s=50, c='r', alpha=.5) # s 面积
plt.show()

# 条形图
plt.bar(data.loc[:,'close'].index, data.loc[:,'close'])
plt.show()

# 饼状图
total_val = [15, 45, 23, 57, 37]
labels = ['a','b','c', 'd', 'e']
explode = [0, 0.1,0, 0.2, 0] #突出
plt.pie(x=total_val, labels=labels, explode=explode, autopct="% 0.f%%", shadow=False)

plt.show()
