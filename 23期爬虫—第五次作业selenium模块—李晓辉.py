import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

url = 'https://www.vip.com/'
driver.get(url)
time.sleep(2)
driver.maximize_window()

driver.find_element(By.CLASS_NAME, 'c-search-input').send_keys('耳机')
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'c-search-input').send_keys(Keys.ENTER)
time.sleep(1)

lst = []
x = 0
for i in range(3):
    x += 1
    driver.execute_script('window.scrollTo(0, 100000000000)')
    time.sleep(2)
    driver.execute_script('window.scrollTo(0, 100000000000)')
    time.sleep(2)
    driver.execute_script('window.scrollTo(0, 100000000000)')
    time.sleep(2)
    shop = driver.find_elements(By.CLASS_NAME, 'c-goods-item')
    # print(len(shop))
    for shops in shop:
        dic = {}
        name = shops.find_element(By.CLASS_NAME, 'c-goods-item__name').text
        rate = shops.find_element(By.CLASS_NAME, 'c-goods-item__sale-price').text
        href = shops.find_element(By.CLASS_NAME, 'J-goods-item__img').get_attribute('src')
        dic['商品名称'] = name
        dic['商品价格'] = rate
        dic['商品图片'] = href
        lst.append(dic)
        # print(dic)
    if x < 3:
        driver.find_element(By.XPATH, '//*[@id="J_nextPage_link"]/i').click()
    else:
        break
print(lst)

li = ['商品名称', '商品价格', '商品图片']
with open('唯品会.csv', 'w', encoding='utf-8', newline='') as f:
    wr = csv.DictWriter(f, li)
    wr.writeheader()
    wr.writerows(lst)
