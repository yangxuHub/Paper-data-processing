import redis
import json
import csv

if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    # 获取paper key
    resp = r.keys('*')
    diff = r.keys('model.pdf*')
    meta = r.keys('model.meta*')
    # diff = list(set(resp).difference(meta))
    # papers单位
    i = 0
    path = "section1.csv"
    with open(path, 'w', encoding='utf-8') as f:
        csv_write = csv.writer(f)
        for line in diff:
            i = i + 1
            paper = r.hgetall(line)
            body_text = json.loads(paper['body_text'])
            id = paper["paper_id"]
            # text
            # try:
            #     print(paper["acl_id"])
            for text in body_text:
                print(text['section'])
                data_row = [id, text['section']]
                csv_write.writerow(data_row)
