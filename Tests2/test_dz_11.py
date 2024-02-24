import pytest  
from dz_11.Date import Date  


@pytest.mark.parametrize("input_data, expected_output",
                         [
                             ("2022.10.15", "2022.10.15"),
                             ("2000.1.1", "2000.1.1"),
                             ("1999.12.31", "1999.12.31"),
                             ("2023.5.20", "2023.5.20"),
                             ("1980.11.25", "1980.11.25"),
                             ("1975.7.4", "1975.7.4"),
                             ("1658.1.17", "1658.1.17")
                         ]) 
def test_input_date(input_data, expected_output, mocker):
    mocker.patch('builtins.input', return_value=input_data)
    date_obj = Date()
    date_obj.input_date()
    assert str(date_obj) == expected_output 



@pytest.mark.parametrize("year, month, day", [
    (2022, 10, 31),
    (2000, 2, 29),
    (1999, 13, 1)
])
def test_date_init(year, month, day):
    d = Date(year, month, day)
    assert d.year == year
    assert d.month == month
    assert d.day == day


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


@pytest.mark.parametrize("year, month, day, expected", [
    (2019, 2, 29, False),
    (2020, 2, 29, True),
    (2021, 4, 31, False),
    (2022, 12, 32, False),
])
def test_date_validate(year, month, day, expected):
    date = Date(year, month, day)
    assert date.validate() == expected
