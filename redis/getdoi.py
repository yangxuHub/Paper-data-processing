import redis
import json
import csv
# 爬虫id获取
if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    # 获取paper key
    resp = r.keys('*')
    meta = r.keys('model.meta*')
    # diff = list(set(resp).difference(meta))
    # papers单位1
    i = 0
    # json格式
    # with open('test.json', 'w') as file_obj:
    # csv write
    path = "cc3.csv"
    with open(path, 'w', encoding='utf-8') as f:
        csv_write = csv.writer(f)
        csv_head = ["S2orc_id", "title", "id", "doi", "acl_id", "arxiv_id","mag_id"]
        csv_write.writerow(csv_head)
        for line in meta:
            print('-------------------------------------%d-------------------------------------'%i)
            # print(line)
            i = i + 1
            paper = r.hgetall(line)
            title = paper["title"]
            id = paper["paper_id"]
            try:
                doi = paper["doi"]
            except KeyError:
                doi = None
            try:
                mag_id = paper["mag_id"]
                mag = paper['mag_field_of_study']
                if mag != "[\"Computer Science\"]":
                    mag_id = None
            except KeyError:
                mag_id = None
            try:
                acl_id = paper["acl_id"]
            except KeyError:
                acl_id = None
            try:
                arxiv_id = paper["arxiv_id"]
            except KeyError:
                arxiv_id = None
            if mag_id or acl_id or arxiv_id:
                data_row = [line, title, id, doi, acl_id, arxiv_id, mag_id]
                csv_write.writerow(data_row)
                print(data_row)
            else:
                print("0")
