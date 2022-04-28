import json
import os
import string
import csv

def get_split(s):
    try:
        content = s.split()
    except:
        content = None
    return content

if __name__ == "__main__":
    path = "./paper"
    fileList = os.listdir(path)
    for file in fileList:
        with open(path + '/' + file, 'r', encoding='utf-8') as f:
            load_dict = json.load(f)
            newdata = []
            x = -1
            try:
                for i in load_dict['document']['table']['region']['cell']:
                    x += 1
                    text = load_dict['document']['table']['region']['cell'][x]['content']
                    content = get_split(text)
                    start_row = load_dict['document']['table']['region']['cell'][x]['@start-row']
                    end_row = load_dict['document']['table']['region']['cell'][x]['@end-row']
                    start_col = load_dict['document']['table']['region']['cell'][x]['@start-col']
                    end_col = load_dict['document']['table']['region']['cell'][x]['@end-col']
                    id = x
                        # id = load_dict['document']['table']['region']['cell'][x]['@id']
                    keydict = {"id": id, "tex": text, "content": content, "start_row": start_row, "end_row": end_row, "start_col": start_col, "end_col": end_col}
                    newdata.append(keydict)
            except:
                continue

        newjson = json.dumps(newdata, indent=4, separators=(',', ': '))
        f = open(file, 'w')
        f.write(newjson)
        f.close()
