# Kapsam (Scope) İncelemesi

## Örnek 1: Yerel (Local) Kapsam
**Tahmin:** Fonksiyon içinde tanımlanan değişken yazdırılır, dışarıdaki aynı isimli değişken etkilenmez.
**Gerçek Sonuç:** Fonksiyon içindeki değer ekrana yazıldı.
**Neden:** Python önce yerel kapsama bakar. İçeride atanan değişken sadece o blokta yaşar ve dışarıdaki (global) değişkeni ezmez.

## Örnek 2: Küresel (Global) Kapsam Okuma
**Tahmin:** Fonksiyon içinde değişken olmadığı için dışarıdaki (global) değer yazdırılır.
**Gerçek Sonuç:** Dışarıdaki değer başarıyla ekrana yazıldı.
**Neden:** Yerel kapsamda değişken bulunamazsa, okuma işlemi için bir üst kapsama (global) bakılır.

## Örnek 3: UnboundLocalError Tuzağı
**Tahmin:** Dışarıdaki global değişkenin değeri fonksiyon içinde artırılıp yazdırılır.
**Gerçek Sonuç:** `UnboundLocalError` hatası fırlatıldı.
**Neden (UnboundLocalError Açıklaması):** Python, bir fonksiyon içinde bir değişkene atama yapıldığında (örneğin `x = x + 1`), o değişkeni otomatik olarak "yerel" (local) kabul eder. Ancak eşittir işaretinin sağ tarafındaki `x` değerini okumaya çalıştığında, yerelde henüz böyle bir değer tanımlanmadığı için bu hatayı verir.