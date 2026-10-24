# Sysmon ve Telemetri

## Temel kavramlar

**Telemetri**, sistem davranışları hakkında toplanan teknik gözlem verileridir. Log, bu verinin belirli biçimde kaydedilmiş hâlidir.

**Sysmon**, Microsoft Sysinternals ailesindeki Windows izleme aracıdır. Engelleme veya tek başına zararlı kararı verme yerine ayrıntılı endpoint telemetrisi üretir. Kayıtları genellikle Microsoft-Windows-Sysmon/Operational kanalındadır.

## Temel Event ID'leri

- **1:** Process creation
- **3:** Network connection
- **7:** Image/DLL loaded
- **11:** File created
- **12–14:** Registry değişiklikleri
- **22:** DNS query

## Korelasyon ve yorumlama

- **SHA256:** Aynı dosya içeriğini kurum genelinde aramaya yardım eder; küçük bir dosya değişikliği hash'i değiştirir.
- **ProcessGuid:** Aynı process'in farklı event'lerdeki davranışlarını ilişkilendirir ve yeniden kullanılabilen PID'ye göre daha güvenilirdir.
- **ParentProcessGuid:** Parent-child process bağını korur.
- Event 11 dosyanın oluşturulduğunu gösterir; hangi IP'den indirildiğini tek başına kanıtlamaz.
- Event 22 DNS sorgusunu gösterir; bağlantı kurulduğunu tek başına kanıtlamaz.
- HKCU Run değişikliği, ilgili kullanıcı oturum açtığında çalışarak persistence sağlayabilir.
- Kullanıcı tarafından yazılabilir klasörden imzasız DLL yüklenmesi side-loading/hijacking ihtimalini düşündürür; tek event tekniği kesinleştirmez.

## Yapılandırma ve görünürlük

- **include:** Yalnızca eşleşen olayları kaydet.
- **exclude:** Eşleşen olayları kaydetme.

Aşırı geniş exclude kuralları kör nokta oluşturur. PowerShell, cmd ve rundll32 gibi living-off-the-land araçlarının tüm process creation kayıtlarını hariç tutmak; parent-child ilişkisini, command line'ı ve ProcessGuid korelasyonunu kaybettirebilir.

**Kayıt bulunmaması, olayın gerçekleşmediğinin kanıtı değildir.** Yapılandırma, servis/agent sağlığı, filtreler, log silinmesi, zaman aralığı ve SIEM iletimi kontrol edilmeli; diğer kaynaklarla doğrulama yapılmalıdır.

## Örnek vaka

**Outlook → Word → hidden/encoded PowerShell → DNS sorgusu → Temp altında support.exe oluşturulması → çalıştırma → HKCU Run persistence**

Dosyanın sorgulanan domain'den indirildiği ek telemetri olmadan çıkarımdır. Event ID 3 yokluğu da network bağlantısı kurulmadığını kanıtlamaz.
