# -*- condig: utf-8 -*-
import requests
from bs4 import BeautifulSoup

from collections import OrderedDict
import json

import argparse
import pdb

def init_args():
    """

    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--page_num', type=int, default=10,
                    help="Number of page want to crawling")
    parser.add_argument('--json_path', type=str, default='moneytoday.json',
                    help="Path for json file to save result." )

    return parser.parse_args()


def crawling_moneytoday(page, json_path):

    url = "http://news.mt.co.kr/newsList.html"
    news_company = 'moneytoday'

    # dict obj for contain all news
    dataAll = OrderedDict()
    data_idx = 0

    #content > ul > li:nth-child(1) > div > strong > a
    #content > ul > li:nth-child(1) > div > p > span
    for i in range(1, page+1):
        
        params = {
            'type' : '1',
            'comd' : None,
            'pDepth' : 'news',
            'pDepth1' : 'politics',
            'pDepth2' : 'Ptotal',
            'page' : str(i)
        }
        request = requests.get(url, params=params)
        html = request.content
        soup = BeautifulSoup(html, 'html5lib')

        # pdb.set_trace()

        news_list = soup.select('#content > ul > li')
        
        for news in news_list:

            _1 = news.select('div > strong > a')[0] # title & link
            _2 = news.select('div > p > span')[0] # description, date

            news_title = _1.text 
            news_link = _1['href']
            
            news_reporter = _2.text[:-19]
            news_date = _2.text[-16:]

            # make dict obj
            newsData = OrderedDict()
            newsData['title'] = news_title
            newsData['link'] = news_link
            newsData['press'] = news_company
            newsData['date'] = news_date
            newsData['reporter'] = news_reporter

            dataAll[str(data_idx)] = newsData
            data_idx += 1

        with open(json_path, 'w') as json_out:
            json.dump(dataAll, json_out, ensure_ascii=False, indent='\t')

if __name__ == '__main__':
    
    args = init_args()

    crawling_moneytoday(args.page_num, args.json_path)

    print("Done")