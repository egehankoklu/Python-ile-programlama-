import time
from functools import wraps
from typing import Callable, Any

def sure_olc(fonksiyon: Callable) -> Callable:
    """Fonksiyonun çalışma süresini ölçüp ekrana yazdıran dekoratör."""
    @wraps(fonksiyon)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        fark = bitis - baslangic
        print(f"{fonksiyon.__name__}: {fark:.4f} sn")
        return sonuc
        
    return sarmalayici


def say(fonksiyon: Callable) -> Callable:
    """Fonksiyonun kaç kez çağrıldığını bir nitelikte tutan dekoratör."""
    @wraps(fonksiyon)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        sarmalayici.cagri += 1
        return fonksiyon(*args, **kwargs)
    
    sarmalayici.cagri = 0
    return sarmalayici


def log_cagri(fonksiyon: Callable) -> Callable:
    """Çağrı öncesi argümanları ve sonrası dönüş değerini yazdıran dekoratör."""
    @wraps(fonksiyon)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        arg_listesi = [repr(a) for a in args]
        kwarg_listesi = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        tum_argumanlar = ", ".join(arg_listesi + kwarg_listesi)
        
        print(f"-> {fonksiyon.__name__}({tum_argumanlar})")
        sonuc = fonksiyon(*args, **kwargs)
        print(f"<- {fonksiyon.__name__} = {repr(sonuc)}")
        
        return sonuc
        
    return sarmalayici