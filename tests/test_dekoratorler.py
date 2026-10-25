from uzay_oyunu.dekoratorler import sure_olc

@sure_olc
def ornek_fonksiyon(a: int, b: int = 0) -> int:
    """Örnek bir toplama fonksiyonu."""
    return a + b

def test_sure_olc_sonuc_degismiyor():
    assert ornek_fonksiyon(3, 4) == 7

def test_sure_olc_adli_arguman():
    assert ornek_fonksiyon(a=5, b=10) == 15

def test_sure_olc_isim_belge_korunuyor():
    assert ornek_fonksiyon.__name__ == "ornek_fonksiyon"
    assert ornek_fonksiyon.__doc__ == "Örnek bir toplama fonksiyonu."