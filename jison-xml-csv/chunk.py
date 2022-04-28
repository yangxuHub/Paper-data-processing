import json
import os
import string
import csv


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
                    pos1 = load_dict['document']['table']['region']['cell'][x]['bounding-box']['@x1']
                    pos2 = load_dict['document']['table']['region']['cell'][x]['bounding-box']['@x2']
                    pos3 = load_dict['document']['table']['region']['cell'][x]['bounding-box']['@y1']
                    pos4 = load_dict['document']['table']['region']['cell'][x]['bounding-box']['@y2']
                    pos = [pos1, pos2, pos3, pos4]
                    text = load_dict['document']['table']['region']['cell'][x]['content']
                    keydict = {"pos": pos, "text": text}
                    newdata.append(keydict)
            except:
                continue

        newjson = json.dumps(newdata, indent=4, separators=(',', ': '))
        f = open(file, 'w')
        f.write(newjson)
        f.close()

