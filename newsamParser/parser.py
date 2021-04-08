import requests
from bs4 import BeautifulSoup

class Parser():
    url = 'https://news.am'
    site_url = 'https://news.am/arm/news/'

    def get_html(self):
        """Geting html of page we need"""
        requesting = requests.get(url=self.site_url)
        return requesting.text


    def find_news(self):
        html = self.get_html()
        bs = BeautifulSoup(html, 'lxml')
        divs = bs.find_all('div', class_='news-list sub-categories')
        print(divs)