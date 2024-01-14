import time
import requests
from requests import get
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


driver = webdriver.Chrome()

url = 'https://www.avito.ru/novosibirsk/avtomobili/audi/a3-ASgBAgICAkTgtg3elyjitg3gnSg?cd=1&p=1&radius=200&searchRadius=200'
print(url)
driver.get(url)
wait = WebDriverWait(driver, 10)
elements = driver.find_elements(By.CSS_SELECTOR, 'div[data-marker="item"]')


for el in elements:
    info= el.find_element(By.CSS_SELECTOR, 'a[itemprop="url"]').get_attribute('title')
    price = el.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')
    price = "{:,}".format(int(price))
    print(info + ' Стоимость = ' + price)