from project import get_currency, get_capital, get_language

def test_get_currency():
    assert get_currency("Albania") == "Lek"
    assert get_currency("Bangladesh") == "Taka"


def test_get_capital():
    assert get_capital("Albania") == "Tirane"
    assert get_capital("Bangladesh") == "Dhaka"


def test_get_language():
    assert get_language("Albania") == "Albanian"
    assert get_language("Bangladesh") == "Bangla"
