from typing import Callable

def hamle_sayaci() -> Callable[[], int]:
    """Her çağrıldığında değeri 1 artan bir sayaç (closure) fonksiyonu döndürür."""
    sayac = 0
    
    def arttir() -> int:
        nonlocal sayac
        sayac += 1
        return sayac
        
    return arttir

def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegenleri bağlantı sayısına göre azalan, eşitlikte alfabetik sırayla döndürür."""
    baglantilar = galaksi["baglantilar"]
    return sorted(baglantilar.keys(), key=lambda p: (-len(baglantilar[p]), p))