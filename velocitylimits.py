from model.client import Client
from config.config import MAXDAILYLOAD, MAXDAILYTRANSACTIONS, MAXWEEKLYLOAD, INPUTFILE, OUTPUTFILE
from input_output.load import load_files

if __name__ == '__main__':
    print(INPUTFILE)
    print(OUTPUTFILE)
    load_files()