import math

while True:
    x = float(input("a: "))
    y = float(input("b: "))
    z = float(input("c: "))

    if x <= 0 or y <= 0 or z <= 0:
        print("Uyarı: Kenarlar pozitif olmalıdır. Lütfen tekrar girin.")
        continue
        
    if not (x + y > z and x + z > y and y + z > x):
        print("Uyarı: Üçgen eşitsizliği sağlanmıyor. Lütfen tekrar girin.")
        continue
        
    break

if x >= y and x >= z:
    a, b, c = x, y, z
elif y >= x and y >= z:
    a, b, c = y, x, z
else:
    a, b, c = z, x, y

if a == b and b == c:
    kenar_turu = "Eşkenar"
elif a == b or a == c or b == c:
    kenar_turu = "İkizkenar"
else:
    kenar_turu = "Çeşitkenar"

cevre = a + b + c
u = cevre / 2
alan = math.sqrt(u * (u - a) * (u - b) * (u - c))

cos_alfa = (b**2 + c**2 - a**2) / (2 * b * c)
aci = math.degrees(math.acos(cos_alfa))

if math.isclose(aci, 90.0):
    aci_turu = "Dik açılı"
elif aci > 90.0:
    aci_turu = "Geniş açılı"
else:
    aci_turu = "Dar açılı"

print(f"Tür: {kenar_turu}, {aci_turu}")
print(f"Çevre: {cevre:.2f}   Alan: {alan:.2f}   En büyük açı: {aci:.2f}°")