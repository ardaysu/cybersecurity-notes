# LSASS ve credential access

## Temel fikir

`lsass.exe`, Windows kimlik doğrulama ve güvenlik politikalarında kritik rol oynar. Aktif oturumlarla ilgili hash, Kerberos ticket'ı veya başka hassas kimlik doğrulama materyalleri bellekte bulunabilir; “bütün parolalar düz metindir” denemez.

## Credential dumping

Onaysız bir process'in LSASS belleğine okuma erişimi istemesi veya dump dosyası oluşturması credential dumping şüphesidir. Ancak:

```txt
LSASS erişim girişimi ≠ credential kesin ele geçirildi
Dump oluşturuldu       ≠ geçerli parola kesin çıkarıldı
```

Erişim sonucu, EDR kararı, dump oluşumu, sonraki dosya/ağ hareketleri ve authentication olayları birlikte incelenir.

## Saldırı zinciri

```txt
LSASS’a erişim
→ dump dosyası
→ sıkıştırma
→ dışarı gönderme
→ ele geçirilmiş olabilecek hesapla yanal hareket
```

Bu zincir credential hırsızlığını güçlü biçimde desteklese de düz metin parola, NTLM hash veya Kerberos ticket gibi hangi materyalin kullanıldığı ayrıca kanıtlanmalıdır.

## Meşru kullanım ihtimali

Microsoft imzalı `ProcDump` gibi araçlar onaylı destek işleminde kullanılabilir; saldırganlar tarafından da kötüye kullanılabilir. Ticket, kullanıcı, zaman, kapsam, dosya yolu ve sonraki davranış doğrulanır.

## Koruma mekanizmaları

- **Protected Process Light (PPL):** Yetkisiz process'lerin LSASS'a erişmesini zorlaştırır.
- **Credential Guard:** Hassas credential materyalinin bir kısmını sanallaştırma tabanlı izole ortamda korur.

Bu korumalar riski azaltır fakat tüm credential access yöntemlerini ortadan kaldırmaz. Saldırgan tarayıcı credential store, Credential Manager, ticket, token, script veya yapılandırma dosyalarına yönelebilir.

## Telemetri

- Sysmon Event ID **10** veya EDR process-access telemetrisi
- Process ve file creation telemetrisi
- EDR block/allow sonucu
- Arşivleme process'i
- Network/proxy aktarım sonucu
- Sonraki Windows authentication ve paylaşım erişimleri

## Final vaka sonucu

Office → PowerShell → LSASS erişimi allowed → dump → ZIP → dış sunucudan HTTP 200 → ayrıcalıklı hesapla `ADMIN$` erişimi zinciri kritik incident gerektirir. Zincir credential kullanımını güçlü biçimde destekler; fakat düz metin parolanın kesin çalındığı iddia edilmez.
