import urllib3
from bs4 import BeautifulSoup as bs4

class Parser():
    url = 'https://news.am'
    site_url = 'https://news.am/arm/news/'
    data_list = []

    def get_html(self):
        """Geting html.data of page to parse"""
        http_pool = urllib3.connection_from_url(self.site_url)
        request = http_pool.urlopen('GET', self.site_url)
        html = request.data.decode('utf-8')
        return html

    def find_news(self):
        html = self.get_html()
        soup = bs4(html, 'html.parser')
        arg_main = soup.find_all("div", {'class': 'news-list sub-categories'})
        arg_second = bs4(str(arg_main), 'html.parser')
        arg_last = arg_second.find_all('a', href=True)
        for arg in arg_last:
            if arg.text:
                print(arg['href'])
                print(arg.text)
                if arg.text != 'Կարդալ ավելին':
                    self.data_list.append([arg['href'], arg.text])

    def get_urls(self):
        return self.data_list