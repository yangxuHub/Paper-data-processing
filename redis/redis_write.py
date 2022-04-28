import redis
import json
# 显示引用link对应id
if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    # print(r.keys())
    resp = r.hgetall("['paper', 'paper_14884315', 'arxiv_1206.6418']")
    body_text = json.loads(resp['body_text'])
    bib_entries = json.loads(resp['bib_entries'])
    # for line in bib_entries:
    #     bib = bib_entries[line]
    #     print(line, bib['link'])
    BIB = 0
    try:
        while 1:
            print(bib_entries['BIBREF%d' % BIB])
            BIB = BIB + 1
    except KeyError:
        BIB = BIB + 1
