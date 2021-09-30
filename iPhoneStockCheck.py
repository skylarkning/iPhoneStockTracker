# coding: utf-8
import requests
import time
import urllib3
import winsound

urllib3.disable_warnings()

store_url = 'https://reserve-prime.apple.com/CA/en_CA/reserve/A/stores.json'
products = 'https://reserve-prime.apple.com/CA/en_CA/reserve/A/availability?iPP=N'
availability_url = 'https://reserve-prime.apple.com/CA/en_CA/reserve/A/availability.json'  # iPhone 13 Pro Max

#如果要添加其他店铺，在下面加上店铺R开头代码：https://reserve-prime.apple.com/CA/en_CA/reserve/A/stores.json
#要添加其它机型配置，可以在苹果官网把具体配置加到购物车然后URL里M开头C/A结尾的就是
stores = [('R121', 'Eaton Centre'), ('R120', 'Yorkdale'), ('R333', 'Fairview')]
product = 'MLJD3VC/A'  # iPhone 13 Pro Max 256G 蓝
product = 'MLJA3VC/A'  # iPhone 13 Pro Max 256G 金色
#product = 'MGLA3CH/A'  # iPhone 12 Pro 128G 银色

#请记得在下面也加上手机的机型代码
products = [
    ('MLJD3VC/A', 'iPhone 13 Pro Max 256G Blue'),
    ('MLJA3VC/A', 'iPhone 13 Pro Max 256G Gold'),
#    ('MLKG3VC/A', 'iPhone 13 PM黑'),

]

print('店铺：', stores)
print('型号：', product)

s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0'

i = 0
while True:
    i += 1
    try:
        availability = s.get(availability_url, verify=False).json()
        for store in stores:
            for product in products:
                product_availability = availability['stores'][store[0]][product[0]]
                contract_state = product_availability['availability']['contract']
                print(i, '\t', store[1], '\t', product[1], '\t', product_availability)
                if contract_state:
                    winsound.Beep(2000, 1000)
    except Exception as e:
        print(i, '获取库存错误', e)

    time.sleep(1)

