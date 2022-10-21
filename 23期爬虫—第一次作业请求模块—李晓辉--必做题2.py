import requests
from faker import Faker
f = Faker()
a = eval(input('请输入翻译模式中译英(0)/英译中(1):'))


while a != 0 and a != 1:
        print('对不起你输入的翻译模式不存在,请重新输入:')
        a = eval(input('请输入翻译模式中译英(0)/英译中(1):'))
        continue

else:
        b = input('请输入您想要翻译的内容:')
        url = 'https://fanyi.so.com/index/search?eng=1&validate=&ignore_trans=0&query=help%0A'
        head = {'user-agent': 'f.chrome',
                'pro': 'fanyi'}
        data = {'eng': a,
                'validate': '',
                'ignore_trans': '0',
                'query': b}
        res = requests.post(url, headers=head, data=data)
        data = res.json()
        print(data['data']['fanyi'])






