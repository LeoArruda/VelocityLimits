from config.config import OUTPUTFILE
import json
from model.client import Client
from config.config import INPUTFILE, OUTPUTFILE

def load_files(filename=INPUTFILE) -> None:
    """
    This function reads the param filename and iterates every row.
    It the transactions from each row, eavaluate against the business rules, and saves 
    the results into the output file.
    :param filename: string input filename.
    :return: None.
    """
    # auxiliary dictionaries to control
    # transactions and clients loaded
    customer_loaded_ids = {}
    clients = {}
    # open/create the output file.
    output = open(OUTPUTFILE,'w')
    with open(INPUTFILE) as file:
        lines = file.readlines()
        for i in range(len(lines)):
            loaded_data = json.loads(lines[i])
            transaction_id = loaded_data["id"]
            customer_id = loaded_data["customer_id"]
            transaction_ammount = float(loaded_data["load_amount"][1::])
            transaction_date = loaded_data["time"][0:10]

            # Create a dictionay to build the output record
            output_dictionary = {}

            if customer_id not in customer_loaded_ids:
                customer_loaded_ids[customer_id] = set()
            
            # Evaluate and ensure we're only loading unique transactions
            if transaction_id not in customer_loaded_ids[customer_id]:
                customer_loaded_ids[customer_id].add(transaction_id)
                if customer_id not in clients:
                    client = Client(customer_id)
                    clients[customer_id] = client
                else:
                    client = clients[customer_id]

                # Build a new output record into out dictionary
                output_dictionary["id"] = transaction_id
                output_dictionary["customer_id"] = customer_id
                if client.load_transaction(transaction_ammount, transaction_date):
                    output_dictionary["accepted"]=True
                else:
                    output_dictionary["accepted"]=False
                
                # Write/Append the output file
                if i == len(lines)-1:
                    output.write(json.dumps(output_dictionary))
                else:
                    output.write(json.dumps(output_dictionary)+'\n')


    output.close()