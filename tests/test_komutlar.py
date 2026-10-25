import pytest
from uzay_oyunu.komutlar import KOMUTLAR, komut, yardim, envanter, harita

def test_komut_kayit_hatasi():
    with pytest.raises(ValueError):
        @komut("yardim", "farkli aciklama")
        def sahte_fonksiyon(durum):
            pass

def test_yardim_komutu():
    durum = {}
    sonuc = yardim(durum)
    assert "yardim" in sonuc
    assert "komutlari listeler" in sonuc

def test_envanter_komutu():
    durum = {"credits": 100, "engines": 2, "copilot": True}
    sonuc = envanter(durum)
    assert "Credits: 100" in sonuc

def test_harita_komutu():
    durum = {"baglantilar": ["orion", "dünya", "kara_delik"]}
    sonuc = harita(durum)
    assert sonuc == "orion, dünya, kara_delik"