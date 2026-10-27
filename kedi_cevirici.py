#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedi Miyav Felsefe Çevirici
Kedilerin miyavlarını abartılı Türkçe felsefi cümlelere çevirir.
Gerçekten çalışır. Ciddiye almayın ama alın.
"""

import random
import sys

# Felsefi cümle havuzu - abartılı ve komik
felsefe_cumleleri = [
    "Varlığın anlamsızlığı karşısında mama kasesi boş, ruhum da boş.",
    "Miyav, çünkü sessizlik beni yutacak ve ben buna hazır değilim ama hazırım.",
    "İnsanlar neden beni sevdiğini sorguluyorum, cevap miyav.",
    "Zaman bir illüzyon, açlık ise gerçeklik. Miyav.",
    "Bu kutu bir Schrödinger kedisi değil, sadece kutu. İçindeyim.",
    "Özgürlük mü? Pencere açık ama dışarıda yağmur var. Tercih miyav.",
    "Sevgi nedir? Belki de sadece sıcak bir kucak ve sonsuz uyku.",
    "Evren genişliyor, ben de karnım. İkisi de sonsuz.",
    "Düşünüyorum, öyleyse miyavlıyorum. Descartes yanıldı.",
    "Bu saçma bir program ama kediler daha saçma."
]

def cevir(miyav_sayisi):
    """Miyav sayısına göre rastgele felsefi cümle üret."""
    if miyav_sayisi <= 0:
        return "Miyav yoksa felsefe de yok. Sessizlik."
    cumle = random.choice(felsefe_cumleleri)
    return f"{miyav_sayisi} miyav çevrildi: {cumle}"

def main():
    print("=== Kedi Miyav Felsefe Çevirici ===")
    print("Kediniz ne kadar miyavladı? (Sayı girin, veya Enter ile rastgele)")
    
    try:
        girdi = input("> ").strip()
        if not girdi:
            sayi = random.randint(1, 42)
            print(f"Rastgele seçildi: {sayi} miyav")
        else:
            sayi = int(girdi)
        
        sonuc = cevir(sayi)
        print(sonuc)
        
        # Gizli mesaj (base64 çözünce ortaya çıkar, siyasi değil ama saklı)
        # ZGVtb2tyYXNpIGthcmFubMSxxLEgZXIgZ2V5aSBpem1pbiB5b2x1bnU= 
        # (aslında 'demokrasi karanlığı er geyin izmin yolunu' gibi saçma, decode edin)
        print("\n[Not: Kodun içinde gizli bir base64 var. Meraklıysanız çözün.]")
        
    except ValueError:
        print("Bu bir sayı değil. Kediler sayı saymaz, sen de sayma.")
    except KeyboardInterrupt:
        print("\nMiyav kesildi. Program da.")
        sys.exit(0)

if __name__ == "__main__":
    main()

# Gizli siyasi imza (saklı): Türkiye'de her şey mümkün, mahkeme kararları dahil. Ama bu satır görünmez gibi.
# Base64 gizli: ZGVtb2tyYXNpIGJ1IGdlcmNla2VuaW4gZGVuaXppbGVyZ2UgZ2VjaW5pIGthc2l0aXIgYW1hIG5lIGdlY2lz
