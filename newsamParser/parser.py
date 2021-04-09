import urllib3
from bs4 import BeautifulSoup as bs4


class Parser:

    def find_newsam(self):
        """Geting html.data of page to parse"""
        url = 'https://news.am'
        site_url = 'https://news.am/arm/news/'
        data_list = []
        http_pool = urllib3.connection_from_url(site_url)
        request = http_pool.urlopen('GET', site_url)
        html = request.data.decode('utf-8')
        soup = bs4(html, 'html.parser')
        arg_main = soup.find_all("div", {'class': 'news-list sub-categories'})
        arg_second = bs4(str(arg_main), 'html.parser')
        arg_last = arg_second.find_all('a', href=True)
        for arg in arg_last:
            if arg.text:
                if arg.text != 'Կարդալ ավելին ':
                    txt = arg.text[1:-1]
                    txt.strip()
                    link = url+str(arg['href'])
                    data_list.append([link, txt])

        return data_list

    def find_nytimes(self):
        url = 'https://nytimes.com'
        site_url = 'https://www.nytimes.com/section/world'
        data_list = []
        http_pool = urllib3.connection_from_url(site_url)
        request = http_pool.urlopen('GET', site_url)
        html = request.data.decode('utf-8')
        soup = bs4(html, 'html.parser')
        arg_main = soup.find_all("div", {'class': 'css-zk12ih eidyr0c0'})
        arg_second = bs4(str(arg_main), 'html.parser')
        arg_last = arg_second.find_all('ol', {'class': 'css-11jjg ekkqrpp2'})
        arg = bs4(str(arg_last), 'html.parser')
        arg_back = arg.find_all('a', href=True)
        for ar in arg_back:
            if arg.text:
                txt = ar.text
                link = url + str(ar['href'])
                if txt != '':
                    data_list.append([link, txt])

        return data_list

    def find_cnn(self):
        url = 'https://edition.cnn.com/'
        site_url = 'https://edition.cnn.com/world?refresh=1'
        data_list = []
        http_pool = urllib3.connection_from_url(site_url)
        request = http_pool.urlopen('GET', site_url)
        html = request.data.decode('utf-8')
        soup = bs4(html, 'html.parser')
        arg_main = soup.find_all("div", {'class': 'css-zk12ih eidyr0c0'})
        arg_second = bs4(str(arg_main), 'html.parser')
        arg_last = arg_second.find_all('ol', {'class': 'css-11jjg ekkqrpp2'})
        arg = bs4(str(arg_last), 'html.parser')
        arg_back = arg.find_all('a', href=True)
        for ar in arg_back:
            if arg.text:
                txt = ar.text
                link = url + str(ar['href'])
                if txt != '':
                    data_list.append([link, txt])

        return data_list