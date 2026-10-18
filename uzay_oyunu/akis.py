from collections.abc import Iterator

def fibonacci() -> Iterator[int]:
    """Sonsuz bir Fibonacci dizisi üreten üreteç (generator) fonksiyonu."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b