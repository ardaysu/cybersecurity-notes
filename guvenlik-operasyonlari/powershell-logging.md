# PowerShell Logging

## Neden önemlidir?

PowerShell meşru bir Windows yönetim aracıdır; kullanımı tek başına saldırı değildir. Office parent process'i, hidden window, encoded/obfuscated içerik, dosya indirme, kullanıcı tarafından yazılabilir dizine yazma ve persistence gibi bağlamlar şüpheyi güçlendirir.

## Temel kaynaklar

- **4688 / Sysmon 1:** PowerShell process'inin parent, command line, kullanıcı ve başlatılma bağlamını gösterir.
- **4104 — Script Block Logging:** PowerShell tarafından çalıştırılan kod bloklarını gösterir; uzun script'ler birden fazla parçaya bölünebilir.
- **4103 — Module Logging:** Cmdlet/modül faaliyetleri ve parameter binding ayrıntılarını sağlayabilir.
- **Transcription:** PowerShell oturumu ve konsol çıktısını metin dosyasına kaydedebilir; hassas veri içerebileceği için merkezi ve güvenli korunmalıdır.

## Encoding, obfuscation ve AMSI

- Base64 encoding şifreleme değildir. Windows PowerShell EncodedCommand çoğunlukla UTF-16LE Base64 kullanır.
- Obfuscation, kodu insanlardan ve basit kurallardan gizlemek için string birleştirme ve çalışma anında kod üretme gibi yöntemlerle karmaşıklaştırır.
- **AMSI**, içeriğin antimalware motorunca taranmasına yardım eden arayüzdür; Script Block Logging ile aynı şey değildir.

## Kanıt sınırları

4688'de tam encoded komut yakalanmışsa analist decode ederek URL veya komutu görebilir. Ancak komut çalışma anında oluşturuluyor, parçalanıyor veya değişiyorsa 4688 gerçek yürütülen içeriği tek başına açıklamayabilir. Ayrıca command line niyeti gösterse bile indirme, dosya oluşturma ve çalıştırma başarısı endpoint/network telemetrisiyle doğrulanmalıdır.

PowerShell loglarının bulunmaması PowerShell'in kullanılmadığını kanıtlamaz. Logging kapalı olabilir, Operational kanal SIEM'e gitmeyebilir, kayıtların üzerine yazılmış olabilir, farklı host/yürütme yöntemi kullanılmış veya telemetri kurcalanmış olabilir.

## Final vaka

**Word → hidden/encoded PowerShell (4688) → Invoke-WebRequest kodu (4104) → cmdlet/parametreler (4103) → dosya oluşturma (Sysmon 11) → payload çalıştırma (Sysmon 1) → zararlı IP bağlantısı (EDR)**

Bu zincir incident açılmasını; cihaz izolasyonu, hesap/oturum kontrolü, hash'in kurum genelinde aranması ve aynı belgeyi alan kullanıcıların araştırılmasını destekler.
