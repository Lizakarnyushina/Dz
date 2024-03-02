from datetime import datetime
from dz_11.date import Date

class DateStamp(Date):
    def __init__(self):
        now = datetime.now()
        self.day = now.day
        self.month = now.month
        self.year = now.year
