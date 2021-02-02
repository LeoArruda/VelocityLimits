from config.config import MAXDAILYLOAD, MAXDAILYTRANSACTIONS, MAXWEEKLYLOAD
from model.koho_date import Date


class Client():
    """
    Client object to handle all features of an account.
    Usage: myclient = Client(1)
    :param filename: string input filename.
    :return: None.
    """
    def __init__(self, client_id):
        self.client_id = client_id  # Client Unique ID
        self.daily_accum_loads = 0  # Accumulator to increase at every transaction
        self.currentday_load_ammount = 0  #  Accumulate the load ammount value daily
        self.currentweek_load_ammount = 0 # Accumulate the load ammount value weekly
        self.last_load_date = Date() # Register the last date


    def is_daily_load_exceeded(self, load_amount):
        """
        Method to evaluate the occurence of a bigger load amount
        than the business rules for Daily Maximum Load Amount
        :param load_amount: float input.
        :return: Boolean.
        """
        #print('Max Daily Load : {}  Load Ammount : {}  calc: {}'.format(MAXDAILYLOAD, load_amount,(MAXDAILYLOAD - self.currentweek_load_ammount)))
        if (load_amount >  MAXDAILYLOAD) or \
            (self.daily_accum_loads >= MAXDAILYTRANSACTIONS) or \
            (MAXDAILYLOAD - self.currentday_load_ammount < load_amount):
            return True
        return False


    def is_weekly_load_exceeded(self, load_amount):
        """
        Method to evaluate the occurence of a bigger load amount
        than the business rules for Weekly Maximum Load Amount
        :param load_amount: float input.
        :return: Boolean.
        """
        #print('Max Week Load : {}  Load Ammount : {}'.format(MAXWEEKLYLOAD, load_amount))
        if (load_amount >  MAXWEEKLYLOAD) or \
           (MAXWEEKLYLOAD - self.currentweek_load_ammount < load_amount): 
            return True
        return False


    def update_daily_load(self, load_amount):
        """
        Method to update the daily load amount and counter.
        :param load_amount: float input.
        :return: None.
        """
        self.currentday_load_ammount += load_amount
        self.daily_accum_loads += 1

    
    def update_weekly_load(self, load_amount):
        """
        Method to update the weekly load amount and counter.
        :param load_amount: float input.
        :return: None.
        """
        self.currentweek_load_ammount += load_amount

    
    def init_new_day(self, load_date):
        """
        Method to evaluate the load date and initiate the a new day and a
        new week.
        :param load_date: String date.
        :return: None.
        """
        date = Date()
        date.set_date(load_date)
        if not self.last_load_date.dates_equal(date): # Evaluates if it is a new day
            self.currentday_load_ammount = 0
            self.daily_accum_loads = 0
            if not self.last_load_date.dates_equal(date): # Evaluates if it is a new week
                self.currentweek_load_ammount = 0
            self.last_load_date = date


    def load_transaction(self, load_amount, load_date):
        """
        Method to initiate a new day, evaluate the Business rules,
        and update Client transaction loads.
        :param load_amount: Float amount.
        :param load_date: String date.
        :return: Boolean.
        """
        self.init_new_day(load_date)
        daily_exceeded = self.is_daily_load_exceeded(load_amount)
        weekly_exceeded = self.is_weekly_load_exceeded(load_amount)
        if not daily_exceeded and not weekly_exceeded: # Evaluates the load doesn't exceed the limits 
            self.update_daily_load(load_amount)
            self.update_weekly_load(load_amount)
            return True
        return False

    
    




