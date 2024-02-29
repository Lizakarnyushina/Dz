import pytest
from datetime import datetime
from dz_12.DataStamp import DateStamp


@pytest.mark.parametrize("day, month, year", [
    (datetime.now().day, datetime.now().month, datetime.now().year),
    (1, 1, 2000),
])
def test_datestamp_creation(day, month, year):
    datestamp = DateStamp(day=day, month=month, year=year)
    assert datestamp.day == day
    assert datestamp.month == month
    assert datestamp.year == year