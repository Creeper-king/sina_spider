# 输出
import codecs


class PageOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output(self):
        fout = codecs.open("sina_news.html", 'w', 'utf-8')

        fout.write("<html>\r")
        fout.write("\t<head>\r")
        fout.write("\t\t<meta charset=\"utf-8\">\r")
        fout.write("\t</head>\r")
        fout.write("\t<body>\r")
        fout.write("\t\t<table>\r")
        for data in self.datas:
            fout.write("\t\t\t<tr>\r")
            fout.write("\t\t\t\t<td><a href=\"%(url)s\">%(title)s</a></td>\r" % {'url': data['url'], 'title': data['title']})
            fout.write("\t\t\t\t<td>%s</td>\r" % data['date'])
            fout.write("\t\t\t</tr>\r")
        fout.write("\t\t</table>\r")
        fout.write("\t</body>\r")
        fout.write("</html>\r")
        fout.close()

    def fail_out(self, fail_urls):
        fout = codecs.open("fail_urls.log", 'w', 'utf-8')
        fout.write("解析失败的URL：\r")
        for url in fail_urls:
            fout.write(url + "\r")
        fout.close()