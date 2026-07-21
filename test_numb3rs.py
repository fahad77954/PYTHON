from numb3rs import validate

def test_numb3rs_ok():
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("192.15.3.0") == True

def test_numb3rs_not_ok():
    assert validate("-1.1.1.1") == False
    assert validate("257.255.255.255") == False
    assert validate("255.257.255.255") == False
    assert validate("0.0.257.0") == False
    assert validate("192.15.3.257") == False

def test_numb3rs_not_ok_invalid():
    assert validate("cat") == False
    assert validate("257") == False
    assert validate("255.257") == False
    assert validate("0.0.2") == False
    assert validate("192.15.3.255.16") == False
