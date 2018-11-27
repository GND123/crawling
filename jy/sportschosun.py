import requests
import urllib.parse
import json
from bs4 import BeautifulSoup

url = "http://sports.chosun.com/latest/main.htm"
res=requests.get(url)
html = res.content
soup = BeautifulSoup(html, 'html5lib')
press = []
searchObj = []
box = []
link = []
temp = []
date = []
datef = []
data = []

box = soup.find("div", {"class":"contlist"})
temp= box.find_all("dt")
for i in range(len(temp)):
    if i%2==1:
        searchObj.append(temp[i])
datef = box.find_all("dd")

for i in range(len(searchObj)):
    temp = searchObj[i].find('a')
    link.append('http://sports.chosun.com'+temp.get('href'))

for i in datef:
    temp = i.find("span")
    date.append(temp.text.strip())

for i in range(len(searchObj)):
    searchObj[i] = searchObj[i].text.strip()

for i in range(len(searchObj)):
    press.append('sportchosun')

data = list(zip(searchObj, link, date, press))

for i in data:
    print(i)
