# Rate Estimation

## Setup

Open this project on PyCharm and do the following:

1. Create and activate the virtualenv
    * **Use PyCharm** or one of the following:
        * `virtualenv --python=python3 venv`
        * `python3 -m virtualenv --python=python3 venv`
        * Note: you might have to use the complete python path.
    * Activate your virtual environment:
        * Mac/Linux: `source venv/bin/activate`
        * Windows: `source venv/Scripts/activate`

1. Install requirements
    * `pip install -r requirements.txt`
    
## Problem definition

There's a Google SpeadSheet with the following sheets:
* `METADATA`: contains the metadata for reading the other sheets.
* `CONFIG`: contains the loan configuration.
* `RATE`: contains the interest rate result.
* `RESULT`: contains the amortization table.

Given the configuration defined on `CONFIG`: 
* `PROB_OF_DEFAULT`: probability of default for the next term.
* `LGD`: loss given default, percentage. 
* `LOAN_AMOUNT`: monetary value.
* `LOAN_TERMS`: duration of the loan.
* `LOAN_MARR`: minimum acceptable rate of return.
* `CLIENT_MIN_RATE`: minimum interest rate offered to a client.
* `CLIENT_MAX_RATE`: maximum interest rate offered to a client.
* `SEARCH_SAMPLES`: number of samples to use on the search algorithm. 

Calculate the loan's interest rate such that the expected interest rate is zero and the show the resulting amortization table. 
* Add the loan's interest rate and offering decision to the `RATE` sheet.
* Add the amortization table to the `RESULT` sheet with the following columns: 
    * `t`: current term. 
    * `BALANCE`: amount that is still owed (exposure at default).
    * `PRINCIPAL`: monetary value representing the principal payment. 
    * `INTEREST`: monetary value representing the interest payment. 
    * `ANNUITY`: annuity
    * `IRR`: internal rate of return
    * `EL`: expected loss
    * `PROB`: probability of scenario.
    
## Use cases

Activate your virtualenv to run the following commands. 

Setup the connection with Google Drive: 

```commandline
$ python main.py setup
```

Run a loan-request process on local mode: 

```commandline
$ python main.py loan-request-local \
    --loan-amount=10000 \
    --loan-marr=0.15 \
    --loan-terms=5 \
    --probability-of-default=0.20 \
    --loss-given-default=0.50 \
    --client-min-rate=0.06 \
    --client-max-rate=0.75 \
    --search-samples=100 \
    --save example.csv \
    --show
```

Expected output: 

```text
Loan request for 10000 due in 5 terms with 3919.15 fix payments and interest rate of 27.61% : Approved
   t   BALANCE  PRINCIPAL  INTEREST  ANNUITY   IRR       EL  PROB
0  0 10,000.00        nan       nan      nan  0.00 1,000.00  0.20
1  1  8,841.83   1,158.17  2,760.98 3,919.15 -0.61   884.18  0.16
2  2  7,363.90   1,477.94  2,441.22 3,919.15 -0.15   736.39  0.13
3  3  5,477.91   1,885.99  2,033.16 3,919.15  0.09   547.79  0.10
4  4  3,071.20   2,406.71  1,512.44 3,919.15  0.21   307.12  0.08
5  5      0.00   3,071.20    847.95 3,919.15  0.28     0.00  0.33
```

Run a loan-request process from/into Google Drive: 

```commandline
$ python main.py loan-request-cloud --sheet-id 10RVyxDjdchzcl_BmjmpODC7t43P9OAKaCdY69jxa3XM --show
```

Example output: 

```text
Loan request for 10000.0 due in 5 terms with 3919.14 fix payments and interest rate of 27.61% : Approved
   t   BALANCE  PRINCIPAL  INTEREST  ANNUITY   IRR       EL  PROB
0  0 10,000.00        nan       nan      nan  0.00 1,000.00  0.20
1  1  8,841.83   1,158.17  2,760.97 3,919.14 -0.61   884.18  0.16
2  2  7,363.89   1,477.94  2,441.20 3,919.14 -0.15   736.39  0.13
3  3  5,477.90   1,885.99  2,033.15 3,919.14  0.09   547.79  0.10
4  4  3,071.19   2,406.71  1,512.43 3,919.14  0.21   307.12  0.08
5  5      0.00   3,071.19    847.95 3,919.14  0.28     0.00  0.33
```
