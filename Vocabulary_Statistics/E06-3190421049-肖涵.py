import jieba
import os
import matplotlib.pyplot as plt
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

excludes = {'the', 'of', 'and', 'is', 'to', 'following', 'be', 'in', 'must', 'for', 'given', 'if', 'then', 'with', 'by',
            'on', 'from', 'int', 'one'}


def getpdffile():
    rootpath = os.walk(os.getcwd())
    fileList = []
    for path, d, filelist in rootpath:
        for filename in filelist:
            if filename.endswith('pdf'):
                fileList.append(filename)
    return fileList


def readpdf(file_path):
    txt = ''
    fp = open(file_path, 'rb')
    praser = PDFParser(fp)
    doc = PDFDocument()
    praser.set_document(doc)
    doc.set_parser(praser)
    doc.initialize()

    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            # 这里layout是一个LTPage对象,里面存放着这个page解析出的各种对象,一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal等等
            # 想要获取文本就获得对象的text属性
            for out in layout:
                if hasattr(out, 'get_text'):
                    txt += out.get_text()
    txt = txt.lower()
    return txt


def txttoword(txt):
    txt = "".join(i for i in txt if ord(i) < 256)
    words = jieba.lcut(txt)
    return words


def countword(fileList):
    counts = {}
    for path in fileList:
        orgtxt = readpdf(path)  # 将pdf中txt读取
        words = txttoword(orgtxt)  # 将txt中的词汇分词，并放入数组
        for word in words:
            if len(word) == 1:
                continue
            elif word == "nodes":
                rword = "node"
            else:
                rword = word
            counts[rword] = counts.get(rword, 0) + 1
        for word in excludes:
            del counts[word]
        items = list(counts.items())
        items.sort(key=lambda x: x[1], reverse=True)
    print('当前文件目录下共有' + str(len(fileList)) + '份试卷，经统计，将试卷中考点热频词汇统计如下：')
    for i in range(10):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))
    return items


def showhistogram(items):
    word_list = []
    count_list = []
    for i in range(10):
        word, count = items[i]
        word_list.append(word)
        count_list.append(count)
    x = list(range(len(word_list)))
    plt.bar(x, count_list, label='TestPoint', tick_label=word_list, fc='lightblue')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    fileList = getpdffile()  # 自定义getpdffile()方法获取当前目录下所有.pdf后缀的文件的路径，存放在fileList
    items = countword(fileList)  # 遍历pdf文件，获取gettext(),进行考点词频统计
    showhistogram(items)  # 绘制柱状图展示考点频率