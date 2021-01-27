from config.config import MAXDAILYLOAD, MAXDAILYTRANSACTIONS, MAXWEEKLYLOAD

class Client():
    """
    Creates a Client object to handle all features of an account.
    Usage: myclient = Client(client_ID)
    """
    def __init__(self, client_ID):
        self.client_id = client_ID
        self.daily_accum_loads = 0
        self.currentday_load_ammount = 0
        self.currentweek_load_ammount = 0



