from twttr import shorten


def test_lowercase():
    assert shorten("twitter") == "twttr"


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"


def test_numbers():
    assert shorten("CS50") == "CS50"


def test_punctuation():
    assert shorten("What's up?") == "Wht's p?"


def test_mixed():
    assert shorten("Fahad") == "Fhd"
    assert shorten("Ali") == "l"