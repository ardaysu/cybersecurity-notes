# Detection Lifecycle

Detection bir sorgudan ibaret değil; tehdit ihtiyacından başlayıp veri doğrulama, geliştirme, test, deploy, izleme, tuning ve emekliliğe kadar yönetilen bir üründür.

## Aşamalar

1. Tehdit/ihtiyaç ve iş riskini tanımlama
2. Gözlemlenebilir detection hipotezi kurma
3. Veri kaynağı, alan, parsing ve coverage doğrulama
4. Kural mantığını geliştirme
5. Pozitif/negatif ve varyasyon testleri
6. Historical backtesting, pilot veya shadow mode
7. Bağlamlı alarm ve SOC playbook hazırlama
8. TP/FP, alarm hacmi ve triage süresini izleme
9. Kontrollü tuning, güncelleme veya emeklilik

## Temel sonuçlar

- Telemetri yoksa iyi görünen kural çalışmaz.
- Pozitif test saldırıyı yakalamayı, negatif test normal davranışın alarm üretmemesini sınar.
- Backtesting kuralın geçmiş verideki hacmini ve bilinen incident'ları yakalayıp yakalamadığını gösterir.
- Geniş allowlist yerine onaylı script, hash/imza, service account ve yönetim cihazı gibi kontrollü istisnalar tercih edilir.
- Detection sahibi, sürümü, ATT&CK eşlemesi, veri kaynağı, playbook'u ve gözden geçirme tarihi belgelenmelidir.
