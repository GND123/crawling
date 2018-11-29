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
    parser.add_argument('--json_path', type=str, default='mydaily.json',
                        help="Path for json file to save result.")

    return parser.parse_args()


def crawling_mydaily(page, json_path):
    myurl = "http://mydaily.co.kr/new_yk/html/section_sub_mj.php?cate=social&catenum=332,552,557&listpg="
    news_company = 'mydaily'

    # dict obj for contain all news
    dataAll = OrderedDict()
    data_idx = 0

    for i in range(1, page + 1):

        url = myurl + str(i)  # URL + page
        request = requests.get(url)
        html = request.content
        soup = BeautifulSoup(html, 'html5lib')

        news_list= soup.select('#section_left > div.section_list > div.section_list_text > a')
        # section_left > div:nth-child(2) > div.section_list_text > a > dd > p
        for news in news_list:
            news_title = news.find('dt').text
            news_link = news['href']

            news_date = news.find('p').text

            # make dict obj
            newsData = OrderedDict()
            newsData['title'] = news_title
            newsData['link'] = 'http://mydaily.co.kr/new_yk/html/'+news_link
            newsData['press'] = news_company
            newsData['date'] = news_date

            dataAll[str(data_idx)] = newsData
            data_idx += 1

        # pdb.set_trace()

        with open(json_path, 'w') as json_out:
            json.dump(dataAll, json_out, ensure_ascii=False, indent='\t')


if __name__ == '__main__':
    args = init_args()

    crawling_mydaily(args.page_num, args.json_path)

    print("Done")