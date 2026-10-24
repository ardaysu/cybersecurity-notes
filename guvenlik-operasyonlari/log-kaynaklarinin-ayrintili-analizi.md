# Log Kaynaklarının Ayrıntılı Analizi

## Endpoint

Process, parent-child ilişkisi, command line, kullanıcı, dosya, registry ve process-network bağlamını gösterir. Firewall kaydı hedefi gösterebilir; bağlantıyı hangi process'in başlattığını endpoint telemetrisi açıklar.

## Network

- **Firewall:** Kaynak/hedef IP, port, protokol ve allow/deny. Allowed, hedefin cevap verdiğini veya bağlantının tamamlandığını tek başına kanıtlamaz.
- **Proxy:** Kullanıcı, domain/tam URL, HTTP yöntemi, durum kodu ve byte miktarı. HTTP 200, dosyanın diske tam yazıldığını veya çalıştırıldığını tek başına kanıtlamaz.
- **DNS:** Domain sorgusu ve çözümlenen IP. Aynı IP'deki firewall bağlantısının kesin olarak o domain'e ait olduğunu tek başına kanıtlamaz.
- **IDS/IPS:** Trafikte imza veya şüpheli örüntü. IDS alarm üretir; IPS yapılandırmaya göre engelleyebilir.
- **NetFlow:** İletişim özeti; bağlantı sayısı, zaman, süre ve byte miktarı. Düzenli aralıklar beaconing ihtimalini gösterebilir.
- **VPN:** Kullanıcı, kaynak IP, verilen iç IP, bağlantı zamanı ve oturum süresi.

## Identity

Başarılı/başarısız giriş, kaynak IP/cihaz, MFA sonucu, doğrulama yöntemi, parola/rol/grup değişiklikleri ve riskli giriş bağlamını verir. **MFA Approved**, girişin bilinçli ve meşru kullanıcı tarafından yapıldığını garanti etmez; MFA fatigue, yanlış onay veya token ele geçirilmesi araştırılır.

## Application

Uygulama içindeki kullanıcı ve iş eylemini gösterir: çağrılan API/endpoint, yöntem, sonuç, etkilenen kayıt sayısı, kaynak IP ve rol değişiklikleri. Request/trace ID, işlemi gateway, backend ve veritabanı logları arasında ilişkilendirebilir.

## Kanıt ve çıkarım

Her kaynak yalnızca gözlemlediği katmanı kanıtlar. Proxy'deki başarılı istek, endpoint'teki aynı adlı dosya oluşturma ve yakın timestamp birlikte indirmeyi güçlü biçimde destekleyebilir; ancak kesin bağ için process-URL ilişkisi, eşleşen hash, aktarımın tamamlanması veya ek EDR telemetrisi aranır.

## Final vaka

**Şüpheli identity girişi → Word'den hidden/encoded PowerShell → DNS ve proxy üzerinden client.exe isteği → endpoint'te dosya oluşturma/çalıştırma → ayrıcalıklı application hesabıyla 120.000 kayıt dışa aktarma**

Bu zincir olası hesap ele geçirme, zararlı kod çalıştırma, payload indirme ve veri çıkarma davranışlarını destekler. Incident açılması; hesap/oturum kontrolü, endpoint izolasyonu, kapsam ve veri çıkışının doğrulanması gerekir.
