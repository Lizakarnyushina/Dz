import pytest  
from dz_11.Date import Date  


@pytest.mark.parametrize("input_data, expected_output", [
    ("2022.10.15", "2022.10.15"),
    ("2000.1.1", "2000.1.1"),
    ("1999.12.31", "1999.12.31"),
    ("2023.5.20", "2023.5.20"),
    ("1980.11.25", "1980.11.25"),
    ("1975.7.4", "1975.7.4"),
    ("1658.1.17", "1658.1.17")
])
def test_input_date(monkeypatch, input_data, expected_output):
    monkeypatch.setattr('builtins.input', lambda _: input_data)
    date = Date()
    date.input_date()
    assert str(date) == expected_output


@pytest.mark.parametrize("year, month, day", [
    (2022, 1, 1),
    (2023, 12, 31),
    (2021, 6, 15),
])
def test_init_valid_date(year, month, day):
    obj = Date(year, month, day)
    assert obj.year == year
    assert obj.month == month
    assert obj.day == day
    assert obj.output is None
    assert obj.validate() is True


@pytest.mark.parametrize("year, month, day", [
    (2021, 2, 28),
    (2000, 2, 29),
])
def test_init_valid_leap_year_dates(year, month, day):
    date = Date(year, month, day)
    assert date.year == year
    assert date.month == month
    assert date.day == day
    assert date.validate() is True


@pytest.mark.parametrize("year, month, day, expected_exception", [
    (2022, 2, 29, ValueError),
    (1999, 4, 31, ValueError),
])
def test_init_invalid_date(year, month, day, expected_exception):
    with pytest.raises(expected_exception):
        Date(year, month, day)


@pytest.mark.parametrize("year, month, day, expected_output", 
                         [ 
                             (2022, 10, 15, "2022.10.15"), 
                             (2000, 1, 1, "2000.1.1"), 
                             (1999, 12, 31, "1999.12.31"),
                             (2023, 5, 20, "2023.5.20"),
                             (1980, 11, 25, "1980.11.25"),
                             (1975, 7, 4, "1975.7.4")
                         ]) 
def test_str_method(year, month, day, expected_output): 
    date_obj = Date(year, month, day) 
    assert str(date_obj) == expected_output


@pytest.mark.parametrize("year, month, day, expected_output", [
    (2021, 2, 28, True),
    (2020, 2, 29, True),
    (2020, 12, 31, True)
])
def test_validate(year, month, day, expected_output):
    instance = Date(year, month, day)
    assert instance.validate() == expected_output
