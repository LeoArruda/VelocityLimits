from datetime import datetime

MAXDAILYTRANSACTIONS = 3
MAXWEEKLYLOAD = 20000
MAXDAILYLOAD = 5000
INPUTFILE = "./data/input.txt"
OUTPUTFILE = "./data/output-{}.txt".format(datetime.now())