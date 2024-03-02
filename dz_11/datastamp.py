from datetime import datetime
from dz_11.date import Date

class DateStamp(Date):
    def __init__(self):
        now = datetime.now()
        super().__init__(now.year, now.month, now.day)
