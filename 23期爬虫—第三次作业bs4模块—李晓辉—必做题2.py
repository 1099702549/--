"""(必做题2)目标网站：https://sc.chinaz.com/yinxiao/
需求：
1、翻页(和第一题同理)爬取网页上的音乐名字，音乐链接
2、将爬取的数据保存到csv
"""

import requests
import csv
from bs4 import BeautifulSoup
from faker import Faker
f = Faker()
a = eval(input('请输入起始页:'))
b = eval(input('请输入结束页:'))
la = []
for i in range(a, b+1):
    url = f'https://sc.chinaz.com/yinxiao/index_{i}.html'
    head = {'User-Agent': 'f.chrome'}
    res = requests.get(url, headers=head)
    data = res.text
    soup = BeautifulSoup(data, 'lxml')
    rig = soup.select('div.right-head')[1:]
    lst = []
    for aud in rig:
        dic = {}
        it = aud.find('a')
        herf = 'https://sc.chinaz.com' + it.get('href')
        name = list(it.stripped_strings)[0]
        # print(name, herf)
        # https://sc.chinaz.com/yinxiao/220921003050.htm
        dic['名字'] = name
        dic['地址'] = herf
        # print(dic)
        lst.append(dic)
    print(lst)
    la += lst
l = ['名字', '地址']
with open('mui.csv', 'w', encoding='utf-8', newline='') as f:
    witer = csv.DictWriter(f, l)
    witer.writeheader()
    witer.writerows(la)











