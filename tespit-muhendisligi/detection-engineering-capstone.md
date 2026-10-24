# Detection Engineering Capstone

## Test, validation ve coverage

- Syntax testi biçimi; fonksiyonel test hedef davranışı; negatif test normal davranışı; regression testi eski kör noktanın dönmemesini kontrol eder.
- Kuralın alarm üretmemesi saldırı olmadığı anlamına gelmez. Kapsam dışı varyasyon, alan eşleşmemesi, telemetri/agent eksikliği, parser sorunu, yanlış zaman aralığı veya devre dışı kural olabilir.

## Threshold, suppression ve tuning

- Allowlist dar ve doğrulanabilir user/host/script/imza/zaman koşullarıyla uygulanır.
- Threshold hacmi, aggregation benzer event'leri tek alarmda özetler.
- Suppression tekrarları azaltır; severity yükselten yeni kanıtı susturmamalıdır.
- Risk-based alerting process, file, network, identity ve asset bağlamını puanlayabilir.

## Versioning ve dokümantasyon

Kural değişiklikleri Git/PR üzerinden owner, gerekçe, ticket/incident, test sonucu, coverage/FP etkisi ve rollback planıyla sürümlenir. Yeni varyasyon minor; küçük kontrollü düzeltme patch; büyük mantık değişikliği major sürüm olabilir.

## Detection gap analizi

Technique, telemetry, field mapping, coverage, asset ve süreç gap'leri ayrı kaydedilir. CommandLine boşluğu sessizce filtrelenmez; alternatif sinyal araştırılır ve veri kalitesi problemi sahipli aksiyona dönüştürülür.
