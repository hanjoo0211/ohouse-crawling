from bs4 import BeautifulSoup as bs
import requests
import re
import urllib.request


def ohImgDownload(url: str, saveName: str):
    html = requests.get(url).text
    soup = bs(html, 'html.parser')
    imgHtmlList = soup.select('img')

    p = re.compile(r'2x,.+? 3x')
    for i in imgHtmlList:
        imgHtml = str(i)
        if p.search(imgHtml):
            link = re.findall(p, str(i))
            link = link[0].replace("2x,", "").replace(" 3x","")

            # fileName = re.findall(r'snapshots/.+?\?', link)
            # fileName = fileName[0].replace("snapshots/", "").replace("?", "")

            # fileExt = re.findall(r'\.[a-z]+', fileName)[0]
            break

    # urllib.request.urlretrieve(link, saveName + fileExt)
    urllib.request.urlretrieve(link, saveName)