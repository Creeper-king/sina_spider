import urllib.request

# 下载器
class PageDownloader(object):

    def download(self, url):
        if url is None:
            return
        response = urllib.request.urlopen(url)
        return response.read()