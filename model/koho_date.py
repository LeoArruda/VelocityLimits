from datetime import datetime

class Date():
    """
    Creates a Date object
    """
    def __init__(self, year=1980, month=1, day=1) -> None:
        super().__init__()
        self.day = day
        self.month = month
        self.year = year
    

    def set_date(self, date_string):
        """
        """
        # Todo:
        # - Parse the received string into day, month, and year.
        # - Set the respective properties
        self.day = int(date_string[8:10])
        self.month = int(date_string[5:7])
        self.year = int(date_string[0:4])
        

    def dates_equal(self, other):
        """
        """
        # Todo:
        # - Compare existing date with other date
        # - Return True if they are equal and False when they are not
        day = self.day == other.day
        month = self.month == other.month
        year = self.year == other.year
        if day and month and year:
            return True
        return False


    def weeks_equal(self, other):
        """
        """
        day = datetime(self.year, self.month, self.day)    
        other_day = datetime(other.year, other.month, other.day)
        return day.isocalendar()[1] == other_day.isocalendar()[1]

    
    def toString(self):
        return "{}-{}-{}".format(self.year, self.month, self.day)


