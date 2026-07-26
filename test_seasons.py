from seasons import convert


def test_zero_days():
    assert convert(0) == "Zero minutes"


def test_one_day():
    assert convert(1) == "One thousand, four hundred forty minutes"


def test_two_days():
    assert convert(2) == "Two thousand, eight hundred eighty minutes"


def test_one_year():
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"


def test_two_years():
    assert convert(730) == "One million, fifty-one thousand, two hundred minutes"
