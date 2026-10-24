# Firewall, IDS ve IPS

## Firewall

Firewall tanımlı policy'ye göre trafiğe izin verir veya engeller. Temel sorusu: **“Bu iletişime izin verilmeli mi?”**

İzin verilen trafiğin içindeki kötü davranışı her zaman anlayamaz.

## IDS

IDS trafiği veya host olaylarını analiz eder ve şüpheli davranış için alarm üretir. Temel sorusu: **“Bu davranış saldırıya benziyor mu?”**

Genellikle passive gözlem yapar; doğrudan engelleme zorunlu değildir.

## IPS

IPS inline yol üzerinde tespitten sonra paketi düşürme, bağlantıyı sonlandırma veya kaynağı engelleme aksiyonu alabilir.

**Trade-off:** IPS false positive üretirse meşru trafiği kesebilir. Kural güveni, test ve tuning kritiktir.
