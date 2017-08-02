# -*- coding: utf-8 -*-
'''
author: svakulenko
2 Aug 2017
'''

from elasticsearch import Elasticsearch

from settings import *

QUESTIONS = ['what is the population of linz?',
             'what is the immigration in linz?',
             'what is the internal_mig_immigration of linz?']


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


def test_search_rows_w_qs(questions=QUESTIONS):
    for question in questions:
        print question
        results = search_rows(INDEX_NAME, question)
        # print results
        print results['hits']['hits'][0]['_score']
        print results['hits']['hits'][0]['_source']['row']
        print '\n'


if __name__ == '__main__':
    test_search_rows_w_qs()
