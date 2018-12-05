# coding:utf-8
'''
爬虫控制模块
调用其他模块完成数据抓取
'''
import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    def __init__(self): #初始化各个模块.

        # 定义url管理器的对象
        self.urls = url_manager.UrlManager()
        # html下载器
        self.downloader = html_downloader.HtmlDownloader()
        # html解析器
        self.parser = html_parser.HtmlParser()
        # html输出器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):

        count = 1 #记录爬取url个数
        self.urls.add_new_url(root_url) #将入口url添加到url管理器

        while self.urls.has_new_url():
            try:
                # 获取一个待爬取的url
                new_url = self.urls.get_new_url()
                # 打印序号和RUL
                print('craw %d : %s'%(count, new_url))

                # 下载页面内容并存储在html_cont
                html_cont = self.downloader.download(new_url)
                # 解析页面并获得URL列表和数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 将新的url列表加入url管理器
                self.urls.add_new_urls(new_urls)
                # 输出器获得数据
                self.outputer.collect_data(new_data)

                if count==30: #爬取30个页面
                    break
                count += 1

            except Exception as err:
                print("craw failed：", err) #错误信息返回

        #输出收集好的数据到html
        self.outputer.output_html()

# 主函数
if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/python" #入口URL
    obj_spider = SpiderMain() #新建爬虫类
    obj_spider.craw(root_url) #启动爬虫


# 爬虫构架
# 主程序 程序入口  spider_main.py      入口参数url
# url调度         url_manager.py      负责url存储与提供
# 页面解析        html_parser.py      解析页面 提取url title 简介
# 页面下载        html_downloader.py  根据url下载页面
# 页面输出        html_outputer.py    输出数据