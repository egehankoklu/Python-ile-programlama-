import pytest
import itertools
from uzay_oyunu.akis import fibonacci, yakit_gostergesi

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