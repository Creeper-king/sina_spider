import url_manager, page_downloader, page_parser, page_outputer

# 调度类
class SpiderMain(object):

    # 构造器：初始化URL管理器、下载器、解析器、输出器
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = page_downloader.PageDownloader()
        self.parser = page_parser.PageParser()
        self.outputer = page_outputer.PageOutputer()

    # 调度方法：由sina首页解析首页新闻url，并解析新闻的一些基本信息，输出到指定位置
    def craw(self, url):
        self.urls.add_new_url(url)
        while self.urls.has_new_url() and self.urls.url_count <= 12:
            new_url = self.urls.get_new_url()
            page_cont = self.downloader.download(new_url)
            new_urls, cont_data = self.parser.parse(new_url, page_cont)
            if new_urls is not None:
                self.urls.add_new_urls(new_urls)
            if cont_data is not None:
                self.outputer.collect_data(cont_data)
        self.outputer.output()
        self.outputer.fail_out(self.parser.fail_urls)

if __name__ == '__main__':
    root_url = "http://www.sina.com.cn/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

