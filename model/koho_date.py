import datetime

class Date():
    """
    Creates a Date object
    """
    def __init__(self, year=1980, month=1, day=1) -> None:
        super().__init__()
        self.year = year
        self.month = month
        self.day = day
    
    def set_date(self, string):
        """
        """
        # Todo:
        # - Parse the received string into day, month, and year.
        # - Set the respective properties
    
    def dates_equal(self, other):
        """
        """
        # Todo:
        # - Compare existing date with other date
        # - Return True if they are equal and False when they are not

    def weeks_equal(self, other):
        """
        """
        # Todo:
        # - Compare existing date/week with other date/week
        # - Return True if they are equal and False when they are not
