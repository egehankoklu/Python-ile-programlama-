import pytest
import itertools
from uzay_oyunu.akis import fibonacci, yakit_gostergesi
from uzay_oyunu.akis import fibonacci, yakit_gostergesi, satirlari_oku, ayristir, uzun_yolculuklar, rota_sayaci

def test_fibonacci_next():
    g = fibonacci()
    sonuc = (next(g), next(g), next(g))
    assert sonuc == (0, 1, 1)

def test_fibonacci_islice():
    sonuc = list(itertools.islice(fibonacci(), 12))
    assert sonuc == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def test_fibonacci_takewhile():
    sonuc = list(itertools.takewhile(lambda x: x < 100, fibonacci()))
    assert sonuc == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def test_fibonacci_tek_kullanimlik():
    g = fibonacci()
    ilk_cagri = list(itertools.islice(g, 3))
    ikinci_cagri = list(itertools.islice(g, 3))
    
    assert ilk_cagri == [0, 1, 1]
    assert ikinci_cagri == [2, 3, 5]
    assert ilk_cagri != ikinci_cagri



    import pytest

def test_yakit_gostergesi_liste():
    sonuc = list(yakit_gostergesi(100, 30))
    assert sonuc == [70, 40, 10, 0]

def test_yakit_gostergesi_stopiteration():
    gosterge = yakit_gostergesi(20, 15)
    assert next(gosterge) == 5
    assert next(gosterge) == 0
    
    with pytest.raises(StopIteration):
        next(gosterge)

def test_boru_hatti_toplam_yakit():
    sonuc = sum(y for _, _, y in ayristir(satirlari_oku("veri/seyir.txt")))
    assert sonuc == 88

def test_boru_hatti_uzun_yolculuklar():
    kayitlar = ayristir(satirlari_oku("veri/seyir.txt"))
    sonuc = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
    assert sonuc == ['sirius', 'centauri', 'orion', 'kara_delik']


def test_rota_sayaci():
    baglantilar = {
        "a": ["b", "c"],
        "b": ["a"],
        "c": ["a", "b"]
    }
    say = rota_sayaci(baglantilar)
    
    assert say("a", 0) == 1
    assert say("a", 1) == 2
    assert say("a", 2) == 3  