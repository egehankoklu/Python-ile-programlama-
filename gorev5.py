gizli_kelime = "KOŞUL"
tahminler = ""
hata = 0

while hata < 6:
    gosterim = ""
    for harf in gizli_kelime:
        if harf in tahminler:
            gosterim += harf + " "
        else:
            gosterim += "_ "
    
    if "_" not in gosterim:
        print(f"{gosterim.strip()}   (hata: {hata}/6)   Kazandınız!")
        break
        
    print(f"{gosterim.strip()}   (hata: {hata}/6)")
    
    giris = input("Harf: ")
    
    if len(giris) != 1 or not giris.isalpha():
        continue
        
    if giris == "i":
        harf = "İ"
    elif giris == "ı":
        harf = "I"
    else:
        harf = giris.upper()
        
    if harf in tahminler:
        print("->   Bu harfi zaten denediniz.")
        continue
        
    tahminler += harf
    
    if harf not in gizli_kelime:
        hata += 1
else:
    print(f"Kaybettiniz. Gizli kelime: {gizli_kelime}")