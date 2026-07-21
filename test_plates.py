from plates import is_valid


def test_length():
    assert is_valid("C") == False
    assert is_valid("ABCDEFG") == False


def test_valid_plates():
    assert is_valid("CS") == True
    assert is_valid("CS50") == True
    assert is_valid("CSBSE") == True


def test_numbers():
    assert is_valid("CS50A") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50000000") == False


def test_beginning_alphabetical():
    assert is_valid("1CS") == False
    assert is_valid("0A") == False
    assert is_valid("5") == False
    assert is_valid("A1") == False
    assert is_valid("1A") == False


def test_alphanumeric():
    assert is_valid("CS.5") == False
    assert is_valid("CS 5") == False
    assert is_valid("CS-5") == False
