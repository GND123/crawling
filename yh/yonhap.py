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
    parser.add_argument('--json_path', type=str, default='yonhap.json',
                        help="Path for json file to save result.")

    return parser.parse_args()


def crawling_yonhap(page, json_path):
    myurl = "https://www.yna.co.kr/news/"
    news_company = 'yonhap'
    headURL = "https://www.yna.co.kr"

    # dict obj for contain all news
    dataAll = OrderedDict()
    data_idx = 0

    for i in range(1, page + 1):

        url = myurl + str(i)  # URL + page
        request = requests.get(url)
        html = request.content
        soup = BeautifulSoup(html, 'html5lib')

        news_contents = soup.find('div', {"class":"contents01"})
        news_list= news_contents.select('li.section02')

        for news in news_list:
            _1 = news.find('strong').a  # title & link
            news_title = _1.text
            news_link = headURL+_1['href']

            news_date = news.find('span', {"class": "p-time"}).text

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

    crawling_yonhap(args.page_num, args.json_path)

    print("Done")