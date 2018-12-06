# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

from collections import OrderedDict
import json

import argparse
import pdb

from time import gmtime, strftime


def init_args():
    """

    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--page_num', type=int, default=3,
                    help="Number of page want to crawling")
    parser.add_argument('--json_path', type=str, default='mail.json',
                    help="Path for json file to save result." )

    return parser.parse_args()


def crawling_mail(page, json_path):

    url = "http://news.mk.co.kr/newsList.php"
    news_company = 'mail'

    # dict obj for contain all news
    dataAll = OrderedDict()
    data_idx = 0

    for i in range(0, page):
        
        today = strftime("%Y%m%d", gmtime())
        params = {
            'sc' : '30000001',
            'thisDate' : today,
            'page' : str(i)
        }
        request = requests.get(url, params=params)
        html = request.content
        soup = BeautifulSoup(html, 'html5lib')

        news_list = soup.select('#container_left > div.list_area > dl')
        
        for news in news_list:

            _1 = news.select('dt > a')[0] # title & link
            _2 = news.select('dd.desc')[0] # description, date

            news_title = _1.text
            news_link = _1['href']
            
            news_date = _2.select('span.date')[0].text

            # make dict obj
            newsData = OrderedDict()
            newsData['title'] = news_title
            newsData['link'] = news_link
            newsData['press'] = news_company
            newsData['date'] = news_date

            dataAll[str(data_idx)] = newsData
            data_idx += 1

        with open(json_path, 'w') as json_out:
            json.dump(dataAll, json_out, ensure_ascii=False, indent='\t')

if __name__ == '__main__':
    
    args = init_args()

    crawling_mail(args.page_num, args.json_path)

    print("Done")