import csv
import string

out = open('five2.csv', 'w', newline='')
csv_writer = csv.writer(out, dialect='excel')

def combine(ss):
    end = []
    e = ""
    l = ''
    for s in ss:
        if s == ','or s== '[' or s == '\'' or s == ']':
            l = s
            continue
        if s == ' ':
            if l != '\'':
                l = s
                continue
            else:
                end.append(e)
                e = ""
        else:
            e = e + s
        l = s
    return end
#
# ss = [' ', '7', '6', ' ', 'W', 'S', 'J', ' ', 'n', 'u', 'l', 'l', ' ', 'n', 'u', 'l', 'l', ' ', 'n', 'u', 'l', 'l', ' ', '1', '9', '9', '6', '8', '1', '4', ' ', '1', '9', '9', '6', '8', '1', '4']
# print(combine(ss))


f = open("222.txt", "r")
dic = f.read()
print(dic)
result = []
last = ''
for data in dic:
    if data == '[' or data == '"' or data == ',':
        last = data
        continue
    if data == ' ' and last != ',':
        result.append('@')
        last = data
        continue
    if data == ']':
        res = str(result)
        print(res)
        print(combine(res))
        csv_writer.writerow(combine(res))
        result = []
        last = data
        continue
    last = data
    result.append(data)




    # #
    # print(result)
    #
    # line = line.replace(',', '\t')  # 将每行的逗号替换成空格
    # # list = line.split()  # 将字符串转为列表，从而可以按单元格写入csv

