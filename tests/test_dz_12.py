import pytest
from freezegun import freeze_time
from dz_11.datastamp import DateStamp

@pytest.mark.parametrize("day, month, year", [
    (1, 1, 2022),
    (None, 1, 2022),
    (1, None, 2022),
    (None, None, 2022),
    (None, None, None)
])
@freeze_time("2022-01-01")
def test_datestamp_creation(day, month, year):
    ds = DateStamp(day=day, month=month, year=year)
    assert ds.day == day if day is not None else 1
    assert ds.month == month if month is not None else 1
    assert ds.year == year if year is not None else 2022
