import pytest  
from dz_11.Date import Date  


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def display_date(self):
        return f"{self.day}.{self.month}.{self.year}"


@pytest.mark.parametrize("year, month, day, expected_output",
                         [(2022, 10, 31, "31.10.2022"),
                          (2000, 1, 1, "1.1.2000"),
                          (2023, 12, 25, "25.12.2023")])
def test_display_date(year, month, day, expected_output):
    date = Date(year, month, day)
    assert date.display_date() == expected_output