'''
获取歌名，歌手名
保存csv
'''
import requests
import re
from faker import Faker
import json
import csv

f = Faker()
url = 'https://music.163.com/discover/toplist'
head = {'user-agent': 'f.chrome'}
res = requests.get(url, headers=head)
html = res.text
mu = re.match('.*?<textarea id="song-list-pre-data" style="display:none;">(.*?)</textarea>.*?', html, re.S)
mu0 = mu.group(1)
mu_mu = json.loads(mu0)
print(mu_mu)
lst = []
for i in mu_mu:
    dic = {}
    music = i['name']
    try:
        name = i['artists'][0]['name']+'/'+i['artists'][1]['name']+'/'+i['artists'][2]['name']+\
               '/'+i['artists'][3]['name']
    # e:
    #     name = i['artists'][0]['name'] + '/' + i['artists'][1]['name'] + '/' + i['artists'][2]
    except:
        name = i['artists'][0]['name']
    print(music, name)
    dic['歌名'] = music
    dic['歌手名'] = name
    lst.append(dic)
li = ['歌名', '歌手名']
with open('网易飙升榜.csv', 'w', encoding='utf-8', newline='') as f:
    we = csv.DictWriter(f, li)
    we.writeheader()
    we.writerows(lst)



