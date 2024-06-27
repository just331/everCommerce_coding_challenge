# EverCommerce Coding Challenge (Prime Number Generator)
This project implements the requested functionality to generate prime numbers given a range of integers (inclusive of inputs).

## Features 
- Returns list of primes inclusive of a given range
- Handles inverse range input, e.g., input of 10 - 1 will be treated just like 1 - 10 would
- Command line interface to specify the range


## Requirements 
- Python 3.7 / higher 

## Running the project
- To run the project from the command line:
```shell
python main.py 1 10
```

## Coverage
```
Name                            Stmts   Miss  Cover   Missing
-------------------------------------------------------------
prime_generator.py                  9      0   100%
tests/__init__.py                   0      0   100%
tests/test_prime_generator.py      21      0   100%
utils.py                           11      0   100%
-------------------------------------------------------------
TOTAL                              41      0   100%

```