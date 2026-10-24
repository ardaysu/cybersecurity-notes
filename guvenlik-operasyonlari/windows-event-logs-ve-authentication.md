# Windows Event Logs ve Authentication

## Temel mimari

- Gerçekleşen olay, provider tarafından log kaydına dönüştürülür.
- Kayıt Security, System, Application veya ilgili Operational kanala yazılır.
- Audit Policy kapalıysa olay gerçekleşse bile gerekli kayıt üretilmeyebilir.
- Event sistem kaydıdır; alert detection mantığının event'i şüpheli bulmasıdır; incident doğrulanmış veya güçlü biçimde desteklenen güvenlik vakasıdır.
- Network logu cihazlar arasındaki iletişimi; endpoint telemetrisi bağlantıyı hangi process ve kullanıcının oluşturduğunu gösterir.

## Authentication event'leri

- **4624:** Başarılı logon
- **4625:** Başarısız logon
- **Logon Type 2:** Interactive
- **Logon Type 3:** Network
- **Logon Type 5:** Service
- **Logon Type 10:** RemoteInteractive / RDP
- **Status/SubStatus:** Başarısızlığın genel ve ayrıntılı nedenini açıklar.

### Saldırı örüntüleri

- **Brute force:** Bir hesapta çok sayıda parola
- **Password spraying:** Çok sayıda hesapta aynı birkaç parola
- **Credential stuffing:** Sızdırılmış kullanıcı–parola eşleşmelerini başka sistemlerde deneme

Tek event saldırı kanıtı değildir. Çok sayıda 4625'in ardından aynı kaynaktan 4624 görülmesi ve sonrasında hesap/yetki değişikliği oluşması güçlü bir korelasyon zinciridir.
