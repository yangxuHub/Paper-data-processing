import redis
import json
import csv

if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    # 获取paper key
    resp = r.keys('*')
    meta = r.keys('meta*')
    diff = list(set(resp).difference(meta))
    # papers单位
    i = 0
    # json格式
    # with open('test.json', 'w') as file_obj:
    # csv write
    path = "a.csv"
    with open(path, 'w', encoding='utf-8') as f:
        csv_write = csv.writer(f)
        csv_head = ["line", "cite", "bib", "txt", "link"]
        csv_write.writerow(csv_head)
        for line in diff:
            i = i + 1
            print('-------------------------------------%d-------------------------------------'%i)
            print(line)
            paper = r.hgetall(line)
            body_text = json.loads(paper['body_text'])
            bib_entries = json.loads(paper['bib_entries'])
            # abstract choose
            abstract = json.loads(paper['abstract'])
            # text
            for text in body_text:
                for cite in text['cite_spans']:
                    print(cite)
                    csv_write = csv.writer(f)
                    # link id
                    try:
                        ref_id = cite['ref_id']
                        bib = bib_entries[ref_id]
                        data_row = [line, cite, ref_id, text['text'], bib['link']]
                    # 没有对应bib字典
                    except KeyError:
                        data_row = [line, cite, ref_id, text['text'], ]
                    csv_write.writerow(data_row)
                    # json.dump(text['text']+"\n",file_obj)