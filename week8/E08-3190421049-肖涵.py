import requests
from bs4 import BeautifulSoup
import re
import demjson
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import wordcloud
import itertools

header={
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

#爬取网页
def spider(url):
    print("正在解析网页...........")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')
    parseText = soup.body
    # print(parseText)
    # 定义查找正则表达式，series:开头，中间任意匹配，}\);结尾的文本，后边多一个?表示懒惰模式
    pattern = re.compile(r"series:(.*?)}\);", re.MULTILINE | re.DOTALL)
    # compile 函数用于编译正则表达式，生成一个 Pattern 对象
    # 正则表达式匹配查找，group(0) 是获取取得的字符串整体，group(1)是取出括号里面我们要匹配的内容
    languageRank = pattern.search(str(parseText)).group(1)
    languageRank = languageRank.replace('\n', '').replace('\r', '').replace(" ", "").replace("\t", "")
    # 定义替换正则表达式，series:开头，中间任意匹配，}\);结尾的文本
    languageRank = languageRank.replace('Date.UTC(', '"').replace(')', '"')
    jsonRank = demjson.decode(languageRank)
    return jsonRank


def PieChart(josnrank):
    print("-------------正在展示各语言最新占比饼图-------------\n")
    labels=[]
    rate=[]
    plt.rcParams['font.sans-serif'] = ['SimHei']
    for json in josnrank:
        labels.append(json.get("name"))
        rate.append(json.get("data")[-1][1])
    plt.figure(figsize=(15, 8))
    plt.title('各语言最新占比图')
    plt.pie(x=rate,labels = labels,autopct = '%.1f%%')
    plt.legend( fontsize=10, bbox_to_anchor=(1.1, 1.05), borderaxespad=0.3)
    plt.show()


def LineChartOverTheYears(josnrank):
    print("-------------正在展示各语言历年占比变化图-------------\n")
    labels = []
    rate = []
    labelss=[]
    plt.rcParams['font.sans-serif'] = ['SimHei']
    fig=plt.figure(figsize=(15,8))
    plt.xlabel("TIME")
    plt.ylabel("RATE(%)")
    for i,json in enumerate(josnrank):
        labels.append([])
        rate.append([])
        # labels.append(json.get("name"))
        datas=json.get("data")
        for data in datas:
            labels[i].append([data[0]])
            rate[i].append(data[1])
        import itertools
        labels[i] = list(itertools.chain.from_iterable(labels[i]))
        # labels[i] = [str(i) for i in labels]
        # labelss.append("".join(labels))
        # labelss = list(map(int, labels))
        x=range(len(rate[i]))
        plt.plot(labels[i], rate[i],label=json.get("name"))
        plt.legend()

    plt.title('各语言历年占比变化图')
    ax = fig.add_subplot(111)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(base=12))
    plt.xticks(rotation=60)
    plt.show()


def ChangeInProportionTrend(josnrank):
    print("-------------正在展示各语言较之去年同期占比趋势变化图-------------\n")
    labels = []
    rate = []
    plt.figure(figsize=(15, 8))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False#解决坐标轴负号显示问题
    plt.title('各语言较之去年同期占比趋势变化图')
    for json in josnrank:
        labels.append(json.get("name"))
        ratee=(json.get("data")[-1][1]-json.get("data")[-13][1])/json.get("data")[-13][1]*100
        rate.append(ratee)
        plt.bar(json.get("name"), ratee, label=json.get("name"))  # tick_label=rate,
        plt.xticks(rotation=60)
    plt.xlabel("LANUAGE")
    plt.ylabel("CHANGE%)")
    plt.legend()
    plt.show()


def WordCloud(josnrank):
    print("-------------正在展示各语言占比所成词云-------------\n")
    word=[]
    for json in josnrank:
        cnt=int(json.get("data")[-1][1]*100)
        lable=json.get("name")
        for i in range(0,cnt):
            word.append(lable)
    txt = ",".join(word)
    w = wordcloud.WordCloud( \
        width=800, height=600, background_color="white",
        max_words=15,
        collocations=False
    )
    w.generate(txt)
    plt.imshow(w)
    plt.axis('off')  # 是否显示坐标轴
    plt.show()


def FunctionChoice():
    print("展示功能列表：")
    print("1.展示各语言最新占比饼图")
    print("2.展示各语言历年占比变化图")
    print("3.展示各语言较之去年同期占比趋势变化图")
    print("4.展示各语言占比所成词云\n")


def main():
    url="https://www.tiobe.com/tiobe-index/"
    jsonRank=spider(url)
    FunctionChoice()
    PieChart(jsonRank)
    LineChartOverTheYears(jsonRank)
    ChangeInProportionTrend(jsonRank)
    WordCloud(jsonRank)
    print("-------------展示结束-------------")
if __name__ == '__main__':
    main()

