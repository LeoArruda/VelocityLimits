import unittest
from model.client import Client
from model.koho_date import Date

class ClientTest(unittest.TestCase) :
    """
    Client_test class to evaluate Client's business rules. 
    """
    def setUp(self):
        self.client = Client(1)
        self.test_date = Date(2021, 1, 12)
        self.client.last_load_date = self.test_date
        self.client.currentday_load_ammount = 2000
        self.client.daily_accum_loads = 1


    def test_DailyLoadInTheSameDayCase(self):
        """
        Test case to evaluate if the loads are in the same day. 
        """
        loading_date = "2021-01-12"
        self.client.init_new_day(loading_date)
        # Case 1: The dates are equal
        self.assertEqual(self.client.last_load_date.day, self.test_date.day)
        self.assertEqual(self.client.last_load_date.month, self.test_date.month)
        self.assertEqual(self.client.last_load_date.year, self.test_date.year)
        self.assertEqual(self.client.currentday_load_ammount, 2000)
        self.assertEqual(self.client.daily_accum_loads, 1)


    def test_DailyLoadInDifferentDaysCase(self):
        """
        Test case to evaluate if the loads are in different days. 
        """
        loading_date = "2021-01-13"
        self.client.init_new_day(loading_date)
        # Case 1: The dates are equal
        self.assertEqual(self.client.last_load_date.day, 13)
        self.assertEqual(self.client.last_load_date.month, 1)
        self.assertEqual(self.client.last_load_date.year, 2021)
        self.assertEqual(self.client.currentday_load_ammount, 0)
        self.assertEqual(self.client.daily_accum_loads, 0)


    def test_FirstTimeLoadCase(self):
        """
        Test case to evaluate the first time load. 
        """
        loading_date = "2021-01-13"
        self.client.currentday_load_ammount = 0
        self.client.daily_accum_loads = 0
        self.client.init_new_day(loading_date)
        self.assertEqual(self.client.last_load_date.day, 13)
        self.assertEqual(self.client.last_load_date.month, 1)
        self.assertEqual(self.client.last_load_date.year, 2021)
        self.assertEqual(self.client.currentday_load_ammount, 0)
        self.assertEqual(self.client.daily_accum_loads, 0)

    
    def test_UpdateDailyTansactionsLoadsCase(self):
        """
        Test case to evaluate an update value into the client's load_ammount
        exceeding the daily limit. 
        """
        self.client.currentday_load_ammount = 4000
        self.client.daily_accum_loads = 4
        self.client.update_daily_load(1500)
        # Test the load ammount and accumulator numbers
        self.assertEqual(self.client.is_daily_load_exceeded(1000), True)


    def test_UpdateDailyAmmountLoadsCase(self):
        """
        Test case to evaluate an update value into the client's load_ammount. 
        """
        self.client.update_daily_load(1500)
        # Test the load ammount and accumulator numbers
        self.assertEqual(self.client.currentday_load_ammount, 3500)
        self.assertEqual(self.client.daily_accum_loads, 2)


    def test_UpdateDailyAmmountLoadsSuccessCase(self):
        """
        Test case to evaluate an update value into the client's load_ammount
        exceeding the daily limit. 
        """
        # Test if load ammount exceeds the daily limits
        self.assertEqual(self.client.is_daily_load_exceeded(3000), False)

    
    def test_UpdateDailyAmmountLoadsExceededCase(self):
        """
        Test case to evaluate an update value into the client's load_ammount
        exceeding the daily limit. 
        """
        # Test if load ammount exceeds the daily limits
        self.assertEqual(self.client.is_daily_load_exceeded(3100), True)

    
    def test_UpdateDailyAmmountLoadsCase(self):
        """
        Test case to evaluate an update value into the client's load_ammount
        exceeding the daily limit. 
        """
        # Test if load ammount exceeds the daily limits
        self.assertEqual(self.client.is_daily_load_exceeded(2500), False)


    def test_UpdateDailyAccumLoadExceedCase(self):
        """
        Test case to evaluate an update value into the client's load_ammount
        exceeding the daily transactions limit. 
        """
        self.client.currentday_load_ammount = 2000
        self.client.daily_accum_loads = 1
        # Test if load ammount exceeds the daily limits
        self.assertEqual(self.client.is_daily_load_exceeded(3001), True)


    def test_UpdateWeeklyAccumLoadExceedCase(self):
        """
        Test case to evaluate an update value into the client's load_ammount
        exceeding the weekly limit. 
        """
        self.client.currentweek_load_ammount = 11000
        # Test if load ammount exceeds the daily limits
        self.assertEqual(self.client.is_weekly_load_exceeded(11000), True)


    def test_UpdateWeeklyAccumLoadNotExceedCase(self):
        """
        Test case to evaluate an update value into the client's load_ammount
        not exceeding the weekly limit. 
        """
        self.client.currentweek_load_ammount = 11000
        # Test if load ammount exceeds the daily limits
        self.assertEqual(self.client.is_weekly_load_exceeded(9000), False)
    

    def test_LoadTransactionsSeveralDay(self):
        """
        Test case to evaluate the update of several transactions client's records.
        This is a more comprehensive test case, covering same day scenarios, different days,
        different weeks and several different ammounts. 
        """
        client = Client(2)
        # First Load
        self.assertEqual(client.load_transaction(3000,"2021-01-03"), True)
        # Overloading in the same day
        self.assertEqual(client.load_transaction(2500,"2021-01-03"), False)
        # Underloading in the same day
        self.assertEqual(client.load_transaction(500,"2021-01-03"), True)
        # checking the 3rd load with ammount 0
        self.assertEqual(client.load_transaction(0,"2021-01-03"), True)
        # checking the 4th load with ammount 0
        self.assertEqual(client.load_transaction(0,"2021-01-03"), False)
        # checking the load into the next day
        self.assertEqual(client.load_transaction(7000,"2021-01-04"), False)
        # checking the load into the following days in the same week
        self.assertEqual(client.load_transaction(5000,"2021-01-05"), True)
        self.assertEqual(client.load_transaction(5000,"2021-01-06"), True)
        self.assertEqual(client.load_transaction(5000,"2021-01-07"), True)
        self.assertEqual(client.load_transaction(5000,"2021-01-08"), True)
        # checking the overload into the same week
        self.assertEqual(client.load_transaction(5000,"2021-01-08"), False)
        # checking the load into the following days in the same week
        self.assertEqual(client.load_transaction(5000,"2021-01-09"), True)


    
    


        

