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
    
    customer_loaded_ids = {}
    clients = {}
    output = open(OUTPUTFILE,'w')
    with open(INPUTFILE) as file:
        lines = file.readlines()
        for i in range(len(lines)):
            loaded_data = json.loads(lines[i])
            transaction_id = loaded_data["id"]
            customer_id = loaded_data["customer_id"]
            transaction_ammount = float(loaded_data["load_amount"][1::])
            transaction_date = loaded_data["time"][0:10]
            if customer_id not in customer_loaded_ids:
                customer_loaded_ids[customer_id] = set()
            
            dic = {}
            if transaction_id not in customer_loaded_ids[customer_id]:
                customer_loaded_ids[customer_id].add(transaction_id)
                if customer_id not in clients:
                    client = Client(customer_id)
                    clients[customer_id] = client
                else:
                    client = clients[customer_id]
                
                if client.load_transaction(transaction_ammount, transaction_date):
                    dic["accepted"]=True
                else:
                    dic["accepted"]=False
                dic["id"] = transaction_id
                dic["customer_id"] = customer_id

                if i == len(lines)-1:
                    output.write(json.dumps(dic))
                else:
                    output.write(json.dumps(dic)+'\n')
            
            print('Processing line: {} '.format(i+1))

        

    output.close()