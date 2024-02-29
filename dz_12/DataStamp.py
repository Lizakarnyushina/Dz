from datetime import datetime

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return f"{self.day}-{self.month}-{self.year}"

class DateStamp(Date):
    def __init__(self, day=None, month=None, year=None):
        now = datetime.now()
        self.day = day if day is not None else now.day
        self.month = month if month is not None else now.month
        self.year = year if year is not None else now.year