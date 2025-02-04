import redis

# 连接到 Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# 定义 Set 的名称
set_name = 'my_set'

# 要添加到 Set 的数据
data = ['value1', 'value2', 'value3']

# 向 Set 中添加数据
r.sadd(set_name, *data)

# 打印 Set 中的所有值
print(r.smembers(set_name))

# 定义 Sorted Set 的名称
sorted_set_name = 'my_sorted_set'

# 要添加到 Sorted Set 的数据及其分数
sorted_data = {
    'value1': 1.0,
    'value2': 2.0,
    'value3': 3.0
}

# 向 Sorted Set 中添加数据
for value, score in sorted_data.items():
    r.zadd(sorted_set_name, {value: score})

# 打印 Sorted Set 中的所有值及其分数
print(r.zrange(sorted_set_name, 0, -1, withscores=True))