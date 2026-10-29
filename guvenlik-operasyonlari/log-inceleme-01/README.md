# Log İnceleme 01 — Girişten Dosya Aktarımına

Bu çalışma tamamen kurgusal kayıtlar üzerinde, soru-cevap yöntemiyle yürütülmüştür. Canlı sistem erişimi veya gerçek olay müdahalesi yapılmamıştır. Devam dersinde kurgusal CSV üzerinde yerel tespit örneği çalıştırılmıştır.

[Örnek kayıtları aç](olaylar.csv)

## Ortam ve kayıtların anlamı

- 203.0.113.10 kurumun ortak internet çıkışıdır; farklı çalışanlar bu adresi paylaşabilir.
- 198.51.100.24 kurumun tanımlı çıkışlarından değildir. Bu tek başına kötü niyet kanıtı değildir.
- Deniz finans ekibindedir ve finans dosyalarına okuma yetkisi vardır.
- Bilinen cihazı LAPTOP-D'dir. Olağan indirme hacmi oturum başına 1–5 MB'dır; bu bir bağlam bilgisidir, evrensel alarm eşiği değildir.
- Saatler aynı gün ve saat dilimine aittir; örnekte saatlerin eşzamanlı olduğu kabul edilir.
- IP'ler dokümantasyon aralıklarından, dış hedef örnek alan adından seçilmiştir.

CSV'deki session_id aynı kullanıcıya ait farklı oturumları ayırır. Başarısız girişlerde oturum oluşmadığından bu alan boş olabilir. bytes alanı olay türüne göre yorumlanır; E13'te hedefe iletilen istek gövdesini ifade eder.

## Üç oturumu birbirinden ayırmak

| Oturum | Kullanıcı ve bağlam | İlk değerlendirme |
|---|---|---|
| S100 | Deniz; bilinen cihaz; kurum çıkışı; parola ve MFA | Verilen bağlamla daha uyumlu; kesin güvenli olduğu sonucu çıkarılmaz. |
| S200 | Berk; MFA doğrulamalı parola sıfırlama sonrası kurum çıkışından giriş | Parola sıfırlama tek başına kötü niyet göstergesi değildir. |
| S300 | Deniz; farklı kaynak; bilinmeyen cihaz; yalnızca parola; büyük indirme | Öncelikli araştırma adayı. |

Dersin ilk yanıtında S200 yazılmış, devamında doğru olarak S300'e ait göstergeler açıklanmıştır. Oturum etiketleri kontrol edilerek karışıklık düzeltilmiştir.

## Zaman çizelgesi

| Kanıt | Olay | Yorum sınırı |
|---|---|---|
| E03–E07 | Aynı IP'den farklı hesaplara başarısız girişler | Spraying şüphesi doğurabilir; parola bilgisi olmadığından yöntem kesinleştirilemez. |
| E10 | S300'de yalnızca parolayla başarılı giriş | MFA kullanımı yok; MFA atlatıldığı kanıtlanmış değildir. |
| E11 | Finans klasörü listelendi | Hesabın mevcut izniyle uyumludur; işlemi gerçek sahibinin yaptığı anlamına gelmez. |
| E12 | 84 MB indirme başarılı kaydedildi | Olağan hacim üzerinde. Başlangıç verisi aktarım hedefinin kontrolünü açıklamaz. |
| E13 | Dış hedefe gönderim engellendi, iletilen gövde 0 bayt | Yalnızca bu girişim hakkında bilgi verir. Diğer aktarım yollarını kapsamaz. |
| E14 | S100'de bilinen cihazdan dosya indirildi | Aynı hesapta iki oturum vardır; işlemler yalnızca kullanıcı adına göre birleştirilmemelidir. |

## İnceleme sırasında verilen ek kanıtlar

Aşağıdaki bilgiler CSV'nin ilk sürümünde yoktur; ders sırasında eklenen kurgusal doğrulamalardır:

1. Uygulama kaydı E12'deki 84 MB dosya yanıtının doğrudan 198.51.100.24 istemci bağlantısına gönderildiğini doğrular.
2. Bu bağlantı kurumun yönetilen çalışma ortamlarından biri değildir; ilk aşamada kontrol eden kişi bilinmez.
3. Deniz'e önceden bilinen telefonundan ulaşılır ve Deniz bu işlemleri yapmadığını söyler.
4. S300'ün cihazı kurum envanterinde bulunmaz.

Bu ek bilgileri ilk CSV'de zaten varmış gibi sunmamak önemlidir.

## İndirme ile dışarı gönderim arasındaki ayrım

E13'ün engellenmesi, E12'deki dosya aktarımını geri almaz. Dosya dışarıdaki bir istemciye indirilmişse sonraki gönderimden önce kurum sınırını aşmış olabilir.

Ek kanıttan önce yalnızca uygulamanın başarılı indirme kaydı bilinmektedir. Ek kanıtla dış istemci bağlantısına aktarım doğrulanır. İstemcinin saldırgana ait olduğu ise sırf IP dışarıda diye kesinleşmez.

**Doğrulanan veri hareketi ile yetkisiz veri sızdırma değerlendirmesi ayrı yazılır.**

Dış hedefin güvenilirliğini araştırmak faydalıdır, ancak dosyanın daha önce nereye aktarıldığı sorusunun yerine geçmez.

## Hangi kaydı neden isteriz?

| Kaynak | Bilgi | Cevapladığı soru |
|---|---|---|
| Dosyayı sunan uygulama | İstek/oturum kimliği, dosya kimliği, yanıt bağlantısı, aktarılan miktar | E12 hangi bağlantıya ne gönderdi? |
| Ağ geçidi veya proxy | Kaynak–hedef, yön, zaman ve aktarım bilgileri | Hangi sınırdan trafik geçti? |
| Yönetilen istemci, erişebiliyorsak | Dosya oluşturma, kopyalama, process ve ağ olayları | Dosya kaydedildi mi, devamında hangi hareketler var? |
| Kimlik sistemi | Oturum oluşumu, doğrulama yöntemi ve mevcut cihaz bilgileri | S300'ün kimlik bağlamı ne? |
| Veri sınıflandırması | Dosyanın hassasiyeti ve iş bağlamı | Olası etki ne kadar büyük? |

Dosyanın içeriği hassasiyeti anlamaya yardımcı olur; işlemi kimin yaptığını tek başına kanıtlamaz. Her incelemede hassas dosyanın tamamını açmak gerekmeyebilir.

Hedef cihaz denetimimizde değilse yolculuğun tamamını göremeyebiliriz. Kopyalama kaydı bulunmaması, kopyalama yapılmadığının kanıtı değildir.

## Kullanıcıdan doğrulama

Deniz'e şüpheli oturumdan bağımsız, önceden bilinen bir kanal üzerinden ulaşılır. Saat, dosya, cihaz ve işlem amacı sorulur. Açıklama kimlik ve cihaz kayıtlarıyla karşılaştırılır.

Aynı IP'deki diğer faaliyetler kapsam araştırması için değerlendirilir; ancak aynı IP aynı kişiyi göstermez. Oturum, hesap, cihaz ve zaman bağlarıyla desteklenmelidir.

## Araştırma ve sınırlama kararı

Deniz'in işlemleri reddetmesi, cihazın bilinmemesi ve dış istemciye dosya aktarımı birlikte değerlendirildiğinde S300 için erişimi sınırlama önerisi gerekçelenir. Araştırmanın bitmesini beklemek zorunlu değildir.

Önerilen yaklaşım:

- S300 oturumunu ve ilgili erişim bilgilerinin kullanımını uygun mekanizmalarla sonlandırmayı değerlendirmek.
- Giriş, dosya ve proxy kayıtları ile oturum/istek kimliklerini korumak.
- Başka oturum, hesap ve dosyalara yayılımı araştırmak.
- S100'ü tanıdık göründüğü için otomatik güvenli ilan etmemek.
- İlgili hesabın kimlik bilgilerini ve oturum politikasını olayın kapsamına göre değerlendirmek.

Parola değişimi her sistemde mevcut oturumları kapatmaz. Kanıt koruma ve sınırlama paralel yürüyebilir; gerçek uygulama kurumun yetki ve olay müdahale prosedürüne bağlıdır.

**Örnek karar cümlesi:** “Deniz'in reddettiği ve bilinmeyen cihazdan açılan S300 oturumunda dış istemciye dosya aktarımı doğrulandığı için oturumun sınırlandırılmasını; kanıtların korunarak kapsam incelemesinin sürdürülmesini öneriyorum.”

Bu karar kurgusal ortam için analist önerisidir; müdahale yapılmış değildir.

## Sonraki uygulama

[Tespit kuralı tasarımı ve testleri](tespit-kurali.md) devam dersinde tamamlandı. Kayan pencere ve başarı korelasyonu kurgusal CSV üzerinde çalıştırıldı; kod, dört test ve sonuç dosyası aynı klasördedir. Üretim ortamında uygulanmamıştır.

[Güvenlik Operasyonları](../README.md)
