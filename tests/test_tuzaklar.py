from uzay_oyunu.oyun import yakit_ekle

def test_yakit_ekle_tuzagi():
    sonuc1 = yakit_ekle(10)
    assert sonuc1 == [10]
    
    sonuc2 = yakit_ekle(20)
    assert sonuc2 == [20]