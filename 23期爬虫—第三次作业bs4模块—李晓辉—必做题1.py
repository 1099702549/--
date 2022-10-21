"""(必做题1)目标网站：https://sc.chinaz.com/tupian/
需求：
1、翻页(指定页数例如1-4页  2-4页)爬取图片名字，图片链接
2、将爬取的数据保存到csv
"""
import requests
from faker import Faker
import csv
from bs4 import BeautifulSoup
f = Faker()

head = {'User-Agent': 'f.chrome'}
a = eval(input('请输入起始页:'))
b = eval(input('请输入结束页:'))
lst = []
for i in range(a, b+1):
    if i == 1:
        url = 'https://sc.chinaz.com/tupian/'
    else:
        url = f'https://sc.chinaz.com/tupian/index_{i}.html'
    res = requests.get(url, headers=head)
    res.encoding = 'utf-8'
    data = res.text
    # print(data)
    soup = BeautifulSoup(data, 'lxml')
    div = soup.select('div.item')
    # print(div)
    lt = []
    for bot in div:
        dic = {}
        it = bot.find('a')
        href = 'https://sc.chinaz.com' + it.get('href')
        # https://sc.chinaz.com/tupian/22092547149.htm
        name = list(it.stripped_strings)[0]
        # print(name, href)
        dic['名字'] = name
        dic['地址'] = href
        lt.append(dic)
    lst += lt
l = ['名字', '地址']
with open('tu.csv', 'w', encoding='utf-8', newline='') as f:
    witer = csv.DictWriter(f, l)
    witer.writeheader()
    witer.writerows(lst)














# with open('tupian.csv', 'w', encoding='utf-8', newline='') as f:
#     write = csv.DictWriter(f, fieldnames=['name', 'url1'])
#     write.writeheader()
#     write.writerows(li)
#



































