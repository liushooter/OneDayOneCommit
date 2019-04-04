#coding:utf-8

import random
import pygal
import json
from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world.maps import World
# 颜色相关
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

class Die:
    """
    一个骰子类
    """
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return random.randint(1, self.num_sides)


# 模拟掷骰子
die = Die()
result_list = []
# 掷1000次
for roll_num in range(1000):
    result = die.roll()
    result_list.append(result)

frequencies = []
# 范围1~6，统计每个数字出现的次数
for value in range(1, die.num_sides + 1):
    frequency = result_list.count(value)
    frequencies.append(frequency)

# 条形图
hist = pygal.Bar()
hist.title = 'Results of rolling one D6 1000 times'
# x轴坐标
hist.x_labels = [1, 2, 3, 4, 5, 6]
# x、y轴的描述
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
# 添加数据， 第一个参数是数据的标题
hist.add('D6', frequencies)
# 保存到本地，格式必须是svg
hist.render_to_file('die_visual.svg')





# 同时掷两个骰子

die_1 = Die()
die_2 = Die()

result_list = []
for roll_num in range(5000):
    # 两个骰子的点数和
    result = die_1.roll() + die_2.roll()
    result_list.append(result)

frequencies = []
# 能掷出的最大数
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result + 1):
    frequency = result_list.count(value)
    frequencies.append(frequency)

# 可视化
hist = pygal.Bar()
hist.title = 'Results of rolling two D6 dice 5000 times'
hist.x_labels = [x for x in range(2, max_result + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
# 添加数据
hist.add('two D6', frequencies)
# 格式必须是svg
hist.render_to_file('2_die_visual.svg')




# 世界人口地图

def get_country_code(country_name):
    """
    根据国家名返回两位国别码
    """
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

filename = r'./population.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2015:
        country_name = pop_dict['Country Name']

        # 有些值是小数，先转为float再转为int
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# 为了使颜色分层更加明显
cc_populations_1,cc_populations_2, cc_populations_3 = {}, {}, {}
for cc, population in cc_populations.items():
    if population < 10000000:
        cc_populations_1[cc] = population
    elif population < 1000000000:
        cc_populations_2[cc] = population
    else:
        cc_populations_3[cc] = population

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
world = World(style=wm_style)
world.title = 'World Populations in 2015, By Country'
world.add('0-10m', cc_populations_1)
world.add('10m-1bn', cc_populations_2)
world.add('>1bn', cc_populations_3)
world.render_to_file('world_population_2015.svg')

# https://www.jianshu.com/p/6fcd47b3528b