from dz_11.date import Date

class DateStamp(Date):
    def __init__(self, day=None, month=None, year=None):
        self.day = day
        self.month = month
        self.year = year
