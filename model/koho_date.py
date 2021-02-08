from datetime import datetime

class Date():
    """
    Date object to handle all method and evaluations for date tests
    Usage: mydate = Client()
    :param None: .
    :return: Object.
    """
    def __init__(self, year=1980, month=1, day=1) -> None:
        super().__init__()
        self.day = day
        self.month = month
        self.year = year
    

    def set_date(self, date_string):
        """
        Method to set a new day.
        :param date_string: String date.
        :return: None.
        """
        self.day = int(date_string[8:10])
        self.month = int(date_string[5:7])
        self.year = int(date_string[0:4])
        

    def dates_equal(self, other):
        """
        Method to compare dates.
        :param other: Object date.
        :return: Boolean.
        """
        day = self.day == other.day
        month = self.month == other.month
        year = self.year == other.year
        if day and month and year:
            return True
        return False


    def weeks_equal(self, other):
        """
        Method to compare Weeks.
        :param other: Object date.
        :return: Boolean.
        """
        day = datetime(self.year, self.month, self.day)    
        other_day = datetime(other.year, other.month, other.day)
        return day.isocalendar()[1] == other_day.isocalendar()[1]

    
    def toString(self):
        """
        Method to parse the object date property into string format.
        :return: String.
        """
        return "{}-{}-{}".format(self.year, self.month, self.day)


