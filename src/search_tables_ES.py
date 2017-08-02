# -*- coding: utf-8 -*-
'''
author: svakulenko
2 Aug 2017
'''

from elasticsearch import Elasticsearch

from settings import *


def search_rows(index_name, question, explain=True):
    es = Elasticsearch()

    results = es.search(index=index_name, body={"query": {"match": {"row": question}}}, doc_type=DOC_TYPE, explain=explain)
    return results


def test_search_rows():
    question = 'what is the population of linz?'
    results = search_rows(INDEX_NAME, question)
    # print results
    print results['hits']['hits'][0]['_source']['row']
    print results['hits']['hits'][0]['_score']


if __name__ == '__main__':
    test_search_rows()
