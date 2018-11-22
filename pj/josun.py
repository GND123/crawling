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
    parser.add_argument('--json_path', type=str, default='josun.json',
                    help="Path for json file to save result." )

    return parser.parse_args()


def crawling_josun(page, json_path):

    url = "http://news.chosun.com/svc/list_in/list.html?pn="
    news_company = 'josun'

    # dict obj for contain all news
    dataAll = OrderedDict()
    data_idx = 0

    for i in range(1, page+1):
        
        url = url + str(i) # URL + page
        request = requests.get(url)
        html = request.content
        soup = BeautifulSoup(html, 'html5lib')

        news_list = soup.select('#list_body_id > div.list_content > dl')
        
        for news in news_list:

            _1 = news.find('dt').a # title & link
            news_title = _1.text 
            news_link = _1['href']
            
            _2 = news.find('dd', {"class" : "date_author"}) # date, author
            news_date = _2.find('span', {"class" : "date"}).text

            """
            news_desc = news.find('dd', {"class" : "desc"}).a.text # description

            # author
            try:
                news_author = _2.find('span', {"class" : "author"}).text
                news_author = news_author.replace('\t ', '').replace('\n', '').replace(' ', '')
            except:
                print("page:{} number:{}, title:{}".format(i, data_idx, news_title))
            """
            # make dict obj
            newsData = OrderedDict()
            newsData['title'] = news_title
            newsData['link'] = news_link
            newsData['press'] = news_company
            newsData['date'] = news_date

            dataAll[str(data_idx)] = newsData
            data_idx += 1
        
        # pdb.set_trace()


        with open(json_path, 'w') as json_out:
            json.dump(dataAll, json_out, ensure_ascii=False, indent='\t')

if __name__ == '__main__':
    
    args = init_args()

    crawling_josun(args.page_num, args.json_path)

    print("Done")