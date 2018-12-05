# coding:utf-8
'''
页面数据输出模块
将抓取的信息以MarkDown格式输出
'''
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self): #将数据输出到html文件中
        #建立一个文件的输出对象，名字为output.html，写模式，
        #python默认的编码是ascii，要转化成utf-8格式
        fout = open('output.html', 'w', encoding='utf-8')

        # 解决html文件在浏览器中乱码的问题，要在html声明中写入<meta charset='utf-8'>
        fout.write('<meta charset="utf-8">')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>") #把数据输出成一个表格形式

        for data in self.datas:
            fout.write("<tr>") #行的开始标签

            #输出每个单元格的内容
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])

            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()
