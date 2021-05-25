import jieba
import requests
from bs4 import BeautifulSoup
import re
# excludes = {搜狐 首页 新闻 体育 汽车 房产 旅游 教育 时尚科技 财经 娱乐 更 多 母婴 健康 历史 军事 美食 文化 星座 专题 游戏 搞笑 动漫 宠物given','if','then','with','by','on','from',''}
website=["https://www.sohu.com/a/454127097_100135484?scm=1019.s000a.v1.0&spm=smpc.ch1001.fd-news.4.1614922478138dzs5whx",
         "https://www.sohu.com/a/453447958_351928?scm=1019.s000a.v1.0&spm=smpc.fb-cba-home.content1-n-2.1.1614921426496vsncorl",
         "https://www.sohu.com/a/453435357_461606?scm=1019.s000a.v1.0&spm=smpc.fb-cba-home.content1-n-2.2.1614921225212vdzbdjk",
         "https://www.sohu.com/a/451835289_351928?scm=1019.s000a.v1.0&spm=smpc.fb-cba-home.content1-n-2.4.1614921225212vdzbdjk"
]
header={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
def Keyword():
    print("请输入要查询的关键字,例如“篮球”,“易建联”,“东莞”:")
    keyword=input()
    return keyword
def spider(website,keyword):
    counts={}
    wordd=[]
    for i,url in enumerate(website):
        rep = requests.get(url, headers=header,)
        rep.encoding = 'utf-8'
        soup=BeautifulSoup(rep.text)
        content=re.sub(r"\s+","",soup.get_text())#re是正则的表达式,sub是substitute表示替换
        words = jieba.lcut(content)

        wordd.append([])
        cnt=0
        for word in words:
            wordd[i].append(word)
            if word == keyword:
                cnt += 1
        counts[i] = cnt

    return counts,wordd

if __name__ == '__main__':
    keyword=Keyword()

    counts,words=spider(website,keyword)

    items = list(counts.items())

    items.sort(key=lambda x: x[1], reverse=True)

    print("以下显示关键词 "+keyword+" 的出现次数:")

    for item in items:
        print(website[item[0]])
        print("新闻摘要: ",end='')
        for i in range(0,10):
            print(str(words[item[0]][i]),end='')
        print("……\n"+keyword+"出现次数:"+str(item[1])+'\n')





