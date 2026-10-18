import time
from typing import Any

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


def sure_olc(fonksiyon: Callable) -> Callable:
    """Bir fonksiyonun ne kadar sürede çalıştığını ölçer ve ekrana yazdırır."""
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"Çalışma süresi: {bitis - baslangic:.6f} saniye")
        return sonuc
        
    return sarmalayici

en_bagli_gezegenler = sure_olc(en_bagli_gezegenler)
