import pytest
from freezegun import freeze_time
from datetime import datetime
from dz_11.datastamp import DateStamp

@pytest.mark.parametrize("test_date", [
    ("2022-01-01", 1, 1, 2022),
    ("2023-05-15", 15, 5, 2023),
    ("2024-12-31", 31, 12, 2024),
])
def test_datestamp_initialization(test_date):
    frozen_date, expected_day, expected_month, expected_year = test_date
    with freeze_time(frozen_date):
        datestamp = DateStamp()
        assert datestamp.day == expected_day
        assert datestamp.month == expected_month
        assert datestamp.year == expected_year
