import pytest  
from dz_11.date import Date  


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


@pytest.mark.parametrize("year, month, day, expected_exception", [
    (2022, 2, 29, ValueError),
    (2021, 2, 28, None),
    (2000, 2, 29, None),
    (1999, 4, 31, ValueError),
])
def test_valid_date(year, month, day, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            Date(year, month, day)
    else:
        date = Date(year, month, day)
        assert date.year == year
        assert date.month == month
        assert date.day == day


@pytest.mark.parametrize("year, month, day, expected_exception", [
    (2022, 2, 29, ValueError),
    (2021, 2, 28, None),
    (2000, 2, 29, None),
    (1999, 4, 31, ValueError),
])
def test_invalid_date(year, month, day, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            Date(year, month, day)
    else:
        date = Date(year, month, day)
        assert date.year == year
        assert date.month == month
        assert date.day == day


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


@pytest.mark.parametrize("date1, date2, expected", [
    (Date(2022, 1, 1), Date(2022, 1, 1), True),
    (Date(2022, 1, 1), Date(2022, 1, 2), False),
    (Date(2022, 1, 1), Date(2023, 1, 1), False),
])
def test_eq(date1, date2, expected):
    assert (date1 == date2) == expected


@pytest.mark.parametrize("date1, date2, expected", [
    (Date(2022, 1, 1), Date(2022, 1, 1), False),
    (Date(2022, 1, 1), Date(2022, 1, 2), True),
    (Date(2022, 1, 1), Date(2023, 1, 1), True),
])
def test_ne(date1, date2, expected):
    assert (date1 != date2) == expected


@pytest.mark.parametrize("date1, date2, expected", [
        (Date(2022, 1, 1), Date(1, 1, 1), Date(2023, 2, 2)),
        (Date(2022, 1, 1), Date(3, 1, 7), Date(2025, 2, 8)),
        (Date(1012, 1, 31), Date(1012, 1, 31), Date(2024, 4, 2)),
        (Date(1011, 1, 31), Date(1012, 1, 31), Date(2023, 4, 3)),
    ])
def test_add(date1, date2, expected):
    result = date1 + date2
    assert (result.year, result.month, result.day) == (expected.year, expected.month, expected.day)

@pytest.mark.parametrize("date1, date2, expected", [
        (Date(2022, 2, 2), Date(2021, 1, 1), Date(1, 1, 1)),
        (Date(2022, 2, 2), Date(1, 1, 1), Date(2021, 1, 1)),
    ])
def test_sub(date1, date2, expected):
    result = date1 - date2
    assert (result.year, result.month, result.day) == (expected.year, expected.month, expected.day)
