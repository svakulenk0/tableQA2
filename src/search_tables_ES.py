# -*- coding: utf-8 -*-
'''
author: svakulenko
2 Aug 2017
'''

from elasticsearch import Elasticsearch

from settings import *

QUESTIONS = ['what is the population of linz?',
             'what is the immigration in linz?',
             'what is the internal_mig_immigration of linz?']  # correct answer: 9693

class ESConnection():
    def __init__(self, index_name, doc_type):
        '''
        establish connection to ES index
        '''
        self.es = Elasticsearch()
        self.index_name = index_name
        self.doc_type = doc_type

    def search_tables(self, question, explain=False):
        results = self.es.search(index=self.index_name, body={"query": {"match": {"content": question}}}, doc_type=self.doc_type, explain=explain)['hits']['hits']
        return results

    def lookup(self, row, column, explain=False):
        results = self.es.search(index=self.index_name, q="column:%s AND row:%s"%(column, row), doc_type=self.doc_type, explain=explain)['hits']['hits']
        return results


def test_search_tables():
    question = 'what is the population of linz?'
    results = search_rows(INDEX_NAME, question)
    # print results
    print results['hits']['hits'][0]['_source']['row']
    print results['hits']['hits'][0]['_score']


def test_search_tables_w_qs(questions=QUESTIONS, index_name=INDEX_NAME_CELLS, doc_type=DOC_TYPE_CELLS):
    es = ESConnection(index_name, doc_type)

    for question in questions:
        print question
        i, j = None, None

        results = es.search_tables(question)
        for result in results:
            # print result
            print result['_score']

            value = result['_source']['content']
            row = result['_source']['row']
            column = result['_source']['column']
            print "row %s column %s value %s" % (row, column, value)

            # hit the header
            if row == 0:
                j = column
            # hit the row
            else:
                i = row
            # look up the cell value with the answer

        # found row and column pointers
        if i and j:
            results = es.lookup(i, j)
            # show top result cell content as the final answer
            print results[0]['_source']['content']

        print '\n'


if __name__ == '__main__':
    test_search_tables_w_qs()
