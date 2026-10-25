# Fibonacci Çağrı Sayıları ve Dekoratör Sırası

## Ölçüm Sonuçları (fib(20) için)
- Yalnızca @say: 21891
- @say üstte, @lru_cache altta: 39
- @lru_cache üstte, @say altta: 21

## Neden Farklı Çıkıyor?

1. **Yalnızca @say (21891 Çağrı):**
Ortada hiçbir önbellekleme (cache) olmadığı için fonksiyon her sayıyı bulmak için kendini tekrar tekrar çağırır. Ağaç yapısında bir hesaplama olduğu için çağrı sayısı üstel olarak artar ve 21891'e ulaşır.

2. **@say üstte, @lru_cache altta (39 Çağrı):**
İç içe sarmalamada en dışta `@say` olduğu için, fonksiyon her çağrıldığında ilk olarak sayaç artar, ardından önbelleğe (cache) bakılır. Önbellek sayesinde işlemler tekrar hesaplanmaz ancak önbellekten "hazır cevabı sormak" için yapılan tüm çağrılar sayaca takıldığı için sonuç 39 çıkar.

3. **@lru_cache üstte, @say altta (21 Çağrı):**
En dışta önbellek (`@lru_cache`) olduğu için fonksiyon çağrıldığında ilk olarak önbelleğe bakılır. Eğer cevap önbellekte varsa, içerideki `@say` dekoratörüne inilmeden doğrudan cevap döndürülür. `@say` sadece daha önce hiç hesaplanmamış yepyeni bir sayı istendiğinde (cache miss durumunda) çalışır. 0'dan 20'ye kadar tam 21 farklı benzersiz sayı hesaplandığı için sayaç 21 olur. Bu durumda sayaca `fib.__wrapped__.cagri` ile ulaşılır.