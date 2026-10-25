from uzay_oyunu.dekoratorler import sure_olc
import time
from uzay_oyunu.akis import rota_sayaci

baglantilar = {
    "dünya": ["sirius", "alfa"],
    "sirius": ["dünya", "orion"],
    "alfa": ["dünya", "beta"],
    "beta": ["alfa", "orion"],
    "orion": ["sirius", "beta"]
}

say_onbellekli = rota_sayaci(baglantilar)
say_onbellekli("dünya", 20)

baslangic = time.perf_counter()
say_onbellekli("dünya", 20)
bitis = time.perf_counter()
onbellekli_sure = bitis - baslangic

@sure_olc
def onbelleksiz_say(gezegen: str, adim: int) -> int:
    if adim == 0:
        return 1
    toplam = 0
    for komsu in baglantilar.get(gezegen, []):
        toplam += onbelleksiz_say(komsu, adim - 1)
    return toplam

baslangic = time.perf_counter()
onbelleksiz_say("dünya", 20)
bitis = time.perf_counter()
onbelleksiz_sure = bitis - baslangic

print("--- README DOSYASINA YAZILACAK DEĞERLER ---")
print(f"Önbelleksiz süre: {onbelleksiz_sure:.6f} saniye")
print(f"Önbellekli süre: {onbellekli_sure:.6f} saniye")
print(f"Cache Info: {say_onbellekli.cache_info()}")