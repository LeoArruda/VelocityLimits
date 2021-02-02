import unittest
from model.koho_date import Date


class KohoDateTest(unittest.TestCase) :
    """
    Koho_date class to evaluate date business rules and corner cases. 
    """

    def test_IsSameDateCase(self):
        """
        Test case to evaluate the same day evaluation method. 
        """
        firstDate = Date(2021, 1, 10)
        secondDate = Date(2021, 1, 12)
        comparison = firstDate.dates_equal(secondDate)
        self.assertIs(comparison, False)

        firstDate = Date(2021, 1, 10)
        secondDate = Date(2021, 1, 10)
        comparison = firstDate.dates_equal(secondDate)
        self.assertIs(comparison, True)

    def test_InitDateCase(self):
        """
        Test case to evaluate the setup of a new date method. 
        """
        firstDate = Date()
        dateString = "2021-01-15"
        firstDate.set_date(dateString)
        self.assertEqual(firstDate.day, 15)
        self.assertEqual(firstDate.month, 1)
        self.assertEqual(firstDate.year, 2021)

    def test_SameWeekCase(self):
        """
        Test case to evaluate the same week evaluation method. 
        """
        firstDate = Date(2021, 1, 10)
        secondDate = Date(2021, 1, 11)
        comparison = firstDate.weeks_equal(secondDate)
        self.assertIs(comparison, False)

        firstDate = Date(2021, 1, 9)
        secondDate = Date(2021, 1, 10)
        comparison = firstDate.weeks_equal(secondDate)
        self.assertIs(comparison, True)

        firstDate = Date(2021, 1, 30)
        secondDate = Date(2021, 2, 1)
        #print("1st Date {}  :  2nd Date {} ".format(firstDate.toString, secondDate.toString))
        comparison = firstDate.weeks_equal(secondDate)
        self.assertIs(comparison, False)





