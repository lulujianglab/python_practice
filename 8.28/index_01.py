
'''
author:蒋璐
time: 2018/8/28
'''

from bs4 import BeautifulSoup

messages = []

''' 
   爬虫获取数据的函数
   :return messages
'''
def crawDatas():
    with open("./prictise/index.html", "r", encoding="utf-8") as data:

        Soup = BeautifulSoup(data, "lxml")

        titles = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a")

        prices = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right")

        stars = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)")


        for title, price, star in zip(titles, prices, stars):
            data = {
                "title": title.get_text(),
                "price": price.get_text().split("$")[1],
                "star-count": len(star.find_all("span","glyphicon glyphicon-star"))
            }

            messages.append(data)

    print(messages)
    return messages

def creat_txt(messages):

    '''
       将爬虫获取的数据写入文件
       :param messages
    '''

    newFile = open("message.txt", "a")
    for message in messages:
        newFile.write(message["title"].ljust(20) + message["price"].ljust(20) + str(message["star-count"]).ljust(20))
        newFile.write("\n")
    newFile.close()
messages = crawDatas()
creat_txt(messages)