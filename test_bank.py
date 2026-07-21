from bank import value

def test_bank():
    assert value("CS5o") == 100
def test_bank_100():
    assert value("hello") == 0
def test_bank_20():
    assert value("hey") == 20
def test_bank_100():
    assert value("Hello") == 0
def test_bank_20():
    assert value("Hey") == 20


