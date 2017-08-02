## Baseline

Load table to ES row by row along with the header labels (also apply lowercasing)

e.g. CSV table:

['NUTS2', 'LAU2_CODE', 'LAU2_NAME', 'YEAR', 'INTERNAL_MIG_IMMIGRATION', 'INTERNATIONAL_MIG_IMMIGRATION', 'IMMIGRATION_TOTAL', 'INTERNAL_MIG_EMIGRATION', 'INTERNATIONAL_MIG_EMIGRATION', 'EMIGRATION_TOTAL']
['AT31', '40101', 'Linz', '2015', '9693', '6583', '16276', '9994', '3171', '13165']

becomes ES document:

nuts2 at31 lau2_code 40101 lau2_name linz year 2015 internal_mig_immigration 9693 international_mig_immigration 6583 immigration_total 16276 internal_mig_emigration 9994 international_mig_emigration 3171 emigration_total 13165


## Baseline results

what is the population of linz?  

0.2824934  

nuts2 at31 lau2_code 40101 lau2_name linz year 2015 internal_mig_immigration 9693 international_mig_immigration 6583 immigration_total 16276 internal_mig_emigration 9994 international_mig_emigration 3171 emigration_total 13165


what is the immigration in linz?  

0.2824934  

nuts2 at31 lau2_code 40101 lau2_name linz year 2015 internal_mig_immigration 9693 international_mig_immigration 6583 immigration_total 16276 internal_mig_emigration 9994 international_mig_emigration 3171 emigration_total 13165


what is the internal_mig_immigration of linz?  

0.5649868  

nuts2 at31 lau2_code 40101 lau2_name linz year 2015 internal_mig_immigration 9693 international_mig_immigration 6583 immigration_total 16276 internal_mig_emigration 9994 international_mig_emigration 3171 emigration_total 13165
