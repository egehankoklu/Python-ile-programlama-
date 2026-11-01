cumle = input("Cümle: ")

harf_sayisi = 0
sesli_sayisi = 0
sessiz_sayisi = 0
rakam_sayisi = 0
kelime_sayisi = 0

kelime_icindeyiz = False
sadece_harfler = ""
ters_harfler = ""
ters_cumle = ""

sesliler = "aeıioöuüAEIİOÖUÜ"

for karakter in cumle:
    ters_cumle = karakter + ters_cumle
    
    if karakter.isalpha():
        harf_sayisi += 1
        kucuk_harf = karakter.lower()
        sadece_harfler += kucuk_harf
        ters_harfler = kucuk_harf + ters_harfler
        
        if karakter in sesliler:
            sesli_sayisi += 1
        else:
            sessiz_sayisi += 1
            
    if karakter.isdigit():
        rakam_sayisi += 1
        
    if karakter.isspace():
        kelime_icindeyiz = False
    else:
        if not kelime_icindeyiz:
            kelime_sayisi += 1
            kelime_icindeyiz = True

print(f"Harf: {harf_sayisi}   Sesli: {sesli_sayisi}   Sessiz: {sessiz_sayisi}   Rakam: {rakam_sayisi}   Kelime: {kelime_sayisi}")
print(f"Ters: {ters_cumle}")

if sadece_harfler != "" and sadece_harfler == ters_harfler:
    print("Palindrom")
elif sadece_harfler != "":
    print("Palindrom değil")