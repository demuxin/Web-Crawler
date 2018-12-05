# coding:utf-8
'''
URL 管理模块
存储URL信息，管理URL集合
防止重复抓取和循环抓取
'''
class UrlManager(object):
    def __init__(self):
        self.new_urls = set() #待爬取的url列表
        self.old_urls = set() #爬取过的url列表

    def add_new_url(self, url):
        if url is None:
            raise Exception
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            raise Exception #在调度程序中用了try except解决异常问题，用raise Exception抛出异常
        for url in urls:
            try:
                self.add_new_url(url)
            except Exception as err:
                print("add url failed：", err)
                continue #遇到为None的直接忽视

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop() #从列表中获取并移除这个URL
        self.old_urls.add(new_url)
        return new_url
