import pytest
from datetime import datetime
from freezegun import freeze_time
from dz_11.datastamp import DateStamp

@pytest.mark.parametrize("year, month, day", [
    (2022, 12, 1),
    (2023, 5, 15),
])
def test_datestamp_init(year, month, day):
    with freeze_time(f"{year}-{month}-{day}"):
        datestamp = DateStamp()
        assert datestamp.year == year
        assert datestamp.month == month
        assert datestamp.day == day
