# Detection Engineering'e Giriş

Detection Engineering; tehdit davranışını ölçülebilir telemetriye çevirme, kuralı geliştirme, test etme, deploy etme, izleme ve tune etme disiplinidir.

## Kural yazmadan önce sorulacaklar

- Hangi tehdit davranışını yakalamaya çalışıyorum?
- İlgili MITRE ATT&CK technique hangisi?
- Davranışı hangi veri kaynağı gözlemleyebilir?
- Gerekli alanlar gerçekten loglanıyor mu?
- Normal ortamda bu davranışın meşru karşılığı var mı?
- Kural hangi FP senaryolarını üretir?
- Saldırgan hangi değişiklikle kuralı atlatabilir?
- Başarıyı hangi metrikle ölçeceğim?

## Basit örnek

**Zayıf kural:** Gece yapılan her erişimi alarm üret.

**Daha iyi detection mantığı:** Kullanıcının normal çalışma saatleri dışında, daha önce görülmeyen cihaz veya konumdan, ayrıcalıklı kaynağa erişmesi ve kısa sürede ek şüpheli kimlik doğrulama olayları üretmesi.

Bu yaklaşım tek koşul yerine bağlamsal kanıt kullanır.
