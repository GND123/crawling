# -*- coding: utf-8 -*-s
import json
import requests
from bs4 import BeautifulSoup as bs
from collections import OrderedDict
# pip3 install requests
# pip3 install bs4
# python3 hani.py

def haniCrawling():
    press = 'hani'
    dataAll = OrderedDict()
    index = 0
    for i in range(1, 30):
        url = 'http://www.hani.co.kr/arti/list1.html'
        headUrl = "http://www.hani.co.kr"
        url = url[:31] + str(i) + url[32:]

        html = requests.request('GET', url)

        bsobj = bs(html.text, 'html.parser')
        aTag = bsobj.select(
            '#section-left-scroll-in > div.section-list-area > div > div > h4 > a'
        )
        dateTag = bsobj.select(
            '#section-left-scroll-in > div.section-list-area > div > div > p > span'
        )
        start = index
        for title in aTag:
            newsData = OrderedDict()
            newsData["link"] = headUrl + title['href']
            newsData["title"] = title.text
            newsData["press"] = 'hani'
            dataAll[str(index)] = newsData
            index += 1
        for date in dateTag:
            temp = date.text
            temp = temp[:4] + temp[5:7] + temp [8:10]
            dataAll[str(start)]["date"] = temp
            start += 1
    with open('hani.json', 'w') as f:
        json.dump(dataAll, f, ensure_ascii=False, indent='\t')



if __name__ == "__main__":
    haniCrawling()
