from uzay_oyunu.dekoratorler import log_cagri
from uzay_oyunu.akis import yakit_gostergesi
from uzay_oyunu.araclar import hamle_sayaci

def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """
    Oyuncunun envanter durumunu kontrol ederek sahip olduğu eşyaların metnini oluşturur.
    
    Args:
        credits (bool): Oyuncunun kredisi olup olmadığı.
        engines (bool): Oyuncunun motoru olup olmadığı.
        copilot (bool): Oyuncunun yardımcı pilotu olup olmadığı.
        
    Returns:
        str: Sahip olunan eşyaları listeleyen metin. Eğer hiçbir eşya yoksa boş string ('') döner.
    """
    esyalar = []
    
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("güçlü motor") 
    if copilot:
        esyalar.append("yetenekli bir pilot")
        
    if not esyalar:
        return ""
        
    return "Sende: " + ", ".join(esyalar)

@log_cagri
def hedef_menusu(hedefler: list[str]) -> str:
    """
    Kullanıcıya sunulacak gidilebilir hedeflerin numaralandırılmış menüsünü oluşturur.
    
    Args:
        hedefler (list[str]): Gidilebilecek hedeflerin isimlerini içeren liste.
        
    Returns:
        str: Numaralandırılmış, çok satırlı menü metni.
    """
    satirlar = ["Nereye gitmek istersin?"]
    
    for i, hedef in enumerate(hedefler, start=1):
        satirlar.append(f"[{i}] {hedef}")
        
    return "\n".join(satirlar)



def yakit_ekle(miktar: int, depo: list = None) -> list:
    """Belirtilen miktardaki yakıtı depoya ekler."""
    if depo is None:
        depo = []
    
    depo.append(miktar)
    return depo


def travel():
    sayac_fonksiyonu = hamle_sayaci()
    gosterge = yakit_gostergesi(100, 40) 
    
    try:
        kalan = next(gosterge)
        sayac_fonksiyonu()
        
        kalan = next(gosterge)
        sayac_fonksiyonu()
        
        kalan = next(gosterge)
        sayac_fonksiyonu()
        
        kalan = next(gosterge)
        sayac_fonksiyonu()
        
    except StopIteration:
        print("Yakıtın bitti, uzayda sürükleniyorsun...")
        return
        
    toplam_hamle = sayac_fonksiyonu()
    print(f"Oyunu {toplam_hamle} hamlede bitirdin!")


@log_cagri
def galaksi_kur(dosya_yolu: str) -> dict:
    return {}  