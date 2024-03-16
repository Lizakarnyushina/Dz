class Date:
    def __init__(self, year=1, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day
        if not self.validate():
            raise ValueError("Некорректная дата при создании объекта")
 

    def input_date(self):
        year, month, day = map(int, input("Введите дату ГГГГ.ММ.ДД: ").split('.'))
        self.year = year
        self.month = month
        self.day = day
        if not self.validate():
            raise ValueError ("Некорректная дата при создании объекта")
 

    def __str__(self):
        return f"{self.year}.{self.month}.{self.day}"
    
    def __repr__(self):
        return f"{self.year}.{self.month}.{self.day}"
 

    def validate(self):
        if self.year < 1 or self.month < 1 or self.month > 12 or self.day < 1:
            return False
 
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            max_day = 31
        elif self.month in [4, 6, 9, 11]:
            max_day = 30
        else:
            if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
                max_day = 29
            else:
                max_day = 28
 
        if self.day > max_day:
            return False
 
        return True
    

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day


    def __ne__(self, other):
        return not self.__eq__(other)


    def __add__(self, other):
        new_year = self.year + other.year
        new_month = self.month + other.month
        new_day = self.day + other.day

        while new_month > 12:
            new_year += 1
            new_month -= 12

        while new_day > 28:  
            max_day = 31 if new_month in [1, 3, 5, 7, 8, 10, 12] else 30
            if new_month == 2:
                max_day = 29 if (new_year % 4 == 0 and new_year % 100 != 0) or new_year % 400 == 0 else 28

            if new_day > max_day:
                new_day -= max_day
                new_month += 1
                if new_month > 12:
                    new_year += 1
                    new_month = 1

        return Date(new_year, new_month, new_day)

    def __sub__(self, other):
        new_year = self.year - other.year
        new_month = self.month - other.month
        new_day = self.day - other.day

        while new_month < 1:
            new_year -= 1
            new_month += 12

        while new_day < 1:
            new_month -= 1
            if new_month < 1:
                new_year -= 1
                new_month = 12

            max_day = 31 if new_month in [1, 3, 5, 7, 8, 10, 12] else 30
            if new_month == 2:
                max_day = 29 if (new_year % 4 == 0 and new_year % 100 != 0) or new_year % 400 == 0 else 28

            new_day += max_day

        return Date(new_year, new_month, new_day)
