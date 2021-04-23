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
            if ar.text:
                txt = ar.text
                link = url + str(ar['href'])
                if txt != '':
                    data_list.append([link, txt])

        return data_list

    def find_tert(self):
        url = 'https://www.tert.am'
        site_url = 'https://www.tert.am/am/'
        data_list = []
        http_pool = urllib3.connection_from_url(site_url)
        request = http_pool.urlopen('GET', site_url)
        html = request.data.decode('utf-8')
        soup = bs4(html, 'html.parser')
        arg_main = soup.find_all("div", {'class': 'inner-content clear-fix'})
        arg_second = bs4(str(arg_main), 'html.parser')
        arg_last = arg_second.find_all('div', {'class': 'inner-content__inner-right'})
        arg = bs4(str(arg_last), 'html.parser')
        arg_back = arg.find_all('div', {'class': 'tab-wrapper'})
        arg_second = bs4(str(arg_back), 'html.parser')
        arg = arg_second.find_all('a', href=True)
        for ar in arg:
            if ar.text:
                txt = ar.text
                txt = txt.strip()
                link = url + str(ar['href'])
                if txt != 'Իրադարձային' and txt != '' and txt != 'Սպորտ' and txt != 'Իրավունք':
                    if txt != 'Քաղաքականություն' and txt != 'Մամուլի տեսություն' and txt != 'Ժամանց':
                        data_list.append([link, txt])

        return data_list

    def find_lurer(self):
        url = 'https://lurer.com'
        site_url = 'https://lurer.com/?l=am'
        data_list = []
        http_pool = urllib3.connection_from_url(site_url)
        request = http_pool.urlopen('GET', site_url)
        html = request.data.decode('utf-8')
        soup = bs4(html, 'html.parser')
        arg_main = soup.find_all("div", {'class': 'main clearfix'})
        arg_second = bs4(str(arg_main), 'html.parser')
        arg_last = arg_second.find_all('div', {'class': 'mainCenterWrapperRight'})
        arg = bs4(str(arg_last), 'html.parser')
        arg_back = arg.find_all('div', {'class': 'timeline'})
        arg_second = bs4(str(arg_back), 'html.parser')
        arg = arg_second.find_all('a', href=True)
        for ar in arg:
            if ar.text:
                txt = ar.text
                txt = txt.strip()
                link = url + str(ar['href'])
                if txt != '':
                    data_list.append([link, txt])

        return data_list

    def find_curr(self):
        site_url = 'https://news.am/arm/news/'
        data_list = {}
        lt = []
        http_pool = urllib3.connection_from_url(site_url)
        request = http_pool.urlopen('GET', site_url)
        html = request.data.decode('utf-8')
        soup = bs4(html, 'html.parser')
        arg_main = soup.find("div", {'class': 'currency-value'})
        arg_second = bs4(str(arg_main), 'html.parser')
        arg_last = arg_second.find_all('div', {'class': 'value'}, text=True)
        for ar in arg_last:
            text = str(ar.text)
            text.split()
            lt.append(text)
        data_list['usd'] = 'DRAM to USD:' + lt[0]
        data_list['eur'] = 'DRAM to EURO: ' + lt[1]
        data_list['rub'] = 'DRAM to RUB:' + lt[2]

        return data_list
