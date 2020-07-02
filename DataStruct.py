import time #코드를 실행하는데 딜레이를 걸어주는 모듈
from selenium import webdriver #가상 드라이브를 이용하여 html 정보를 받아온다.
from selenium.webdriver.common.keys import Keys #셀레니움의 키를 인식하는 모듈
from bs4 import BeautifulSoup
import urllib.request #크롤링 모듈이지만 이미지 저장을 위해 사용
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException    # 태그가 없는 예외 처리
import pandas as pd
from konlpy.tag import Okt

"""
    Test_Sample1
    people1 = FoodData()
    people1.setUrl('https://ko.wiktionary.org/wiki/분류:한국어_음식')
    people1.foodSearch()
    FoodList = people1.getData()
    print(FoodList)
"""
class FoodData:
    def setUrl(self, url):
        self.url = url

    def getData(self):
        return self.totalResult

    def foodSearch(self):
        chrome_path = "chromedriver" #자신의 크롬드라이브의 경로를 지정

        base_url = self.url #접속하고자하는 url'

        options = webdriver.ChromeOptions()

        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(chrome_path, options=options)
        driver.get(base_url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        parsor_result = soup.find_all('a')
        result = []
        for data in parsor_result:
            title = data.get('title')
            if data.get('title'):
                result.append(title)

        self.totalResult = result[1 : 201]


if __name__ == " __main__":
    people1 = FoodData()
    people1.setUrl('https://ko.wiktionary.org/wiki/분류:한국어_음식')
    people1.foodSearch()
    FoodList = people1.getData()
    print(FoodList)



