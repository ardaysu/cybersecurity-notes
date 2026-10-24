# Threat Intelligence Temelleri

## Data, information ve intelligence

- **Data:** Ham gözlem.
- **Information:** Düzenlenmiş ve bağlamlandırılmış veri.
- **Intelligence:** Karar veya aksiyon alınmasını sağlayan değerlendirme.

Threat Intelligence yalnızca IOC listesi değildir; tehdidin kimliği/yöntemleri, hedeflenen varlıklar, göstergenin güvenilirliği ve SOC'un hangi aksiyonu alması gerektiği hakkında bağlam üretir.

## Seviyeler

- **Tactical:** IOC, araç, ATT&CK tekniği, detection ve hunting bilgileri.
- **Operational:** Kampanya, hedefler, ilk erişim, altyapı, zaman aralığı ve saldırı zinciri.
- **Strategic:** Sektör/jeopolitik eğilim, uzun vadeli risk, yatırım ve iş etkisi.

## Kaynaklar ve değerlendirme

Dış kaynaklar; ticari/açık feed'ler, güvenlik raporları, CERT/ISAC, sandbox ve pasif DNS olabilir. İç kaynaklar; geçmiş incident'lar, SIEM/EDR, proxy/DNS/firewall, phishing ve hunting bulgularıdır.

- **Confidence:** Bilginin doğru olduğuna güven.
- **Severity:** Bilgi doğruysa kurum üzerindeki olası etki.

IOC değerlendirilirken kaynak güvenilirliği, bağımsız doğrulama, first/last seen, güncellik, paylaşımlı altyapı ihtimali, kurum içindeki cihaz/process bağlamı ve destekleyici davranışlar incelenir. Her IOC'nin otomatik engellenmesi false positive ve iş kesintisi yaratabilir.

## Intelligence Lifecycle

1. Requirements — cevaplanacak ihtiyacı belirle
2. Collection — uygun iç/dış veriyi topla
3. Processing — normalize et, temizle ve enrich et
4. Analysis — anlamlandır, confidence ve aksiyon üret
5. Dissemination — sonucu doğru hedef kitleye ilet
6. Feedback — fayda/FP sonuçlarıyla yeni ihtiyacı belirle

## Final vaka

Medium-confidence phishing domain'i tek başına incident kanıtı değildir. Aynı domain'in e-posta ile kullanıcılara ulaşması, proxy erişimi, ardından şüpheli identity girişi ve yüksek hacimli application export davranışı aynı hikâyeyi desteklediğinde incident güveni yükselir.

Threat Intelligence'ın görevi yalnızca “domain kötü” demek değil; araştırmayı yönlendirmek, kurum içi telemetriyle ilişkilendirmek ve bulguyu hunting/detection/response aksiyonuna dönüştürmektir.
