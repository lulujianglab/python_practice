
'''
author:蒋璐
time: 2018/8/29
'''

from bs4 import BeautifulSoup
import requests

url = "https://www.tripadvisor.cn/Hotels-g294212-Beijing-Hotels.html#apg=74712b8a776e4aa29d9e72c0e1341982&ss=AC1820522A19A4E7B9D7B643AB674093"

''' 
   主函数
'''
def hotel_data(url):

    with requests.get(url) as web_data:
        Soup = BeautifulSoup(web_data.text, "lxml")

        ''' 
            获取酒店名
        '''
        hotels = Soup.select("div > div > div.meta_listing.ui_columns.is-mobile.nonen > div.ui_column.is-8.main_col.allowEllipsis > div.prw_rup.prw_meta_hsx_listing_name.listing-title > div > a")
        # for hotel in hotels:
        #     print(hotel.get_text())

        ''' 
            获取酒店价格
        '''
        prices = Soup.select("div > div > div.meta_listing.ui_columns.is-mobile.nonen > div.ui_column.is-8.main_col.allowEllipsis > div.main-cols > div.comm-col > div > div > div.premium_offer.no_cpu.ui_columns.is-mobile.is-gapless.is-multiline.metaOffer > div.priceBlock.ui_column.is-12-tablet > div.price-wrap > div")
        # for price in prices:
        #     print(price.get_text().split("带")[0])

        ''' 
            创建列表存放字典表
        '''
        informations = []
        for hotel, price in zip(hotels, prices):
            data = {
                "hotel" : hotel.get_text(),
                "price" : price.get_text().split("带")[0].split("￥")[1]
            }
            informations.append(data)
        print(informations)

    return informations

# hotel_data(url)
def creat_txt(informations):

    """保存为txt文件

    :param informations:
    """
    file1 = open("info.txt", "a")
    for info in informations:
        file1.write(info["hotel"].ljust(30) + info["price"].ljust(20))
        file1.write("\n")
    file1.close()

informations = hotel_data(url)
creat_txt(informations)

'''   
    hotel:#taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_0 > div:nth-child(1) > div > div.meta_listing.ui_columns.is-mobile.nonen > div.ui_column.is-8.main_col.allowEllipsis > div.prw_rup.prw_meta_hsx_listing_name.listing-title > div > a
   
    price: #taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_0 > div:nth-child(1) > div > div.meta_listing.ui_columns.is-mobile.nonen > div.ui_column.is-8.main_col.allowEllipsis > div.main-cols > div.comm-col > div > div > div.premium_offer.no_cpu.ui_columns.is-mobile.is-gapless.is-multiline.metaOffer > div.priceBlock.ui_column.is-12-tablet > div.price-wrap > div

'''
