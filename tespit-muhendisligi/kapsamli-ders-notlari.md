# Faz 3 — Tespit Mühendisliği

> **Durum:** Kavramsal bölüm tamamlandı  
> **Amaç:** Bir saldırı fikrini ölçülebilir veri gereksinimine, test edilebilir kurala ve sürdürülebilir detection'a çevirmek.

## 1. Detection engineering nedir?

Detection engineering bir sorgu yazmaktan daha geniştir. Tehdit hipotezini, gerekli telemetriyi, mantığı, testi, yayınlamayı, tuning'i ve yaşam döngüsünü kapsar.

Kötü başlangıç: “PowerShell'i yakalayalım.”  
İyi başlangıç: “Kullanıcı cihazında Office'in gizli/encoded PowerShell başlatıp dış ağla iletişim kurduğu olası phishing execution zincirini tespit etmek istiyoruz.”

İkinci ifade hedef davranışı, kapsamı ve doğrulama verisini tarif eder.

## 2. Use case tasarımı

Bir use case şu sorulara cevap vermelidir:

- Hangi tehdit veya davranış hedefleniyor?
- Hangi varlıklar ve platformlar kapsamda?
- Hangi log kaynakları ve alanlar gerekiyor?
- Başarılı tespit nasıl görünür?
- Bilinen benign senaryolar neler?
- Alarmın sahibi ve response adımı kimde?
- Ölçülecek kalite kriteri nedir?

Telemetri yoksa kural yazmak görünürlük yaratmaz. Bu durumda sonuç “detection gap” değil, önce “visibility gap” olabilir.

## 3. MITRE ATT&CK technique–telemetry eşleştirmesi

ATT&CK tekniği “hangi saldırgan davranışı?” sorusunu cevaplar. Telemetri eşleştirmesi ise “bunu nerede görebilirim?” sorusudur.

Örneğin Scheduled Task/Job için:

- Security 4698/4702
- Task Scheduler Operational logları
- Registry veya task dosyası değişiklikleri
- Creator process
- Task tetiklendiğinde oluşan process

Sadece 4698'e bağlı kural görevin oluşturulduğunu görür; gerçekten çalıştığını göstermez. Coverage, tekniğin adını etikete eklemek değil, davranışın gerekli aşamalarını görebilmektir.

## 4. Sigma kural yapısı

Sigma, SIEM'den bağımsız detection tanımıdır. Tipik bölümler:

```yaml
title: Suspicious Encoded PowerShell From Office
logsource:
  category: process_creation
  product: windows
detection:
  office_parent:
    ParentImage|endswith:
      - '\\winword.exe'
      - '\\excel.exe'
  powershell_child:
    Image|endswith: '\\powershell.exe'
    CommandLine|contains:
      - '-enc'
      - '-EncodedCommand'
  condition: office_parent and powershell_child
falsepositives:
  - Approved Office automation
level: high
```

Sigma dosyası tek başına üretim tespiti değildir. Backend dönüşümü, alan eşleme, veri kalitesi, SIEM sözdizimi, performans ve false-positive testi gerekir.

## 5. SIEM sorgu mantığı

KQL, SPL veya başka bir dil değişse de temel düşünce aynıdır:

1. Veri kaynağını ve zaman aralığını daralt.
2. İlgili event/alanları filtrele.
3. Alanları normalize et.
4. Kullanıcı, cihaz, process veya zaman üzerinden ilişkilendir.
5. Sonucu analistin karar verebileceği alanlarla göster.

Yalnızca eşleşme sayısı değil; `timestamp`, `host`, `user`, `parent`, `process`, `command_line`, `destination` ve kuralın neden eşleştiği görünmelidir.

## 6. Davranış kuralı ve IOC kuralı

Hash veya IP kuralı hızlı değer üretir fakat saldırgan göstergesi değişince kırılır. Davranış kuralı daha dayanıklıdır ama daha çok veri, tuning ve bakım ister.

Bu bir “biri doğru, diğeri yanlış” seçimi değildir:

- Bilinen aktif IOC'leri hızlıca taramak ve engellemek kısa vadeli kapsama sağlar.
- Aynı saldırı amacını farklı altyapıyla yakalayacak davranış kuralı uzun vadeli yatırım sağlar.

Pyramid of Pain açısından hash saldırgan için ucuz değişikliktir; TTP'yi değiştirmek daha maliyetlidir. Savunma, mümkün olduğunca yukarı katmanlara çıkarken IOC'nin hız avantajını kaybetmemelidir.

## 7. Detection coverage ve fidelity

- **Coverage:** Hangi tehditlerin, tekniklerin, varlıkların ve saldırı aşamalarının görülebildiği.
- **Fidelity:** Alarmın gerçeği ne kadar güvenilir ve eyleme dönük temsil ettiği.

Çok geniş bir kural coverage artırırken gürültü yaratabilir. Aşırı spesifik kural fidelity yüksek görünürken varyasyonları kaçırabilir. Amaç tek metriği maksimum yapmak değil, risk ve operasyon kapasitesine uygun dengeyi kurmaktır.

## 8. Korelasyon ve risk tabanlı alarm

Tek bir zayıf sinyal yerine olaylar puanlanabilir:

| Sinyal | Örnek risk |
|---|---:|
| Encoded PowerShell | 25 |
| Office parent | 30 |
| Yeni domain bağlantısı | 20 |
| Defender ayarı değişikliği | 40 |

Toplam puan eşik aşınca alarm üretilebilir. Böylece her davranışın mutlaka aynı sorguda bulunması şart olmaz. Ancak puanlar bilimsel gerçek değil, test edilmesi gereken operasyonel varsayımlardır.

## 9. Test ve doğrulama

Bir detection için en az şu testler gerekir:

- **Positive test:** Beklenen saldırı örneği alarm üretiyor mu?
- **Negative test:** Benign örnek gereksiz alarm üretiyor mu?
- **Variant test:** Küçük teknik değişikliklerde kural çalışıyor mu?
- **Data quality test:** Gerekli alanlar gerçekten dolu mu?
- **Performance test:** Sorgu makul sürede ve maliyetle çalışıyor mu?
- **Regression test:** Tuning sonrası eski doğru örnekler hâlâ yakalanıyor mu?

Sadece örnek saldırıyı yakalamak, üretime hazır olduğunu kanıtlamaz.

## 10. Tuning, suppression ve allowlist

Tuning'in amacı alarm sayısını düşürmek değil, karar kalitesini artırmaktır.

- **Allowlist:** Doğrulanmış benign varlık veya davranışı kapsam dışı bırakır.
- **Suppression:** Aynı olayın belirli sürede tekrar alarm üretmesini sınırlar.
- **Threshold:** Belirli sayı/zaman koşulunu arar.

Şirketin kullandığı meşru hizmeti hariç bırakmak bazen doğrudur; fakat geniş domain, ortak IP veya yalnızca process adına dayalı istisna saldırganın saklanabileceği kör nokta yaratabilir. İstisna mümkün olduğunca kimlik, imza, yol, cihaz grubu ve onaylı kullanım bağlamıyla dar tutulmalıdır.

## 11. Detection-as-code

Detection'lar kod gibi yönetildiğinde:

- Git geçmişiyle kim/ne zaman/neden değişti görülür.
- Pull request ile gözden geçirilir.
- Otomatik syntax ve test kontrolleri çalışır.
- Sürüm, sahiplik ve rollback mümkün olur.
- Dokümantasyon kuraldan ayrılmaz.

Kural dosyasına yalnızca sorgu değil; amaç, veri kaynağı, ATT&CK mapping, false positive, severity, test örnekleri ve response yönlendirmesi eklenmelidir.

## 12. Detection gap mi visibility gap mi?

Alarm gelmemesinin olası nedenleri:

1. Davranış için kural yoktur — detection gap.
2. Kural vardır ama gerekli log toplanmıyordur — visibility gap.
3. Log gelir ama alan mapping'i bozulmuştur — processing/data quality gap.
4. Kural aşırı dar veya yanlış mantıklıdır — logic gap.
5. Kural devre dışı veya zamanlaması bozuktur — operational gap.

Sorunu doğru adlandırmadan doğru yatırım yapılamaz.

## 13. Capstone düşünme şablonu

Bir use case'i uçtan uca yazarken:

```text
Tehdit hipotezi
→ ATT&CK davranışı
→ gerekli telemetri ve alanlar
→ sorgu/Sigma mantığı
→ benign senaryolar
→ pozitif/negatif/varyant testleri
→ severity ve analist çıktısı
→ response playbook
→ metrikler ve gözden geçirme tarihi
```

İyi detection, “çalışan sorgu” değil; doğru tehdidi yeterli bağlamla ve sürdürülebilir biçimde operasyon ekibine taşıyan üründür.
