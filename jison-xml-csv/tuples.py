"""
S: score
M: method
M: metric
M: dataset
T: task
TDMMS tuple generator
"""

from graph.models.graph_entity import *
from py2neo import Graph, GraphService
from py2neo.ogm import *


class Generator:
    def __init__(self, uri, user, password, graph_name):
        self.repo = Repository(uri, auth=(user, password), name=graph_name)
        self.graph = Graph(uri, auth=(user, password), name=graph_name)

    def generate(self):
        """
        generate tdmms in current graph
        :return: a list of tdmms tuple
        """
        ret = set()
        cypher_query = 'match (n:CellValue)-[r:HEADER]->(header), (n)-[s:STUB]->(stub), (header)-[header_relation]-(header_related), (stub)-[stub_relation]-(stub_related) where type(header_relation) <> "HEADER" and type(header_relation) <> "SUTB" and type(stub_relation) <> "HEADER" and type(stub_relation) <> "STUB" return distinct n.value as score, header.word as header, header.corr_type as header_type, stub.word as stub, stub.corr_type as stub_type, header_related.word as header_related, header_related.corr_type as header_related_type, stub_related.word as stub_related, stub_related.corr_type as stub_related_type'
        result = self.graph.run(cypher_query)
        for record in result:
            score = record['score']
            to_be_added = [None] * 5
            to_be_added[0] = score
            header, stub, header_type, stub_type = record['header'], record['stub'], record['header_type'], record['stub_type']
            header_related, header_related_type, stub_related, stub_related_type = record['header_related'], record['header_related_type'], record['stub_related'], record['stub_related_type']
            for (w, t) in zip([header, stub, header_related, stub_related], [header_type, stub_type, header_related_type, stub_related_type]):
                for i, v in enumerate(['Method', 'Metric', 'Material', 'Task']):
                    if t == v:
                        if not to_be_added[i+1]:
                            to_be_added[i+1] = w
            ret.add(tuple(to_be_added))
        print(ret)
        print(len(ret))


if __name__ == '__main__':
    g = Generator('bolt://neo4j@localhost:7687', 'neo4j', 'lhclhc1006', 'acl-test')
    g.generate()
    print("hello")