class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    
    def input_date(cls):
        year = int(input("Введите год: "))
        month = int(input("Введите месяц: "))
        day = int(input("Введите день: "))
        return cls(year, month, day)


    def display_date(self):
        print("Дата: {self.day}.{self.month}.{self.year}")