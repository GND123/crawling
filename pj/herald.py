# -*- condig: utf-8 -*-
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
    parser.add_argument('--json_path', type=str, default='herald.json',
                    help="Path for json file to save result." )

    return parser.parse_args()


def crawling_herald(page, json_path):

    url = "http://biz.heraldcorp.com/list.php"
    news_company = 'herald'

    # dict obj for contain all news
    dataAll = OrderedDict()
    data_idx = 0

    #body > div > div.view_bg > div.con_left > div.list > ul > li:nth-child(1) > a > div > div.list_t1.ellipsis

    for i in range(1, page+1):
        
        params = {
            'ct' : '010000000000',
            'np' : str(i)
        }
        request = requests.get(url, params=params)
        html = request.content
        soup = BeautifulSoup(html, 'html5lib')

        news_list = soup.select('body > div > div.view_bg > div.con_left > div.list > ul > li')
        
        # pdb.set_trace()

        for news in news_list:

            _1 = news.select('a')[0] # link
            _2 = _1.select('div > div.list_t1.ellipsis')[0] # title
            _3 = _1.select('div > div.list_t3')[0] # date

            # pdb.set_trace()

            news_title = _2.text
            news_link = "None" # 머리에 오는 url이 모두 다름. 일단 보류
            
            news_date = _3.text

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

    crawling_herald(args.page_num, args.json_path)

    print("Done")