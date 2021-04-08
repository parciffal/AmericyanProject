from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://news.am'
site_url = 'https://news.am/arm/news/'
requesting = requests.get(url=site_url)
bs = BeautifulSoup(requesting.text, 'html.parser')
print(bs.head)
divs = bs.find_all('div', class_='news-list single-right')
print(divs)