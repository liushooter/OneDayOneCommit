import tushare as ts

# 实时票房
ts.realtime_boxoffice()


# 每日票房
ts.day_boxoffice() #取上一日的数据
ts.day_boxoffice('2010-01-01')  #取指定日期的数据

# 月度票房
ts.month_boxoffice() #取上一月票房数据
ts.month_boxoffice('2019-02') #此月数据


# 影院日度票房
ts.day_cinema() #取上一日全国影院票房排行数据
df = ts.day_cinema('2019-02-05') # 指定日期的数据 2019年春节
df.to_excel('movie.xlsx') # pip install openpyxl