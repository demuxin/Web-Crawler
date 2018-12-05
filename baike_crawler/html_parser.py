# coding:utf-8
'''
页面解析模块
产生新的URL链接
获取词条名称和信息
'''
from bs4 import BeautifulSoup
import re
import urllib.parse #---python3

class HtmlParser(object):

    # 获取出来链接放入新URL库
    def _get_new_urls(self, page_url, soup):
        new_urls = set() #空集合
        # URL结构：/item/xxx
        # .*：贪婪模式   .*?：懒惰模式
        links = soup.find_all('a', href = re.compile(r"/item/(.*)")) #获得新网页内所有RUL，也可以"/item/(*?)"
        for link in links:
            new_url = link['href']
            #将new_url按照page_url的格式拼接成一个新的URL
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {} #存放数据

        #把url也放入最终的数据中，方便使用
        res_data['url'] = page_url

        # 标题：<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_ = "lemmaWgt-lemmaTitle-title").find("h1")
        # if title_node is not None:
        #     res_data['title'] = title_node.get_text()
        res_data['title'] = title_node.get_text()

        # 简介：<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_ = "lemma-summary")
        # 在这加一个判断语句有一个问题，就是如果判断为否，没有加入键'summary'，
        # 但是在output_html()中仍然会输出它，就会出现错误：KeyError：'summary'
        # if summary_node is not None:
        #     res_data['summary'] = summary_node.get_text()
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        # soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
