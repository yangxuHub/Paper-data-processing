# 词频统计
import csv
import re
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
with open("./guanjianzi.txt", encoding="UTF-8") as f:
    text = f.read()

    speech = text.lower().split()

    from collections import Counter

    wd = Counter(speech)
    # wd.most_common(10)
    # 去除停用词
    for sw in stop_words:
        del wd[sw]
    print(wd.most_common(100))
    path = "guanjianzi.csv"
    with open(path, 'w+t', encoding='utf-8') as f:
        csv_write = csv.writer(f)
        data_row = wd.most_common(1000)
        csv_write.writerow(data_row)
    #   正则表达式
    #     word = f.read()
        for strs in data_row:
            pattern = re.compile(r"[A-Za-z]")
            result = pattern.findall(str(strs))
            with open("paixu.txt", 'a', encoding='utf-8') as fp:
                fp.writelines(result)
                fp.writelines(",")

#    liebiao
    with open("test.txt", 'r', encoding='utf-8') as f:
        p = f.read()
        # 测试
        # 从网络上拷贝的一段英文，实现分隔。当不是分隔符时，认为是一个单词。
        # 需要定义一个变量来记录单词的开始
        words = []  # 建立一个空列表
        index = 0  # 遍历所有的字符
        start = 0  # 记录每个单词的开始位置
        while index < len(p):  # 当index小于p的长度
            start = index  # start来记录位置
            while p[index] != " " and p[index] not in [","]:  # 若不是空格，点号，逗号
                index += 1  # index加一
                if index == len(p):  # 若遍历完成
                    break  # 结束
            words.append(p[start:index])
            if index == len(p):
                break
            while p[index] == " " or p[index] in [","]:
                index += 1
                if index == len(p):
                    break

        print(words)
        with open("liebiao.txt", 'a', encoding='utf-8') as fp:
            fp.write(words)

