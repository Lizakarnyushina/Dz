from datetime import datetime
from dz_11.date import Date

class DateStamp(Date):
    def __init__(self, day=None, month=None, year=None):
        now = datetime.now()
        self.day = day if day is not None else now.day
        self.month = month if month is not None else now.month
        self.year = year if year is not None else now.year