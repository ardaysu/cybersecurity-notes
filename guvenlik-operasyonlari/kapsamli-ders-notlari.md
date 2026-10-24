# Faz 2 — Güvenlik Operasyonları (SOC)

> **Durum:** Tamamlandı  
> **Amaç:** Alarmı ezbere kapatmak yerine, kanıtları ilişkilendirerek karar verebilen analist düşüncesi geliştirmek.

## 1. SOC ve analist seviyeleri

SOC, güvenlik sinyallerinin izlendiği, doğrulandığı, araştırıldığı ve müdahaleye dönüştürüldüğü operasyon merkezidir.

- **L1:** Alarm doğrulama, ilk bağlam, temel triage ve eskalasyon.
- **L2:** Derin inceleme, kapsam belirleme, zaman çizelgesi ve containment önerisi.
- **L3 / Threat Hunter / Detection Engineer:** Proaktif avcılık, karmaşık olaylar, yeni tespit geliştirme ve telemetri boşlukları.

Seviyeler her kurumda aynı adla kullanılmayabilir. Esas fark, kararın karmaşıklığı ve sorumluluk alanıdır.

## 2. SIEM, EDR, XDR ve SOAR

| Sistem | Temel işi | Analiste sağladığı bağlam |
|---|---|---|
| SIEM | Farklı kaynaklardaki logları toplar, normalize eder ve ilişkilendirir | Kurum çapında arama ve korelasyon |
| EDR | Endpoint process, dosya, registry ve ağ davranışını izler | Process ağacı ve host müdahalesi |
| XDR | Endpoint, identity, e-posta ve ağ sinyallerini ortak olayda birleştirir | Ürünler arası saldırı zinciri |
| SOAR | Tekrarlanan araştırma ve müdahale adımlarını otomatikleştirir | Enrichment, ticket, containment akışı |

SOAR otomasyon demektir ama körlemesine aksiyon demek değildir. Yanlış pozitif üreten bir kuralı otomatik izolasyona bağlamak operasyonel zararı büyütebilir.

## 3. Incident Response ve Threat Hunting

Incident Response genellikle bir sinyal veya doğrulanmış olayla başlar: hazırlık, tespit/analiz, containment, eradication, recovery ve lessons learned.

Threat hunting ise “alarm gelmesini beklemeden” bir hipotezi test eder:

> Saldırganlar kullanıcı cihazlarında imzalı Windows araçlarını kullanarak gizli PowerShell başlatıyor olabilir mi?

Hunt sonucu zararlı aktivite, benign açıklama, veri eksikliği veya yeni detection fikri olabilir. Sonuç bulunamaması, hipotezin yanlış olduğunu kanıtlamaz; telemetri yetersiz olabilir.

## 4. Kural tabanlı tespit ve UEBA

Kural tabanlı tespit belirli koşulları arar. UEBA kullanıcı ve varlık davranışlarının alışılmış profilinden sapmayı değerlendirir. UEBA'nın değeri “ML kullandığı için otomatik doğru” olması değil, kimlik ve varlık geçmişini bağlama katmasıdır.

Örnek:

```text
finance.admin normalde 09:00–18:00 çalışıyor
02:10 yeni cihazdan oturum
02:12 ADMIN$ erişimi
```

Yeni cihaz tek başına saldırı değildir; saat, ayrıcalık, hedef ve önceki credential access olayı riski yükseltir.

## 5. False positive, false negative ve metrikler

- **True Positive:** Saldırı doğru yakalandı.
- **False Positive:** Meşru davranış saldırı diye işaretlendi.
- **False Negative:** Saldırı kaçırıldı.
- **True Negative:** Meşru davranış doğru biçimde sessiz kaldı.

`Precision = TP / (TP + FP)` alarm verenlerin ne kadarının doğru olduğunu; `Recall = TP / (TP + FN)` gerçek saldırıların ne kadarının yakalandığını gösterir.

Kritik bir sistemde recall öncelikli olabilir; fakat sınırsız yanlış alarm da analistlerin asıl vakayı kaçırmasına neden olur. “Hiç saldırı kaçmasın, alarm yorgunluğu tolere edilir” ancak operasyonun gerçekten bu alarmları işleyebildiği ölçüde doğrudur. Güvenlikte maliyet sadece model metriği değil, insan dikkatidir.

## 6. 327 high-priority alarm problemi

Bir vardiyada yüzlerce “high” alarm varsa iki olasılık vardır: kurum gerçekten sürekli krizdedir veya önceliklendirme anlamını yitirmiştir. İncelenecekler:

- Kural aynı olayı tekrar tekrar mı üretiyor?
- Varlık kritiklikleri kullanılıyor mu?
- Çok sık görülen benign süreç için kontrollü suppression mümkün mü?
- Aynı saldırı zincirine ait alarmlar tek incident altında gruplanıyor mu?
- “High” etiketi davranışın şiddetini mi, yalnızca tek IOC eşleşmesini mi anlatıyor?

Amaç alarm sayısını kozmetik olarak azaltmak değil; analist dikkatini gerçek riske taşımaktır.

## 7. Windows Event Logs ve authentication

Event ID tek başına karar değildir; olayın türünü bulmak için indekstir.

| Event ID | Genel anlam | Analiz sorusu |
|---|---|---|
| 4688 | Yeni process | Parent, command line, kullanıcı nedir? |
| 4624 | Başarılı logon | Logon type, kaynak cihaz/IP, hesap normal mi? |
| 4625 | Başarısız logon | Hata nedeni, tekrar sayısı ve hedef dağılımı nedir? |
| 4720 | Kullanıcı oluşturma | Kim oluşturdu, ticket var mı? |
| 4728 / 4732 | Gruba üye ekleme | Hangi ayrıcalık kazanıldı? |
| 4698 | Scheduled task oluşturma | Action, trigger, run-as ve creator nedir? |
| 7045 | Servis kurulması | Binary yolu, hesap ve başlangıç tipi nedir? |
| 1102 | Security log temizleme | Kim, neyin ardından ve neden temizledi? |

Event 1102 güçlü bir defense evasion sinyali olabilir; bakım veya test faaliyeti de olabilir. Onay kaydı ve öncesindeki davranış kontrol edilir.

## 8. Sysmon ve telemetri

Sysmon, Windows'un varsayılan loglarının ötesinde process, network, file ve registry telemetrisi sağlar. Sık kullanılan örnekler:

- Event 1: Process creation
- Event 3: Network connection
- Event 10: Process access
- Event 11: File creation
- Event 12–14: Registry değişiklikleri

Sysmon kurmak tek başına görünürlük sağlamaz. Doğru yapılandırma, merkezi toplama, zaman senkronizasyonu, alanların normalize edilmesi ve saklama süresi gerekir. Kaydedilmeyen command line sonradan geri getirilemez.

## 9. Log kaynakları ve korelasyon

Bir phishing zinciri farklı sistemlere dağılır:

```text
E-posta güvenliği → mesaj kullanıcıya ulaştı
Proxy/DNS         → bağlantı açıldı
EDR               → tarayıcıdan EXE ve process zinciri
Firewall          → dış IP bağlantısı
Identity          → yeni cihazdan oturum
File/DLP          → olası veri aktarımı
```

Ayrı sistemlerde farklı kullanıcı adı biçimleri varsa identity normalization gerekir. Aksi halde aynı kişinin aksiyonları farklı kişilermiş gibi yorumlanabilir.

**Kesin olan:** E-posta ulaştı, link açıldı, process çalıştı, bağlantı kuruldu.  
**Olası yorum:** Kullanıcının credential'ı ele geçirilmiş olabilir.  
**Ek kanıt:** Yeni cihaz, MFA kaydı, mailbox rule, token kullanımı, veri aktarımı.

## 10. PowerShell logging

PowerShell meşru bir yönetim aracıdır ve sistemde zaten bulunduğu için “living off the land” amacıyla kötüye kullanılabilir.

Şüpheyi artıran işaretler:

- `-WindowStyle Hidden`
- `-EncodedCommand`
- Office veya e-posta istemcisinden başlatılma
- İndirme, bellek içi çalıştırma veya güvenlik ayarını değiştirme
- Kısa sürede credential erişimi veya dış bağlantı

Bu işaretlerin üçünün birden zorunlu tutulması tespiti aşırı daraltır. Her biri ayrı sinyal olabilir; risk puanlama ve korelasyonla güçlendirilebilir.

PowerShell için 4103 module logging ve 4104 script block logging faydalıdır. Ancak loglama devre dışıysa process command line, AMSI/EDR, network ve child process telemetrisi kullanılır.

## 11. Detection lifecycle

```text
İhtiyaç → veri → kural → test → yayın → izleme → tuning → emeklilik
```

Kural üretimde sonsuza kadar doğru kalmaz. Uygulamalar, altyapı, saldırgan teknikleri ve log şemaları değişir. Alarm hacmi düştüğünde “saldırı yok” demeden önce kuralın hâlâ veri alıp almadığı kontrol edilir.

## 12. Alarmdan karara analist akışı

1. Alarmın söylediğini aynen yaz; henüz yorum ekleme.
2. Varlık, kullanıcı, zaman ve iş kritikliğini belirle.
3. Parent-child process, command line ve dosya bilgilerini incele.
4. Öncesi/sonrası ağ, identity, file ve registry olaylarını bağla.
5. Onaylı değişiklik, ticket ve bilinen yönetim aracı ihtimalini doğrula.
6. Kesin gözlem, güçlü çıkarım ve bilinmeyenleri ayrı yaz.
7. Kapsam ve etkiye göre kapat, izle, eskale et veya incident aç.

SOC analizinin özü tek alarmı “iyi/kötü” diye sınıflandırmak değil, eksik bir hikâyeyi kanıtlarla tamamlamaktır.
