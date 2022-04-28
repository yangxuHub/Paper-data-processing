# json提取有用表格
import json
import os
import string
import csv

#     # 获取json中包含的所有键（包括嵌套字典）
# def key_json(xml_str):
#     # parse是的xml解析器
#     key_list = []
#     for key in xml_str.keys():
#         if type(xml_str[key]) == type({}):
#             key_json(xml_str[key])
#         key_list.append(key)
#     print(key_list)
#     return key_list
def find_string(s):
    t = ['F1', 'f1', 'Recall', 'Accuracy', 'Precision', 'AP', 'macro-F1', 'Methods', 'Model', 'IgnF1']
    result = False
    for i in range(0, 9):
        if s==t[i]:
            result = True
            break
        # result = t.find(s) >= 0
    return result
    # try:
    #     string.index(t , str(s))
    #     return True
    # except(ValueError):
    #     return False

if __name__ == "__main__":
    path = "./paper"
    fileList = os.listdir(path)
    out = "table_clean.csv"
    with open(out, 'w', encoding='utf-8') as f:
        csv_write = csv.writer(f)
        csv_head = ["paper_id", "table"]
        csv_write.writerow(csv_head)
        for file in fileList:
            table = []
            print(file + ':')
            with open(path + '/' + file, 'r') as f:
                xml_str = json.load(f)
                # data = key_json(xml_str)
                # i是table
                for i in range(0, 20):
                    try:
                        content = xml_str['document']['table'][i]['region']
                    except:
                        break
                    for j in range(0, 200):
                        try:
                            content = xml_str['document']['table'][i]['region']['cell'][j]['content']
                        except:
                            break
                        # print(content)
                        if find_string(content):
                            print(content)
                            table.append(i + 1)
                            data_row = [file, table, content]
                            csv_write.writerow(data_row)
                            print(file, table)

                            # 一旦满足条件就转到下一个table
                            break

