import time
from typing import Iterator

def zamanlayici(aralik: float) -> Iterator[bool]:
    """Belirli bir aralık geçtiğinde True, aksi halde False üreten üreteç."""
    son_zaman = time.time()
    while True:
        su_an = time.time()
        if su_an - son_zaman >= aralik:
            son_zaman = su_an
            yield True
        else:
            yield False

def tik_tak_calistir() -> None:
    """10 saniye boyunca çalışan ve tik/tak üreteçlerini kontrol eden ana fonksiyon."""
    baslangic = time.time()
    tik_ureteci = zamanlayici(2.0)
    tak_ureteci = zamanlayici(5.0)
    
    while time.time() - baslangic < 10.0:
        if next(tik_ureteci):
            print("tik")
        if next(tak_ureteci):
            print("tak")

if __name__ == "__main__":
    tik_tak_calistir()

"""
Bu program bir "meşgul bekleme" (busy waiting) örneğidir. Çünkü while döngüsü 
hiç duraksamadan, saniyede binlerce kez dönerek zamanı kontrol eder ve işlemciyi 
(CPU) boş yere yorarak %100 kapasiteyle meşgul eder. 

Eğer time.sleep() kullansaydık, işletim sistemi programımızı belirttiğimiz süre 
boyunca tamamen uykuya alırdı. Böylece işlemci yorulmaz ve o boşlukta bilgisayardaki 
diğer programlara kaynak ayrılabilirdi.
"""