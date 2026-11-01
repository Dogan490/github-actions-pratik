
from hesap_makinesi import toplama, cikarma, carpma, bolme


# Toplama testi
def test_toplama():
    assert toplama(5, 3) == 8


# Çıkarma testi
def test_cikarma():
    assert cikarma(10, 4) == 6


# Çarpma testi
def test_carpma():
    assert carpma(5, 4) == 20


# Bölme testi
def test_bolme():
    assert bolme(10, 2) == 5
