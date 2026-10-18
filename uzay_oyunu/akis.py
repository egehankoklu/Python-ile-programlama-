from collections.abc import Iterator

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