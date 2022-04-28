import json
import redis
import json
# 引文上下文文本)
if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    # create a lookup for the pdf parse based on paper ID
    paper_id_to_pdf_parse = {}
    resp = r.keys('*')
    meta = r.keys('meta*')
    diff = list(set(resp).difference(meta))
    for line in diff:
        f_pdf = r.hgetall(line)
        pdf_parse_dict = json.loads(f_pdf['body_text'])
        paper_id_to_pdf_parse[pdf_parse_dict['paper_id']] = pdf_parse_dict

    # 用元数据值过滤论文
    citation_contexts = []
    # with open('data/metadata/sample.jsonl') as f_meta:
    for line in meta:
        f_meta = r.hgetall(line)
        metadata_dict = json.loads(f_meta)
        paper_id = metadata_dict['paper_id']
        print("Currently viewing S2ORC paper: {paper_id}")

        # 假设我们只关心 ACL 选集论文
        if not metadata_dict['acl_id']:
            continue

        # 并且我们只需要解析有出站引用的论文
        if not metadata_dict['has_outbound_citations']:
            continue

        # 获取引用上下文（段落）
        if paper_id in paper_id_to_pdf_parse:
            # 从先前计算的查找字典中获取完整的 pdf 解析
            pdf_parse = paper_id_to_pdf_parse[paper_id]

            # (2) 从 pdf 解析中提取我们需要的字段，包括参考书目和文本
            bib_entries = pdf_parse['bib_entries']
            paragraphs = pdf_parse['abstract'] + pdf_parse['body_text']

            # (3) 循环段落，获取引用上下文
            for paragraph in paragraphs:

                # (4) 循环本段中的每个内联引用
                for cite_span in paragraph['cite_spans']:

                    # (5) 每个内联引用都可以解析为bib条目
                    cited_bib_entry = bib_entries[cite_span['ref_id']]

                    # (6) 该bib条目*可*链接至S2ORC纸张。如果是这样的话，抓取一段
                    linked_paper_id = cited_bib_entry['link']
                    if linked_paper_id:
                        citation_contexts.append({
                            'citing_paper_id': paper_id,
                            'cited_paper_id': linked_paper_id,
                            'context': paragraph['text'],
                            'citation_mention_start': cite_span['start'],
                            'citation_mention_end': cite_span['end'],
                        })