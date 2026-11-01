taban_numara = "453914880343646"

for i in range(10):
    deneme_numarasi = taban_numara + str(i)
    toplam = 0
    
    for j in range(16):
        rakam = int(deneme_numarasi[j])
        
        if j % 2 == 0:
            rakam *= 2
            if rakam > 9:
                rakam -= 9
                
        toplam += rakam
        
    if toplam % 10 == 0:
        print(i)
        break