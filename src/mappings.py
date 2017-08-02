# -*- coding: utf-8 -*-
'''
author: svakulenko
2 Aug 2017
'''

ngram_tokenizer = {
                     "settings": {
                        "number_of_shards": 1,
                        "analysis": {
                           "tokenizer": {
                              "ngram_tokenizer": {
                                 "type": "nGram",
                                 "min_gram": 4,
                                 "max_gram": 4
                              }
                           },
                           "analyzer": {
                              "ngram_tokenizer_analyzer": {
                                 "type": "custom",
                                 "tokenizer": "ngram_tokenizer"
                              }
                           }
                        }
                     },
                     "mappings": {
                        "doc": {
                           "properties": {
                              "content": {
                                 "type": "text",
                                 "term_vector": "yes",
                                 "analyzer": "ngram_tokenizer_analyzer"
                              }
                           }
                        }
                     }
                  }
