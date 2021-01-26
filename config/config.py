from datetime import datetime

MAXDAILYTRANSACTIONS = 3
MAXWEEKLYLOAD = 20000
MAXDAILYLOAD = 5000
INPUTFILE = "../files/input.txt"
OUTPUTFILE = "../files/output-{}.txt".format(datetime.now())