from typing import Callable, Dict, Any, Tuple

KOMUTLAR: Dict[str, Tuple[Callable, str]] = {}

def komut(ad: str, aciklama: str = "") -> Callable:
    """Fonksiyonu değiştirmeden KOMUTLAR sözlüğüne kaydeden dekoratör."""
    def dekorator(fonksiyon: Callable) -> Callable:
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' komutu zaten kayıtlı!")
        KOMUTLAR[ad] = (fonksiyon, aciklama)
        return fonksiyon
    return dekorator

@komut("yardim", "komutlari listeler")
def yardim(durum: Dict[str, Any]) -> str:
    """Sistemdeki tüm komutları ve açıklamalarını listeler."""
    sonuc = []
    for k_ad, (_, k_aciklama) in KOMUTLAR.items():
        sonuc.append(f"{k_ad:<10} {k_aciklama}")
    return "\n".join(sonuc)

@komut("envanter", "esyalarini gosterir")
def envanter(durum: Dict[str, Any]) -> str:
    """Oyuncunun durum sözlüğündeki eşyalarını gösterir."""
    credits_sayisi = durum.get('credits', 0)
    engines = durum.get('engines', 0)
    copilot = durum.get('copilot', False)
    return f"Credits: {credits_sayisi}, Engines: {engines}, Copilot: {copilot}"

@komut("harita", "gidebilecegin gezegenleri gosterir")
def harita(durum: Dict[str, Any]) -> str:
    """Durum içindeki bağlantılar listesini aralarına virgül koyarak döndürür."""
    baglantilar = durum.get("baglantilar", [])
    return ", ".join(baglantilar)