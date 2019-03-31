import pandas as pd

trade_volumn = [1099, 500, 2345, 1304]
stock = ["平安银行","万科","上汽","茅台"]
res = pd.Series(trade_volumn, index=stock)

print(res.index)
print(res.index[0])
print(res['万科'])
print(res[['万科','茅台']])
print(res.head(2))
print(res.tail(1))
print(res[res>1500])

res2 = res.reindex(['平安保险', '万科', '上汽', '茅台'])
print(res2)

print(res2[res2.isnull()])
print(res2[res2.notnull()])

res3 = res2.drop(['茅台'])
print(res3)


###########DataFrame###########

a = pd.Series([500,455,124], index=['主营业务利润', '非主营业务利润','其他收入'])
b = pd.Series([3567,1245,789], index=['主营业务利润', '非主营业务利润','其他收入'])
c = pd.Series([908,235,98], index=['主营业务利润', '非主营业务利润','其他收入'])

list = {"公司a":a, "公司b":b, "公司c":c}
df = pd.DataFrame(list)

df.iloc[0,0]
df.iloc[0,2]
print(df.iloc[0,2:])
print(df.iloc[0:,2])

print(df.loc['主营业务利润', '公司a'])
print(df.loc['其他收入'])
print(df.loc['其他收入':])

# 行/列转换
df2 = df.T
df2

management = [234, 1230, 457]
df2.loc[: ,'管理费用'] = management

d = [580, 436, 214, 123]
df2.loc['公司d',:] = d

print(df2)

print(df2.sort_values(by=['主营业务利润'], ascending=True))

# 数据透视表
df2.pivot_table('today', index='code', column='key', aggfunc='mean').fillna(0) #aggregation
# fillna 填充Nona为0