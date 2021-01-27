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

        