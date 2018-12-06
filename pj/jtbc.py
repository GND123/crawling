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
    parser.add_argument('--json_path', type=str, default='jtbc.json',
                    help="Path for json file to save result." )

    return parser.parse_args()


def crawling_jtbc(page, json_path):

    url = "http://news.jtbc.joins.com/section/list.aspx"
    news_company = 'jtbc'

    # dict obj for contain all news
    dataAll = OrderedDict()
    data_idx = 0

    for i in range(1, page+1):
        
        params = {
            'scode' : '',
            'pgi' : str(i)
        }
        request = requests.get(url, params=params)
        html = request.content
        soup = BeautifulSoup(html, 'html5lib')

        news_list = soup.select('#section_list > li')
        
        for news in news_list:

            _1 = news.select('dt > a')[0] # title & link
            _2 = news.select('dd.info > span.date')[0] # date

            news_title = _1.text
            news_link = _1['href']
            
            news_date = _2.text

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

    crawling_jtbc(args.page_num, args.json_path)

    print("Done")