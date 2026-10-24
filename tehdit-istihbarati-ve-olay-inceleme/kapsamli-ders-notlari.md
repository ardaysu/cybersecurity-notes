# Faz 5 — Threat Intelligence ve DFIR

> **Durum:** 4/10 tamamlandı; 5. başlığa giriş yapıldı ve faz park edildi  
> **Dönüş noktası:** Kaynak güvenilirliği ve bilgi güven seviyesi

## 1. IOC nedir?

IOC, **Indicator of Compromise**; Türkçede ihlal/ele geçirilme göstergesidir. Bir saldırıyla ilişkili olabilecek gözlemlenebilir izdir:

- Dosya hash'i
- IP adresi
- Domain veya URL
- Dosya adı/yolu
- E-posta adresi
- Registry değeri
- Sertifika veya mutex

IOC “kesin saldırı kanıtı” değildir. Olay yerindeki parmak izi gibidir: değerlidir, fakat kime ait olduğu, ne zaman bırakıldığı ve hâlâ geçerli olup olmadığı araştırılır.

## 2. IOC yaşam döngüsü

```text
Toplama → doğrulama → enrichment → kullanıma alma
→ izleme → güncelleme / emekliye ayırma
```

İyi IOC kaydında değer dışında tür, kaynak, first seen, last seen, confidence, durum, ilişkili campaign ve expiration bulunur.

Bir IP sonsuza kadar engellenmez. Saldırgan bulut sunucusunu bırakabilir, dinamik IP başka kullanıcıya geçebilir veya aynı CDN/VPN adresini masum kullanıcılar paylaşabilir. Tarihsel kayıt tutulurken otomatik engelleme süresi dolabilir.

## 3. IOC nerede tutulur ve kullanılır?

- **TIP:** Merkezi kayıt, ilişki ve yaşam döngüsü
- **SIEM:** Loglarla eşleştirme ve watchlist
- **EDR/XDR:** Endpoint tespit/engelleme
- **Firewall, proxy, DNS:** IP/domain/URL kontrolü
- **Case management:** IOC'nin bulunduğu olay ve alınan karar
- **Threat feed:** Dış kaynaklardan güncelleme

Tek bir feed'in güncel ve kurum ihtiyacına uygun olması garanti değildir. Birden fazla kaynak, iç telemetri ve iş bağlamı birlikte değerlendirilir.

## 4. IOC doğrulama ve enrichment

Bir IP için sorular:

- Kime/AS'e ait, hosting/VPN/CDN mi?
- Kaynak bunu neden zararlı sayıyor?
- First/last seen nedir?
- Kurumda daha önce hangi cihazlar erişmiş?
- Bağlantı engellenmiş mi, başarılı mı?
- Öncesi/sonrası dosya indirme, PowerShell veya credential kullanımı var mı?
- Aynı campaign ile ilişkili başka IOC/TTP var mı?

“Zararlı listesinde olan IP'ye erişim görüldü” diyebiliriz; yalnızca bundan “incident doğrulandı” sonucu çıkmaz. Kullanıcı ele geçirilmiş siteyi açmış, reklam yönlendirmesi görmüş veya istek engellenmiş olabilir. Alarm yanlış değildir; sonucu araştırma belirler.

## 5. IOC ve IOA farkı

- **IOC:** Geride kalan veya bilinen gösterge; “neyle ilişki vardı?”
- **IOA (Indicator of Attack):** Saldırgan davranışı/niyeti; “ne yapmaya çalışıyor?”

Dosya hash'i kolay değişir. Buna karşılık Office → encoded PowerShell → credential erişimi → dış bağlantı zincirini değiştirmek saldırgan için daha zahmetlidir. IOA/davranış tespiti çoğu zaman daha dayanıklıdır; fakat daha çok telemetri ve tuning ister.

## 6. Pyramid of Pain

Pyramid of Pain, savunmacının hangi göstergede tespit kurduğunda saldırgana ne kadar değişiklik maliyeti yüklediğini anlatır:

```text
Hash → IP → Domain → Network/Host Artifact → Tool → TTP
```

Alt katmanlar hızlı ve kesin olabilir ama saldırgan için kolay değişir. Üst katmanlar davranışı hedefler ve daha dayanıklıdır; savunmacı için geliştirme ve bakım maliyeti de yükselir.

Doğru strateji yalnızca yukarı çıkmak değildir. Aktif campaign IOC'lerini hemen tararken uzun vadede TTP/davranış detection'ı geliştirmek iki farklı zaman ufkunu birlikte yönetir.

## 7. Living off the Land ve LOLBins

PowerShell, `rundll32`, `mshta`, `certutil` gibi meşru sistem araçları saldırgan tarafından kullanılabilir. Araç adı tek başına zararlı olmadığı için tespit daha zordur.

Bağlam işaretleri:

- Beklenmedik parent process
- Gizli veya encoded komut
- Olağan dışı dosya yolu
- İndirme veya bellekte yürütme
- Güvenlik ayarı değişikliği
- Yeni dış hedef
- Sonraki credential veya lateral movement davranışı

Bu durum saldırganın “kendi levyesini getirmek yerine binadaki aleti kullanması” gibidir. Aracı yasaklamak operasyonu bozabilir; kullanım biçimini izlemek gerekir.

## 8. Threat actor, campaign ve TTP

- **Threat actor:** Faaliyeti yürüten kişi veya grup.
- **Campaign:** Belirli zaman/hedef/amaç çevresindeki ilişkili operasyonlar.
- **TTP:** Tactics, Techniques and Procedures; neyi amaçladıkları, nasıl yaptıkları ve pratikteki uygulama biçimleri.

Aynı actor farklı campaign yürütebilir; aynı TTP birden fazla actor tarafından kullanılabilir. Tek araç veya IP üzerinden kesin attribution yapılmaz.

## 9. Threat Intelligence seviyeleri

| Seviye | Soru | Örnek kullanıcı |
|---|---|---|
| Strategic | Kurum hangi tehditlere yatırım yapmalı? | Yönetim, risk |
| Operational | Hangi campaign/actor kimi, neden ve nasıl hedefliyor? | CTI, IR lideri |
| Tactical | Hangi TTP'lere karşı görünürlük/savunma gerekli? | Detection, hunting |
| Technical | Hangi IP, domain, hash hemen aranmalı? | SOC, güvenlik ürünleri |

Bir rapor birden fazla seviyeyi içerebilir. X grubunun phishing campaign'i için operasyon ayrıntısı, TTP'lere karşı detection önerisi ve eğitim yatırımı aynı çalışmada bulunabilir.

## 10. Intelligence lifecycle

### Requirements

Neyi ve neden öğrenmemiz gerektiği belirlenir. Sorun burada net değilse sonraki her aşama gürültü üretir. Örnek PIR: “Önümüzdeki üç ay finans ekibini hedefleyen credential phishing riskini nasıl azaltabiliriz?”

### Collection

İhtiyaca uygun iç/dış veriler toplanır. Her şeyi toplamak veri zenginliği değil, veri kirliliği yaratabilir.

### Processing

Ham veri normalize edilir, yinelenen kayıtlar kaldırılır, zaman ve kimlikler ortak forma çevrilir. Bağlamsız IP listesi henüz intelligence değildir.

### Analysis

Verinin anlamı, güven düzeyi, alternatif açıklamalar ve kurum etkisi değerlendirilir. “Bu actor kesin saldıracak” gibi kanıtsız kesinlik burada doğar.

### Dissemination

Sonuç doğru kişiye uygun ayrıntıda verilir. Yönetim risk ve yatırım; SOC aranacak göstergeler; detection ekibi TTP ve telemetri ister.

### Feedback

Bilgi işe yaradı mı, aksiyon alındı mı, yeni ne öğrenilmeli? Aksiyona dönüşmeyen analiz yalnızca rapordur; feedback yeni requirements'ı besler.

## 11. Kaynak güvenilirliği ile bilgi güveni

Başladığımız fakat tamamlamadığımız başlık budur. Temel ayrım:

- **Kaynak güvenilirliği:** Bu kaynak geçmişte ne kadar doğru ve tutarlıydı?
- **Bilgi güveni:** Bu özel iddia ne kadar kanıtla destekleniyor?

Güvenilir kaynak da yanlış veya eski bilgi paylaşabilir; bilinmeyen kaynak bağımsız kanıtlarla doğru çıkabilir. Kaynak ile iddia ayrı puanlanmalıdır.

## Henüz tamamlanmayan DFIR başlıkları

- Intelligence doğrulama ve enrichment'in sistematik uygulanması
- Alert triage
- Timeline oluşturma
- Evidence preservation ve chain of custody
- Lessons learned
- Disk, memory ve network artifact farkındalığı

Bu maddeler yalnızca yol haritasıdır; işlenmiş ders gibi sunulmamıştır.
