from um import count
def test_count():
    assert count("hello um world") == 1
    assert count("um hello UM") == 2
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("um?") == 1
    assert count("hello um, how are you um") == 2
