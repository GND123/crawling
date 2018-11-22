import requests
from bs4 import BeautifulSoup

import pdb

url = "http://www.chosun.com/"

request = requests.get(url)
html = request.content
soup = BeautifulSoup(html, 'html5lib')

# pdb.set_trace()

dt_list = soup.find_all('div', attrs={"class" : "sec_con"})
print(len(dt_list))
with open("data/josun_div_sec_con.txt", "w") as f_out_dt:
    i = 1
    for dt in dt_list:
        f_out_dt.write("[%d]\n%s\n\n" % (i, dt))
        i += 1

# with open("data/josun_dl_all.txt", "w") as f_out_title:
#     for dt in dt_list:
#         f_out_title.write("="*60 + "\n%s\n%s\n" % (dt, dt.get_text().encode('utf-8')) + "="*60 + "\n\n")


#################################

# news_list = soup.find_all('dl', )
#
# with open("josun_final.txt", "w") as f:
#     for news in news_list:
#         if news.dt is not None:
#             try:
#                 title = news.dt.a.get_text()
#                 title = title.replace('\t', '')
#                 title = title.replace('\n', '')
#                 f.write(title)
#                 f.write(news.dt.a['href'] + "\n")
#             except:
#                 print("Not news:{}".format(news.dt))
##################################

# news_list = soup.select('dl.news_item') # final3
# news_list = soup.find_all('dl', attrs={"class" : "news_item" "news_item thum"}) #final4
# news_list = soup.select('dl.news_item')
# print(len(news_list))
# news_list.extend(soup.select('dl.news_item thum'))
# print(len(news_list))

# with open("josun_final4.txt", "w") as f:
#     for news in news_list:
#         if news.dt is not None:
#             try:
#                 title = news.dt.a.get_text()
#                 title = title.replace('\t', '')
#                 title = title.replace('\n', '')
#                 f.write(title)
#                 f.write(news.dt.a['href'] + "\n")
#             except:
#                 print("Not news:{}".format(news.dt))

# print("Done")