import unittest
from model.koho_date import Date


class KohoDateTest(unittest.TestCase) :
    """
    Koho_date class to evaluate date business rules and corner cases. 
    """

    def test_IsSameDate(self):
        firstDate = Date(2021, 1, 10)
        secondDate = Date(2021, 1, 12)
        comparison = firstDate.dates_equal(secondDate)
        self.assertIs(comparison, False)

        firstDate = Date(2021, 1, 10)
        secondDate = Date(2021, 1, 10)
        comparison = firstDate.dates_equal(secondDate)
        self.assertIs(comparison, True)

