# Software Testing using Unittest

This project is designed for learning how to use Python's `unittest` framework for testing various algorithms and functions. It provides a hands-on approach to practicing writing and running unit tests, helping you understand how to test your Python code effectively. The tests cover a wide range of functionalities including basic string manipulation, mathematical functions, and more.

## Test Coverage

| Name                                      | Stmts | Miss | Cover |
|-------------------------------------------|-------|------|-------|
| main_code\alternating_cha_HR.py           | 6     | 0    | 100%  |
| main_code\caesar_cipher_HR.py            | 12    | 0    | 100%  |
| main_code\fizzbuzz.py                     | 9     | 0    | 100%  |
| main_code\funny_string_HR.py             | 12    | 0    | 100%  |
| main_code\grid_challenge_HR.py            | 7     | 0    | 100%  |
| main_code\number.py                       | 6     | 0    | 100%  |
| main_code\staircase.py                    | 5     | 0    | 100%  |
| main_code\two_cha_HR.py                   | 10    | 0    | 100%  |
| tests\test_alternating_cha_HR_utils.py   | 43    | 0    | 100%  |
| tests\test_caesar_cipher_HR_utils.py     | 78    | 0    | 100%  |
| tests\test_fizzbuzz_utils.py             | 47    | 0    | 100%  |
| tests\test_funny_string_HR.py            | 43    | 0    | 100%  |
| tests\test_grid_challenge_HR_utils.py    | 43    | 0    | 100%  |
| tests\test_number_utils.py               | 39    | 0    | 100%  |
| tests\test_staircase_utils.py            | 64    | 0    | 100%  |
| tests\test_two_cha_HR_utils.py           | 51    | 0    | 100%  |
| **TOTAL**                                 | **475**| **0** | **100%** |


## Usage
```bash
nose2 -v --with-coverage
```
## Run
To run tests for a specific file, use
```bash
python -m unittest -v .\tests\test_[filename].py
```
Alternatively, to run all tests with coverage
```bash
nose2 -v --with-coverage
```