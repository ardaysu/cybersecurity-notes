# HTTP, HTTPS ve TLS

HTTP açık metin taşındığında aradaki sistemler içeriği okuyabilir veya değiştirebilir. HTTPS, HTTP trafiğini TLS ile korur.

TLS genel olarak içeriği şifreler, sunucu kimliğini sertifikayla doğrular ve veri bütünlüğünü korur. Fakat bütün davranışsal bilgiyi gizlemez:

- Kaynak/hedef IP ve port
- Zaman ve bağlantı süresi
- Paket ve akış boyutları
- Trafik yönü
- Sensör ve TLS sürümüne bağlı bazı handshake bilgileri

> **Ana sonuç:** TLS içeriği gizler; trafiğin varlığını ve davranışını tamamen gizlemez.

Şifreli trafikte NIDS içerik tabanlı imzaları göremeyebilir. TLS inspection; mahremiyet, performans ve sertifika yönetimi maliyeti doğurur.
