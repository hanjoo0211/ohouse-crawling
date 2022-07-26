from bs4 import BeautifulSoup as bs
import requests
import re
import urllib.request
import ssl

url = "https://ohou.se/cards/17735135?affect_type=CardSearch&affect_id=0&query=%23%EB%AA%AC%EC%8A%A4%ED%85%8C%EB%9D%BC"
html = requests.get(url).text
soup = bs(html, 'html.parser')
imgHtmlList = soup.select('img')

p = re.compile(r"2x,.+? 3x")
for i in imgHtmlList:
    imgHtml = str(i)
    if p.search(imgHtml):
        link = re.findall(r'2x,.+? 3x', str(i))
        link = link[0].replace("2x,", "").replace(" 3x","")
        break
print(link)

urllib.request.urlretrieve(link, "test.jpeg")