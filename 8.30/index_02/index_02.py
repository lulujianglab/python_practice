from bs4 import BeautifulSoup
import requests
import pymongo

url = "http://www.mayi.com/beijing/"

# 手机端
headers = {
    "Cookie" : "_channel=tg_baidu; _caname=pinzhuan_dz_bt; mayi_uuid=5332292984345820788107; _my_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22tg_baidu%22%2C%22ca_n%22%3A%22pinzhuan_dz_bt%22%2C%22ca_i%22%3A%22ad%22%7D; _ga=GA1.2.1106082146.1535509093; _gid=GA1.2.60425182.1535509093; bad_id73859f20-f357-11e6-b43e-3b18b16942dc=cb427ec1-ab31-11e8-953b-219cef9748c6; _ip=111.203.12.97; viewhistory=*851952143; room_851952143=http://www.mayi.com/room/851952143; __jsluid=891fc43c5cc9cd83fc594499b20e9404; _keyword=; _caid=; Qs_lvt_101147=1535509140%2C1535607019; Qs_pv_101147=1510010507289344800%2C4427323643241822700%2C2645420871355934700%2C3733374157516228600%2C4159806077712125000; sid=486203048476064; Hm_lvt_0294bbb72b1c6a6b342da076397c9af2=1535509096,1535510523,1535607021; nice_id73859f20-f357-11e6-b43e-3b18b16942dc=ca2c9451-ac15-11e8-953b-219cef9748c6; cto_lwid=cf6ea931-cca7-48c1-acb0-6ae47738de7b; SESSION=ce8df05f-f74d-438b-8e8c-06460bcc46e0; Hm_lpvt_0294bbb72b1c6a6b342da076397c9af2=1535609155; _gat_gtag_UA_63543541_1=1",
    "User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}

def rentHouse(url):

    """爬取租房标题、价格、图片链接数据

    :param url:
    """
    with requests.get(url,headers = headers) as web_data:
        Soup = BeautifulSoup(web_data.text, "lxml")
        titles = Soup.select("section > div.room-list > div > a > div.room-info.clearfloat > div.room-left.fl.font_24.w_full > p.title.font_34.c_black.hidden-txt.w_full")
        print(titles)

        prices = Soup.select("section > div.room-list > div > a > div.relave > div.priceBox.asote > span")
        print(prices)

        images = Soup.select("section > div.room-list > div > a > div.relave > img")
        print(images)

        rentHouse_data = []

        for title, price, image in zip(titles, prices,images):
            data = {
                "title" : title.get_text(),
                "price" : price.get_text()[1:],
                "image" : image.get("data-original")
            }
            rentHouse_data.append(data)
    return rentHouse_data

rentHouse_info = rentHouse(url)

client = pymongo.MongoClient("localhost", 27017)

mayizufang = client["jianglu"]

zufang_sheet = mayizufang["jianglu"]

for info in rentHouse_info:
    zufang_sheet.insert_one(info)


"""
#content-room > section > div.room-list > div:nth-child(3) > a > div.room-info.clearfloat > div.room-left.fl.font_24.w_full > p.title.font_34.c_black.hidden-txt.w_full

#content-room > section > div.room-list > div:nth-child(3) > a > div.relave > div.priceBox.asote > span

#content-room > section > div.room-list > div:nth-child(22) > a > div.relave > img
"""