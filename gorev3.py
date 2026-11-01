tc_no = input("T.C. kimlik no: ")

gecerli_mi = False

if len(tc_no) == 11 and tc_no.isdigit() and tc_no[0] != '0':
    toplam_tek = 0
    toplam_cift = 0

    for i in range(9):
        rakam = int(tc_no[i])
        if i % 2 == 0:
            toplam_tek += rakam
        else:
            toplam_cift += rakam

    h10 = (7 * toplam_tek - toplam_cift) % 10
    h11 = (toplam_tek + toplam_cift + h10) % 10

    if h10 == int(tc_no[9]) and h11 == int(tc_no[10]):
        print(f"Tek: {toplam_tek}   Çift: {toplam_cift}   10. hane: {h10}   11. hane: {h11}   ->   GEÇERLİ")
        gecerli_mi = True

if not gecerli_mi:
    print("->   GEÇERSİZ")