import re
from bs4 import BeautifulSoup


class PageParser(object):

    def _get_new_urls(self, page_url, suop):
        if page_url != "http://www.sina.com.cn/":
            return
        new_urls = set()
        links = suop.find_all('a', href=re.compile(r'http://news.sina.com.cn/\S+\.shtml'))
        for link in links:
            new_url = link['href']
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, page_url, suop):
        if page_url == "http://www.sina.com.cn/":
            return
        res_data = {}
        title_node = suop.find('h1', class_="main-title")
        if title_node is None:
            return
        res_data['title'] = title_node.text
        date_node = suop.find('span', class_="date")
        res_data['date'] = date_node.get_text()
        res_data['url'] = page_url
        return res_data



    def parse(self, url, cont):
        if url is None or cont is None:
            return
        suop = BeautifulSoup(cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(url, suop)
        new_data = self._get_new_data(url, suop)
        return new_urls, new_data