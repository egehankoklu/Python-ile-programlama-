from functools import reduce, partial
from typing import Dict, List

def buyuk_harfli_gezegenler_fonksiyonel(baglantilar: Dict[str, List[str]]) -> List[str]:
    """Gezegen adlarını map ile büyük harfe çevirir."""
    return list(map(str.upper, baglantilar.keys()))

def buyuk_harfli_gezegenler_uretec(baglantilar: Dict[str, List[str]]) -> List[str]:
    """Gezegen adlarını liste üreteci ile büyük harfe çevirir."""
    return [gezegen.upper() for gezegen in baglantilar.keys()]

def coklu_baglantisi_olanlar_fonksiyonel(baglantilar: Dict[str, List[str]]) -> List[str]:
    """En az iki bağlantısı olan gezegenleri filter ile bulur."""
    return list(filter(lambda g: len(baglantilar[g]) >= 2, baglantilar.keys()))

def coklu_baglantisi_olanlar_uretec(baglantilar: Dict[str, List[str]]) -> List[str]:
    """En az iki bağlantısı olan gezegenleri liste üreteci ile bulur."""
    return [gezegen for gezegen in baglantilar.keys() if len(baglantilar[gezegen]) >= 2]

def toplam_baglanti_fonksiyonel(baglantilar: Dict[str, List[str]]) -> int:
    """Toplam bağlantı sayısını reduce ile hesaplar."""
    return reduce(lambda a, b: a + b, map(len, baglantilar.values()), 0)

def toplam_baglanti_sum(baglantilar: Dict[str, List[str]]) -> int:
    """Toplam bağlantı sayısını sum ile hesaplar."""
    return sum(len(baglantilar[g]) for g in baglantilar.keys())

def yolculuk(hedef: str, hiz: int) -> str:
    """Temsili yolculuk fonksiyonu."""
    return f"{hedef} noktasına {hiz} hızıyla gidiliyor."

hizli_yolculuk = partial(yolculuk, hiz=3)

# Bence liste üreteçleri (list comprehension) ve sum() kullanımı, map/filter/reduce üçlüsüne göre çok daha okunaklı çünkü İngilizce bir cümle okur gibi kolayca anlaşılabiliyor.