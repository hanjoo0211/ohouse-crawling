from ohImgDownload import ohImgDownload
from ohLinkFinder import ohLinkFinder


def ohCrawler(toSearch: str, howMany: int):
    linkSet = ohLinkFinder(toSearch, howMany)
    for i, link in enumerate(linkSet):
        pad = '0'
        n = 3

        saveName = str(i).rjust(n, pad)
        ohImgDownload(link, saveName + '.jpg')
        

ohCrawler('몬스테라', 500)