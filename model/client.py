from config.config import MAXDAILYLOAD, MAXDAILYTRANSACTIONS, MAXWEEKLYLOAD
from model.koho_date import Date


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
        self.last_load_date = Date()


    def is_daily_load_exceeded(self, load_amount):
        """
        """
        if (load_amount >  MAXDAILYLOAD) or \
            (self.daily_accum_loads >= MAXDAILYTRANSACTIONS) or \
            (MAXDAILYLOAD - self.currentweek_load_ammount < load_amount) :
            return True
        return False

    def is_weekly_load_exceeded(self, load_amount):
        """
        """
        if (load_amount >  MAXWEEKLYLOAD) or \
            (MAXWEEKLYLOAD - self.currentday_load_ammount < load_amount) :
            return True
        return False

    def update_daily_load(self, load_amount):
        """
        """
        self.currentday_load_ammount += load_amount
        self.daily_accum_loads += 1

    
    def update_weekly_load(self, load_amount):
        """
        """
        self.currentweek_load_ammount += load_amount

    
    def init_new_day(self, load_date):
        """
        Add initiate a new day in case the date changed
        """

    def load_transaction(self, load_amount, load_date):
        """
        Evaluates the business rules and executes the new load case possible
        """
    




