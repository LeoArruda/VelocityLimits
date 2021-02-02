# The Challenge

In finance, it's common for accounts to have so-called "velocity limits". In this task, you'll write a program that accepts or declines attempts to load funds into customers' accounts in real-time.

Each attempt to load funds will come as a single-line JSON payload, structured as follows:

```json
{ "id": "1234", "customer_id": "1234", "load_amount": "$123.45", "time": "2018-01-01T00:00:00Z" }
```

Each customer is subject to three limits:

- A maximum of $5,000 can be loaded per day
- A maximum of $20,000 can be loaded per week
- A maximum of 3 loads can be performed per day, regardless of amount

As such, a user attempting to load $3,000 twice in one day would be declined on the second attempt, as would a user attempting to load $400 four times in a day.

For each load attempt, you should return a JSON response indicating whether the fund load was accepted based on the user's activity, with the structure:

```json
{ "id": "1234", "customer_id": "1234", "accepted": true }
```

You can assume that the input arrives in ascending chronological order and that if a load ID is observed more than once for a particular user, all but the first instance can be ignored. Each day is considered to end at midnight UTC, and weeks start on Monday (i.e. one second after 23:59:59 on Sunday).

Your program should process lines from `input.txt` and return output in the format specified above, either to standard output or a file. Expected output given our input data can be found in `output.txt`.

You're welcome to write your program in a general-purpose language of your choosing.

We value well-structured, self-documenting code with sensible test coverage. Descriptive function and variable names are appreciated, as is isolating your business logic from the rest of your code.

# Organization

The final directory organization is:  
```
.
├── Makefile
├── README.md
├── config
│   └── config.py        # Has all business rules. It can easier changed. 
├── data                 # This directory is used to store all datasets. 
│   ├── README.md
│   ├── input.txt        # File to be used as source of the transactions. 
│   ├── output.txt       # Sample file provided.
│   └── result.txt       # Results stored after processing.
├── input_output
│   └── load.py          # Method responsible to load the transactions.
├── model
│   ├── client.py        # Class and methods designed to store client's information.
│   └── koho_date.py     # Class and methods designed to handle all date information.
├── tests                # Directory used to store all test cases.
│   ├── __init__.py
│   ├── client_test.py
│   ├── io_load_test.py
│   └── koho_date_test.py
└── velocitylimits.py    # The main program.
```

# How to run the test cases.

To run the tests:

- On the program root directory, run the following command.  

```
python -m unittest discover -v -s tests -p *_test.py
```

- The expected results from the tests are: 
```
$ python -m unittest discover -v -s tests -p *_test.py
test_DailyLoadInDifferentDaysCase (client_test.ClientTest) ... ok
test_DailyLoadInTheSameDayCase (client_test.ClientTest) ... ok
test_FirstTimeLoadCase (client_test.ClientTest) ... ok
test_LoadTransactionsSeveralDay (client_test.ClientTest) ... ok
test_UpdateDailyAccumLoadExceedCase (client_test.ClientTest) ... ok
test_UpdateDailyAmmountLoadsCase (client_test.ClientTest) ... ok
test_UpdateDailyAmmountLoadsExceededCase (client_test.ClientTest) ... ok
test_UpdateDailyAmmountLoadsSuccessCase (client_test.ClientTest) ... ok
test_UpdateDailyTansactionsLoadsCase (client_test.ClientTest) ... ok
test_UpdateWeeklyAccumLoadExceedCase (client_test.ClientTest) ... ok
test_UpdateWeeklyAccumLoadNotExceedCase (client_test.ClientTest) ... ok
test_LoadAndCompareResultsCase (io_load_test.IOLoad_Test) ... ok
test_InitDateCase (koho_date_test.KohoDateTest) ... ok
test_IsSameDateCase (koho_date_test.KohoDateTest) ... ok
test_SameWeekCase (koho_date_test.KohoDateTest) ... ok

----------------------------------------------------------------------
Ran 15 tests in 0.045s

OK
```


# How to use
- On the program root directory, run the following command.  

```
python velocitylimits.py
```