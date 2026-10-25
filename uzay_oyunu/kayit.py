

def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler: str) -> None:
    """Görev detaylarını, adımları ve ek bilgileri formatlı şekilde ekrana yazdırır."""
    print(f"[{oncelik.upper()}] {baslik}")
    
    for i, adim in enumerate(adimlar, 1):
        print(f"  {i}. {adim}")
        
    for anahtar, deger in ekler.items():
        print(f"{anahtar}: {deger}")


if __name__ == "__main__":
    adim_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_sozluk = {"sorumlu": "Ayşe"}

    gorev_kaydi("Kara deliğe atla", *adim_listesi, oncelik="yüksek", **ek_sozluk)