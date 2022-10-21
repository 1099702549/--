# (必做题2)目标网站：https://www.9ku.com/music/t_new.htm
# 需求：
# 1、爬取2022最新歌曲所有的歌曲名、歌曲详情页地址 共300条数据
# 2、将爬取的数据保存到csv文件中
# 3、要求使用xpath语法，写好注释
import requests
import csv
from faker import Faker
from lxml import etree
f = Faker()

url = 'https://www.9ku.com/music/t_new.htm'
head = {'user-agent': 'f.chrome'}
res = requests.get(url, headers=head)
res.encoding = 'utf-8'
res1 = res.text
data = etree.HTML(res1)
div = data.xpath('//div[@class="songList clearfix"]/ol/li')
lsp = []
for div1 in div:
    dic = {}
    name = div1.xpath('./a[@class="songName "]/text()')
    url = div1.xpath('./a/@href')
    dic['名字'] = name[0]
    dic['地址'] = 'https://www.9ku.com'+url[0]
    # print(name, url)
    lsp.append(dic)
    print(lsp)
li = ['名字', '地址']
with open('音乐.csv', 'w', encoding='utf-8', newline='') as f:
    xiaoli = csv.DictWriter(f, li)
    xiaoli.writeheader()
    xiaoli.writerows(lsp)













































