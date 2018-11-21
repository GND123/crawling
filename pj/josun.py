import requests
from bs4 import BeautifulSoup

import pdb

url = "http://www.chosun.com/"

request = requests.get(url)
html = request.content
soup = BeautifulSoup(html, 'html5lib')

"""
with open('./josun_soup.txt', 'w') as f_out:
    f_out.write(str(soup))
"""
# pdb.set_trace()

# dt_list = soup.find_all('dl')
# with open("data/josun_dl.txt", "w") as f_out_dt:
#     for dt in dt_list:
#         f_out_dt.write("%s\n" % dt)

# with open("data/josun_dl_all.txt", "w") as f_out_title:
#     for dt in dt_list:
#         f_out_title.write("="*60 + "\n%s\n%s\n" % (dt, dt.get_text().encode('utf-8')) + "="*60 + "\n\n")

news_list = soup.find_all('dl')
# pdb.set_trace()

with open("josun_final.txt", "w") as f:
    for news in news_list:
        if news.dt is not None:
            try:
                title = news.dt.a.get_text()
                title = title.replace('\t', '')
                title = title.replace('\n', '')
                f.write(title)
                f.write(news.dt.a['href'] + "\n")
            except:
                print("Not news:{}".format(news.dt))

print("Done")