from uzay_oyunu.dekoratorler import sure_olc, say

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


from uzay_oyunu.dekoratorler import say

@say
def deneme_fonksiyonu() -> int:
    """Sayaç testi için boş fonksiyon."""
    return 1

def test_say_dekoratoru():
    deneme_fonksiyonu()
    deneme_fonksiyonu()
    deneme_fonksiyonu()
    assert deneme_fonksiyonu.cagri == 3 


import pytest
from uzay_oyunu.oyun import yakit_harca

def test_sinirla_sinir_degerleri():
    assert yakit_harca(0) == 100
    assert yakit_harca(100) == 0
    assert yakit_harca(30) == 70

def test_sinirla_aralik_disi():
    with pytest.raises(ValueError) as hata:
        yakit_harca(150)
    assert str(hata.value) == "yakit_harca: 150 değeri 0-100 aralığında değil"
    
    with pytest.raises(ValueError):
        yakit_harca(-10)    