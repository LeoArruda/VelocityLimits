import unittest
from model.client import Client
from model.koho_date import Date

class ClientTest(unittest.TestCase) :
    """
    Client_test class to evaluate Client's business rules. 
    """
    def test_DailyLoadInTheSameDay(self):
        """
        """
        client = Client(1)
        test_date = Date(2020, 7, 2)
        client.last_load_date = test_date
        client.currentday_load_ammount = 2000
        client.daily_accum_loads = 1
        loading_date = "2020-07-02"
        client.init_new_day(loading_date)

        self.assertEqual(client.last_load_date.day, test_date.day)
        self.assertEqual(client.last_load_date.month, test_date.month)
        self.assertEqual(client.last_load_date.year, test_date.year)
        self.assertEqual(client.currentday_load_ammount, 2000)
        self.assertEqual(client.daily_accum_loads, 1)
