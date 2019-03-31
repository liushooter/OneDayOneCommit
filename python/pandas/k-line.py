# https://zhuanlan.zhihu.com/p/22692029

import tushare as ts
import matplotlib.pyplot as plt
from matplotlib import pylab
from pylab import date2num
import mpl_finance as fin
import datetime

data = ts.get_k_data('000001', '2018-01-01')


def date_to_num(dates):
    num_time = []
    for date in dates:
        date_time = datetime.datetime.strptime(date,'%Y-%m-%d')
        num_date = date2num(date_time)
        num_time.append(num_date)

    return num_time


mat_data = data.as_matrix()
num_time =date_to_num(mat_data[:,0])
mat_data[:,0]= num_time


fig, ax = plt.subplots(figsize=(60,20))
fig.subplots_adjust(bottom=.5)

fin.candlestick_ohlc(ax, mat_data, colorup='g',colordown='r', alpha=1.0)

plt.xticks(rotation=30)

plt.title('000001.SH')
plt.xlabel('Date')
plt.ylabel('Price')
ax.xaxis_date()

plt.show()