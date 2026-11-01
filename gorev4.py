n = int(input("n: "))

mevcut = n
adim = 0
en_yuksek = n

while mevcut != 1:
    mevcut = mevcut // 2 if mevcut % 2 == 0 else 3 * mevcut + 1
    if mevcut > en_yuksek:
        en_yuksek = mevcut
    adim += 1

print(f"{n} -> 1: {adim} adım, en yüksek değer {en_yuksek}")

sinir = int(input("Üst sınır: "))

maks_adim = 0
en_uzun_baslangic = 1

for i in range(1, sinir + 1):
    mevcut_i = i
    guncel_adim = 0
    
    while mevcut_i != 1:
        mevcut_i = mevcut_i // 2 if mevcut_i % 2 == 0 else 3 * mevcut_i + 1
        guncel_adim += 1
        
    if guncel_adim > maks_adim:
        maks_adim = guncel_adim
        en_uzun_baslangic = i

print(f"1-{sinir} arasında en uzun zincir: {en_uzun_baslangic} ({maks_adim} adım)")