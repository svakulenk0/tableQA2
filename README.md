## Approach

1. Load table to ES row by row along with the header labels (also apply lowercasing)

e.g. CSV table:

['NUTS2', 'LAU2_CODE', 'LAU2_NAME', 'YEAR', 'INTERNAL_MIG_IMMIGRATION', 'INTERNATIONAL_MIG_IMMIGRATION', 'IMMIGRATION_TOTAL', 'INTERNAL_MIG_EMIGRATION', 'INTERNATIONAL_MIG_EMIGRATION', 'EMIGRATION_TOTAL']
['AT31', '40101', 'Linz', '2015', '9693', '6583', '16276', '9994', '3171', '13165']

becomes ES document:

nuts2 at31 lau2_code 40101 lau2_name linz year 2015 internal_mig_immigration 9693 international_mig_immigration 6583 immigration_total 16276 internal_mig_emigration 9994 international_mig_emigration 3171 emigration_total 13165

2. Tokenize documents: 1)Word Tokenizer (standard analyzer); 2)Ngram Tokenizer (4 character-level ngrams, e.g. inte, nter, tern, erna, etc.).

3. Question => Find relevant cells => row, column => Look up the Answer


## Row search results

1. **Word Tokenizer**


what is the **population** of linz?  

0.2824934  

nuts2 at31 lau2_code 40101 lau2_name linz year 2015 internal_mig_immigration 9693 international_mig_immigration 6583 immigration_total 16276 internal_mig_emigration 9994 international_mig_emigration 3171 emigration_total 13165

<br>

what is the **immigration** in linz?  

0.2824934  

nuts2 at31 lau2_code 40101 lau2_name linz year 2015 **internal_mig_immigration** 9693 **international_mig_immigration** 6583 **immigration_total** 16276 internal_mig_emigration 9994 international_mig_emigration 3171 emigration_total 13165

<br>

what is the **internal_mig_immigration** of linz?  

0.5649868  

nuts2 at31 lau2_code 40101 lau2_name linz year 2015 **internal_mig_immigration** 9693 international_mig_immigration 6583 immigration_total 16276 internal_mig_emigration 9994 international_mig_emigration 3171 emigration_total 13165


2. **Ngram Tokenizer**


what is the population of linz?  

2.2908065  

nuts2 at31 lau2_code 40101 lau2_name linz year 2015 internal_mig_immigration 9693 international_mig_immigration 6583 immigration_total 16276 internal_mig_emigration 9994 international_mig_emigration 3171 emigration_total 13165

<br>

what is the immigration in linz?  

4.328201  

nuts2 at31 lau2_code 40101 lau2_name linz year 2015 internal_mig_immigration 9693 international_mig_immigration 6583 immigration_total 16276 internal_mig_emigration 9994 international_mig_emigration 3171 emigration_total 13165

<br>

what is the internal_mig_immigration of linz?  

8.121933  

nuts2 at31 lau2_code 40101 lau2_name linz year 2015 internal_mig_immigration 9693 international_mig_immigration 6583 immigration_total 16276 internal_mig_emigration 9994 international_mig_emigration 3171 emigration_total 13165


## Cell search results

1. **Word Tokenizer**

what is the internal_mig_immigration in linz?  

1.2039728  

row 0 column 4 value internal_mig_immigration  

1.2039728  

row 1 column 2 value linz  

Answer: row 1 column 4 value 9693

2. **Ngram Tokenizer**

what is the population of linz?  

4.081641  

row 1 column 2 value linz  

Answer: Not found


what is the immigration in linz?  

7.168558  

row 0 column 6 value immigration_total  

4.081641  

row 1 column 2 value linz  

Answer: row 1 column 6 value 16276


what is the internal_mig_immigration in linz?  

15.177296  

row 0 column 4 value internal_mig_immigration  

4.081641  

row 1 column 2 value linz  

Answer: row 1 column 4 value 9693


## References

* [An Introduction to Ngrams in Elasticsearch. 2015.](https://qbox.io/blog/an-introduction-to-ngrams-in-elasticsearch)
