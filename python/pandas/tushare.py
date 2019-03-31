import tushare as ts
import pandas as pd

print(ts.__version__)
# http://tushare.org/


# 股票历史行情数据
ts.get_hist_data('000001')


# 复权数据
ts.get_h_data('000001')

ts.get_h_data('002337') #前复权
ts.get_h_data('002337', autype='hfq') #后复权
ts.get_h_data('002337', autype=None) #不复权
ts.get_h_data('002337', start='2015-01-01', end='2015-03-16') #两个日期之间的前复权数据

ts.get_h_data('399106', index=True) #深圳综合指数

# 限售股解禁
ts.xsg_data()
ts.xsg_data(year=2018,month=6)


# 行业分类 来自新浪财经
list = ts.get_industry_classified()
list1 = list.loc[list['c_name']=='综合行业']
list2 = list.loc[list['c_name']=='交通运输']

# 热点概念
ts.get_concept_classified()


# 上市公司的财务报表数据
# 财务指标

# 盈利能力
ts.get_profit_data(2018,4) # 18年4季度

# 偿债能力
ts.get_debtpaying_data(2018,4) # 18年4季度

# 宏观经济

# 存款利率
ts.get_deposit_rate()

# 贷款利率
ts.get_loan_rate()

# 存款准备金率
ts.get_rrr()

# 货币供应量(年底余额)
ts.get_money_supply_bal()


# 国内货币供应量
df = ts.get_money_supply()
# df.to_csv('money_supply.csv')
df.to_excel('money_supply.xlsx') # pip install openpyxl
pd.read_excel('money_supply.xlsx') # pip install xlrd


# 国内生产总值(年度)
ts.get_gdp_year()

# 国内生产总值(季度)
ts.get_gdp_quarter()

# 三大需求对GDP贡献
ts.get_gdp_for()

# 三大产业对GDP拉动
ts.get_gdp_pull()

# 三大产业贡献率
ts.get_gdp_contrib()

# 居民消费价格指数
ts.get_cpi()

# 工业品出厂价格指数
ts.get_ppi()