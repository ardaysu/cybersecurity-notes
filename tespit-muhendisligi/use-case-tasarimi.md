# Use Case Tasarımı

Belirsiz “şüpheli PowerShell'i yakala” talebi; tehdit senaryosu, korunan varlık, gözlemlenen davranış, potansiyel iş etkisi, telemetri, detection mantığı, severity, FP koşulları, playbook ve başarı ölçütleri bulunan uygulanabilir use case'e dönüştürüldü.

## Tasarım ilkeleri

- Gözlemlenen davranış ile yalnızca potansiyel olan etki ayrılır.
- Aynı detection, privileged user, critical asset, executable oluşturma ve zararlı network hedefi gibi enrichment'larla daha yüksek önceliğe çıkabilir.
- Başarı alarm sayısıyla değil; saldırı testlerini yakalama, kabul edilebilir FP, yeterli araştırma alanları, telemetri coverage'ı ve triage kullanılabilirliğiyle ölçülür.
- Meşru otomasyonlar geniş ekip/kullanıcı allowlist'iyle değil; user, host, parent/child, script path, imza/hash, zaman, owner ve change ticket gibi dar koşullarla belgelenir.
- Playbook parent process, command/script içeriği, kullanıcı yetkisi, belge kaynağı, file/network/persistence davranışı ve kurum genelindeki yayılımı araştırır.

## Karar

Office → hidden/encoded PowerShell güçlü bir alert'tir; tek başına doğrulanmış incident değildir. Komut içeriği ve devam davranışlarıyla doğrulanır, kanıt güçlenirse incident'a yükseltilir.
