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
    parser.add_argument('--json_path', type=str, default='digitaltimes.json',
                        help="Path for json file to save result.")

    return parser.parse_args()


def crawling_digitaltimes(page, json_path):
    myurl = "http://www.dt.co.kr/section.html?cpage="
    news_company = 'digitaltimes'

    # dict obj for contain all news
    dataAll = OrderedDict()
    data_idx = 0

    for i in range(1, page + 1):

        url = myurl + str(i)  # URL + page
        request = requests.get(url)
        html = request.content
        soup = BeautifulSoup(html, 'html5lib')

        news_list = soup.select('#container > div.section_left > div.section_list.cf > div.s_con')

        for news in news_list:
            # title & link
            _1 = news.find('div', {"class": "s_title"})
            news_title = _1.text
            news_link = _1.find('a')['href']

            news_date = news.find('div', {"class": "reporter"}).text

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

    crawling_digitaltimes(args.page_num, args.json_path)

    print("Done")