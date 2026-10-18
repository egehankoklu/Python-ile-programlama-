from collections.abc import Iterator
from typing import Iterable, Tuple

def fibonacci() -> Iterator[int]:
    """Sonsuz bir Fibonacci dizisi üreten üreteç (generator) fonksiyonu."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def yakit_gostergesi(yakit: int, tuketim: int) -> Iterator[int]:
    """Her çağrıldığında yakıtı tüketim kadar azaltıp kalanı üreten fonksiyon."""
    while yakit > 0:
        yakit -= tuketim
        if yakit < 0:
            yakit = 0
        yield yakit   


from typing import Iterator, Iterable, Tuple

def satirlari_oku(yol: str) -> Iterator[str]:
    """Dosyayı satır satır okur, boş ve # ile başlayan satırları atlar."""
    with open(yol, 'r', encoding='utf-8') as dosya:
        for satir in dosya:
            temiz_satir = satir.strip()
            if temiz_satir and not temiz_satir.startswith('#'):
                yield temiz_satir

def ayristir(satirlar: Iterable[str]) -> Iterator[Tuple[str, str, int]]:
    """Satırları kaynak, hedef ve yakıt demetine dönüştürür."""
    for satir in satirlar:
        parcalar = satir.split()
        yield (parcalar[0], parcalar[2], int(parcalar[3]))

def uzun_yolculuklar(kayitlar: Iterable[Tuple[str, str, int]], esik: int) -> Iterator[Tuple[str, str, int]]:
    """Yakıt miktarı eşik değerinden büyük olan kayıtları süzer."""
    for kayit in kayitlar:
        if kayit[2] > esik:
            yield kayit 