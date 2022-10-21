import requests
from faker import Faker
f = Faker()
name = input('请输入搜索内容:')
ye = eval(input('请输入起始页:'))
j = eval(input('请输入结束页:'))
for i in range(ye, j+1):
    url = f'https://sogou.com/web?query={name}&from=index-nologin&s_from=index&sut=13523&sst0=1662595413632&lkt=3%2C1662595412713%2C1662595413056&sugsuv=1662473611299&sugtime=1662595413632&page={(i-1)+1}&ie=utf8&p=40040100&dp=1&w=01019900&dr=1'
    head = {'user-agent': 'f.chrome'}
    res = requests.get(url, headers=head)
    # print(res.text)

    with open(f'{name}第{i}页.html','w',encoding='utf-8') as f:
        f.write(res.text)
