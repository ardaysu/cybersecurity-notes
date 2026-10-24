# Kural Tabanlı Tespit ve UEBA

## Kural tabanlı tespit

Önceden tanımlanmış koşulları arar.

Örnek:

- Belirli sayıda başarısız oturum açma
- Bilinen kötü hash
- Şüpheli PowerShell parametresi
- Yasaklı ülke veya IP aralığından erişim

**Avantaj:** Açıklanabilir ve kontrol edilebilir.

**Sınır:** Önceden düşünülmeyen davranışı kaçırabilir; statik eşikler gürültü üretebilir.

## UEBA

User and Entity Behavior Analytics, kullanıcı veya cihaz için davranış profili oluşturur ve sapmaları puanlar.

Örnek: Normalde mesai saatlerinde İstanbul'dan erişen bir kullanıcının gece farklı bir ülkeden çok sayıda sisteme erişmesi.

**Önemli sonuç:** Gece erişimi tek başına saldırı kanıtı değildir. Nöbetçi çalışan, seyahat, VPN veya planlı operasyon olabilir. Saat bilgisi; cihaz, konum, kimlik doğrulama, erişilen kaynak ve geçmiş davranışla birleştirilmelidir.

UEBA kuralın yerini tamamen almaz. Kural tabanlı sinyal ile davranışsal anomali birlikte daha güçlü bağlam oluşturabilir.
