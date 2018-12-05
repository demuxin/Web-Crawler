# coding:utf-8
'''
页面下载模块
下载网页HTML代码并转换为UTF-8格式
'''
# urllib模块
import urllib.request

class HtmlDownloader(object):

    def download(self, url):

        if url is not None:
            try:
                # Python3，加上超时检测
                request = urllib.request.urlopen(url, timeout = 10)
                if request.getcode() == 200:
                    # return request.read().decode("utf-8")
                    return request.read()
                else:
                    return None

            except Exception as err:
                print(str(err))
        else:
            return None


# requests模块 用这个方法输出乱码
# import requests
#
# class HtmlDownloader(object):
#
#     def download(self, url):
#         if url is None:
#             return None
#
#         response = requests.get(url)
#
#         if response.status_code != 200:
#             return None #请求失败
#         else:
#             return response.text #返回下载好的内容