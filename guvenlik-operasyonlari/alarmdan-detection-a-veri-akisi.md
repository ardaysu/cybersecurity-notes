# Alarmdan Detection'a Veri Akışı

1. **Telemetry generation:** Endpoint, network, identity ve uygulama olay üretir.
2. **Collection:** Agent, forwarder veya API veriyi toplar.
3. **Parsing / normalization:** Alanlar ortak şemaya dönüştürülür.
4. **Enrichment:** Asset, kullanıcı, threat intelligence ve kritikiyet bilgisi eklenir.
5. **Detection:** Kural, korelasyon, istatistiksel model veya ML sinyal üretir.
6. **Alert:** Detection sonucu analistin inceleyebileceği olaya dönüşür.
7. **Triage / investigation:** Alarm doğrulanır ve bağlam genişletilir.
8. **Response:** Containment, eradication ve recovery uygulanır.
9. **Feedback:** FP/FN sonuçları kurala ve veri kalitesine geri beslenir.

Garbage in, garbage out ilkesi burada geçerlidir. Veri kaynağı eksik, timestamp hatalı veya parsing bozuksa iyi yazılmış kural dahi güvenilir sonuç üretemez.
