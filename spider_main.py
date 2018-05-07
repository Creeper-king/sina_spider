import url_manager, page_downloader, page_parser, page_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = page_downloader.PageDownloader()
        self.parser = page_parser.PageParser()
        self.outputer = page_outputer.PageOutputer()

    def craw(self, url):
        self.urls.add_new_url(url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            page_cont = self.downloader.download(new_url)
            new_urls, cont_data = self.parser.parse(new_url, page_cont)
            if new_urls is not None:
                print("new_urls：" + new_url)
                self.urls.add_new_urls(new_urls)
            if cont_data is not None:
                print("cont_data：" + new_url)
                self.outputer.output(cont_data)


if __name__ == '__main__':
    root_url = "http://www.sina.com.cn/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
