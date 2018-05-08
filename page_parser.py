import logging
import re
from bs4 import BeautifulSoup

# 解析器
class PageParser(object):

    def __init__(self):
        self.fail_urls = set()

    def _get_new_urls(self, bfs):
        new_urls = set()
        links = bfs.find_all('a', href=re.compile(r'http://news.sina.com.cn/\S+\.shtml'))
        for link in links:
            new_url = link['href']
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, page_url, bfs):
        if page_url == "http://www.sina.com.cn/":
            return
        res_data = {}
        title_node = bfs.find('h1', class_="main-title")
        if title_node is None:
            title_node = bfs.find(id="artibodyTitle")
        date_node = bfs.find('span', class_="date")
        if date_node is None:
            date_node = bfs.find(id="navtimeSource")
        if title_node is None or date_node is None:
            self.fail_urls.add(page_url)
            return
        res_data['title'] = title_node.get_text()
        res_data['date'] = date_node.get_text()
        res_data['url'] = page_url
        return res_data


    def parse(self, url, cont):
        if url is None or cont is None:
            return
        bfs = BeautifulSoup(cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(bfs)
        new_data = self._get_new_data(url, bfs)
        return new_urls, new_data