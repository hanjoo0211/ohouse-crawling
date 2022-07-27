from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def ohLinkFinder(toSearch: str):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('start-maximized')
    driver = webdriver.Chrome('chromedriver.exe', options=options)

    toSearch = toSearch.replace("#", "%23")
    url = f"https://ohou.se/cards/feed?query={toSearch}"

    linkSet = set()
    driver.get(url)
    
    last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    while len(linkSet) <= 300:
        linkList = driver.find_elements(By.CLASS_NAME, 'card-search-item__content__link')
        for _ in linkList:
            link = _.get_attribute('href')
            linkSet.add(link)

        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(1.0)
        new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_page_height == last_page_height:
            time.sleep(1.0)
            if new_page_height == driver.execute_script("return document.documentElement.scrollHeight"):
                break
        else:
            last_page_height = new_page_height

    return linkSet


def infinite_loop(driver):
    #스크롤 내리기
    last_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True: # True
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(1.0)
        new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_page_height == last_page_height:
            time.sleep(1.0)
            if new_page_height == driver.execute_script("return document.documentElement.scrollHeight"):
                break
        else:
            last_page_height = new_page_height


print(ohLinkFinder("#몬스테라"))