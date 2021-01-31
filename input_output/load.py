from config.config import OUTPUTFILE
import json
from model.client import Client
from config.config import INPUTFILE, OUTPUTFILE

def load_files(filename=INPUTFILE):
    """
    Loader
    """
    # Todo:
    # - Open the filename
    # - Store the clients
    # - Store the loaded transactions
    # - Write the expected output
    clients = {}
    clients_loaded_ids = {}
    output = open(OUTPUTFILE,'w')
    with open(INPUTFILE) as file:
        data = file.readlines()
        print(len(data))

    output.close()