# (必做题1)目标网站：http://www.piaofang.biz/
# 需求：
# 1、爬取页面所有电影名及票房(提示一共100条数据  数据必须获取完整  其中有两条需要特殊处理)
# 2、将获取到的数据保存到csv文件中 注意不能忽略表头
# 3、使用xpath数据解析方式实现 写好注释
import requests
import csv
from faker import Faker
from lxml import etree
f = Faker()

url = 'http://www.piaofang.biz/'
head = {'user-agent': 'f.chrome'}

res = requests.get(url, headers=head)
res.encoding = 'gb2312'
data = res.text
# print(data)
ele = etree.HTML(data)
div = ele.xpath('//div[@class="zhuti"]/table/tr')[1:]

lst = []
for div1 in div:
    dic = {}
    if div1.xpath('./td'):
        if div1.xpath('./td[@class="title"]/a'):
            name = div1.xpath('./td[@class="title"]//text()')[:3]   # 无语住了，研究一晚上竟然这么简单，人麻了
        else:
            name = div1.xpath('./td[@class="title"]/text()')
        piao = div1.xpath('./td[@class="piaofang"]/span/text()')

        dic['电影名'] = ''.join(name)
        dic['票房'] = ''.join(piao)
        lst.append(dic)
print(lst)
li = ['电影名', '票房']
with open('电影.csv', 'w', encoding='utf-8', newline='') as f:
    xiaoli = csv.DictWriter(f, li)
    xiaoli.writeheader()
    xiaoli.writerows(lst)
















































