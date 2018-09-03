
'''
author:蒋璐
time: 2018/8/28
'''

from bs4 import BeautifulSoup
import requests

url = "https://www.tripadvisor.cn/Restaurants-g294212-Beijing.html"

''' 
   主函数
'''
def output_info(url):

    with requests.get(url) as web_data:
        Soup = BeautifulSoup(web_data.text, "lxml")

        ''' 
            获取点名
        '''
        shopNames = Soup.select("div.ui_columns.is-mobile > div.ui_column.is-9.shortSellDetails > div.title > a")
        # for shopName in shopNames:
        #     print(shopName.get_text())

        ''' 
            获取点评数量
        '''
        nums = Soup.select("div.ui_columns.is-mobile > div.ui_column.is-9.shortSellDetails > div.rating.rebrand > span.reviewCount > a")
        # for num in nums:
        #     print(num.get_text().split("条")[0])

        ''' 
            创建列表存放字典表
        '''
        informations = []
        for shopName, num in zip(shopNames, nums):
            data = {
                shopName.get_text().split("\n")[1] : num.get_text().split("条")[0].split("\n")[-1]
            }
            informations.append(data)
        print(informations)

output_info(url)

'''   
    shopName: #eatery_3512046 > div.ui_columns.is-mobile > div.ui_column.is-9.shortSellDetails > div.title > a
    num: #eatery_9810329 > div.ui_columns.is-mobile > div.ui_column.is-9.shortSellDetails > div.rating.rebrand > span.reviewCount > a
'''
