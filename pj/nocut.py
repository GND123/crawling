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
    parser.add_argument('--json_path', type=str, default='nocut.json',
                    help="Path for json file to save result." )

    return parser.parse_args()


def crawling_nocut(page, json_path):

    url = "http://www.nocutnews.co.kr/news/list?page="
    news_company = 'nocut'

    headURL = "http://www.nocutnews.co.kr"
    tailURL = "?page="

    # dict obj for contain all news
    dataAll = OrderedDict()
    data_idx = 0

    #pnlNewsList > ul > li:nth-of-type(1) > dl > dt > a
    for i in range(1, page+1):
        
        params = {
            'page' : str(i)
        }
        request = requests.get(url, params=params)
        html = request.content
        soup = BeautifulSoup(html, 'html5lib')

        news_list = soup.select('#pnlNewsList > ul > li > dl')
        
        for news in news_list:
            
            try:
                _1 = news.select('dt > a')[0] # title & link
                _2 = news.select('dd.txt > a')[0] # description, date
            except Exception as e:
                print(news, i, data_idx)
                print(e)

            news_title = _1.text 
            news_link = headURL + _1['href'] + tailURL + str(i)
            
            news_date = _2.text[-21:]

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

    crawling_nocut(args.page_num, args.json_path)

    print("Done")