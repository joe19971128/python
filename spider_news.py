import requests
import random
from bs4 import BeautifulSoup
import os








class News():
    def __init__(self, url):
        # 请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"
        }
        self.url = url

    def request(self):
        # 解析
        self.r = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.r.text, "html.parser")
        # 图片（迭代）
        self.news_pic = self.soup.select('div[id="Content"] img')
        # 内容（迭代）
        self.news_body = self.soup.find("div", id="Content").find_all("p")
        # 标题
        self.news_title = self.soup.find("div", id="lft-art").find("h1").text

    def makedir(self):
        # 创建目录
        # 标题前五个单词作为文件名
        self.path = os.getcwd() + "/" + " ".join(self.news_title.split(" ")[:5])
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            print("mkDir Ok")
        else:
            print("Dir is Exists")
        os.chdir(self.path)

    def save(self):
        # 保存
        for i in self.news_pic:
            img_url = i['src']
            img = requests.get(img_url, headers=self.headers)
            with open(self.news_title + str(random.randint(1,100)) + ".jpeg", "wb")as f:
                f.write(img.content)
                print("img Ok")
                f.close()
        content = ""
        for i in self.news_body:
            content += i.text.strip() + "\n"
        with open(self.news_title + ".txt", "w")as f:
            f.write(content)
            print("content Ok")
            f.close()

    def enter(self):
        self.request()
        self.makedir()
        self.save()

    def __str__(self):
        return "python3.5爬取新闻页"





a = News("http://www.chinadaily.com.cn/a/201804/30/WS5ae66975a3105cdcf651b44c.html")
a.enter()
print(a)

