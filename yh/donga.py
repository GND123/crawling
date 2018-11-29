# -*- coding: utf-8 -*-
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
    parser.add_argument('--json_path', type=str, default='donga.json',
                        help="Path for json file to save result.")

    return parser.parse_args()


def crawling_donga(page, json_path):
    news_url = "http://news.donga.com/List"
    news_company = 'donga'

    # dict obj for contain all news
    dataAll = OrderedDict()
    data_idx = 0

    for i in range(1, page + 1):

        url = news_url + '?p=' + str(20*(i-1)+1)  # URL + page
        request = requests.get(url)
        html = request.content
        soup = BeautifulSoup(html, 'html5lib')
        news_list = soup.select('#contents > div > div.rightList')
        for news in news_list:
            news_title = news.find('span', {"class": "tit"}).text
            news_link = news.find('a')['href']
            news_date = news.find('span', {"class": "date"}).text

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

    crawling_donga(args.page_num, args.json_path)

    print("Done")