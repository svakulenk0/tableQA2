# -*- coding: utf-8 -*-
'''
author: svakulenko
2 Aug 2017
'''

from elasticsearch import Elasticsearch

from load_csv import load_csv
from settings import *
from mappings import ngram_tokenizer


def rows2ES(file_name, index_name, limit=2, mapping={}):
    '''
    Loads a table from the CSV file to the ES index row by row along with the heading within the row,
    i.e. row is a document to search for.

    limit <int> number of rows to process
    '''

    es = Elasticsearch()

    # reset index
    try:
        es.indices.delete(index=index_name)
        es.indices.create(index=index_name, body=mapping)
    except Exception as e:
        print e

    header, rows = load_csv(file_name)
    row_strs = []
    if limit:
        rows = rows[:limit]
    for i, row in enumerate(rows):
        row_str = ""
        for j, cell in enumerate(row):
            # recursively append cells with headers
            row_str = "%s %s %s" % (row_str, header[j], cell)
        row_str = row_str.lower().strip()
        print row_str

        # write row to ES index
        es.index(index=index_name, doc_type=DOC_TYPE_ROWS, id=i,
                 body={'content': row_str})


def test_rows2ES():
    rows2ES(SAMPLE_CSV_FILE, INDEX_NAME_ROWS)


def test_custom_mapping():
    rows2ES(SAMPLE_CSV_FILE, INDEX_NAME_ROWS, mapping=ngram_tokenizer)


def cells2ES(file_name, index_name, limit=None, mapping={}):
    '''
    Loads a table from the CSV file to the ES index row by row along with the heading within the row,
    i.e. row is a document to search for.

    limit <int> number of rows to process
    '''

    es = Elasticsearch()

    # reset index
    try:
        es.indices.delete(index=index_name)
    except Exception as e:
        print e
    es.indices.create(index=index_name, body=mapping)

    header, rows = load_csv(SAMPLE_CSV_FILE)
    rows.insert(0, header)
    if limit:
        rows = rows[:limit]
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            # lowercase text value
            cell = cell.lower()
            print "row %s column %s value %s" % (i, j, cell)

            # write cell to ES index
            try:
                es.index(index=index_name, doc_type=DOC_TYPE_CELLS,
                         body={'row': i, 'column': j, 'content': cell})
            except:
                print cell


def test_cells2ES():
    # cells2ES(SAMPLE_CSV_FILE, INDEX_NAME_CELLS, mapping={})
    cells2ES(SAMPLE_CSV_FILE, INDEX_NAME_CELLS, mapping=ngram_tokenizer, limit=2)


def index_whole_dataset():
    cells2ES(SAMPLE_CSV_FILE, INDEX_NAME_CELLS, mapping=ngram_tokenizer)


if __name__ == '__main__':
    index_whole_dataset()
