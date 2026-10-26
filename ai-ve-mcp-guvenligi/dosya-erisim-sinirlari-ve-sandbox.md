# Dosya Erişim Sınırları, Path Traversal ve Sandbox

## 1. Kullanıcı onayı neden tek başına sınır koymaz?

Bir AI asistana “Proje klasörümdeki raporu özetle” dediğimizi düşünelim. Agent hangi aracı çağıracağına karar verir; dosyayı gerçekten açan taraf ise aracın arkasındaki program olabilir.

Kullanıcının istediği iş dar kapsamlıdır: belirli klasördeki raporu okumak. Programın işletim sistemindeki izinleri ise daha geniş olabilir. İşlemi onaylamak, programın bütün teknik erişim izinlerini otomatik olarak o raporla sınırlandırmaz.

Bunu bir anahtar örneğiyle düşünebiliriz: Birine “Masamdaki defteri getir” demek, elindeki anahtarın açabildiği diğer kapıları kilitlemez. Yapılması istenen iş ile yapılabilecek işlemler farklıdır.

**Temel ayrım: Kullanıcı talebi görevi tanımlar; erişim kontrolü hangi kaynaklara hangi işlemlerin uygulanabileceğini sınırlar.**

## 2. Çalışma dizini bir güvenlik sınırı değildir

Örnek klasörler:

```text
Belgeler/
├── Projem/
│   └── rapor.txt
└── Ozel/
    └── sifreler.txt
```

Programın çalışma dizini `Projem` olabilir. Çalışma dizini, göreli dosya yollarının başlangıç noktasıdır. Programın yalnızca bu klasöre erişebileceği anlamına gelmez.

Programı çalıştıran hesabın izinleri `Ozel` klasörüne de erişmeye elveriyorsa, ayrıca uygulanan bir sınır bulunmadığında program başka bir dosyayı da açabilir.

**Çalışma dizini başlangıç noktasıdır; tek başına güvenlik sınırı değildir.**

Bir klasörü listeleyebilmek ile içindeki her dosyanın içeriğini okuyabilmek de farklıdır. Unix benzeri sistemlerde klasör listeleme, yol üzerindeki klasörlerden geçiş ve hedef dosyayı okuma izinleri ayrı değerlendirilir. Dolayısıyla “ana dizini okuyabiliyor, bütün dosyaları kesin okuyabilir” diye genelleme yapılmaz.

## 3. Path traversal mantığı

`Projem` içinden şu yolların kullanıldığını düşünelim:

| Yol | Anlamı |
|---|---|
| `rapor.txt` | Bulunulan klasördeki raporu hedefler. |
| `../Ozel/sifreler.txt` | Bir üst klasöre çıkar ve Ozel içindeki dosyayı hedefler. |

`..`, dosya yollarında bir üst dizini ifade eder. Bu kullanım kendi başına kötü niyetli değildir; normal dosya işlemlerinde de bulunur.

Sorun, dışarıdan alınan bir dosya yolunun izin verilen alanı aşmasına rağmen program tarafından kabul edilmesidir. Bu kapsam dışına çıkma zafiyeti path traversal olarak adlandırılır.

Dışarıdaki dosyanın hedeflenmesi, dosyanın mutlaka okunacağını göstermez. İşletim sistemi izinleri, sandbox veya başka bir kontrol erişimi engelleyebilir.

## 4. Metin başlangıcı ile klasör üyeliği aynı değildir

Sınır denetimi şöyle tasarlanmış olsun:

> Yolun başı /Belgeler/Projem ise izin ver.

Bu kontrol aşağıdaki iki yolu da kabul edebilir:

```text
/Belgeler/Projem/rapor.txt
/Belgeler/Projem-Ozel/sifreler.txt
```

Oysa klasörler yan yanadır:

```text
Belgeler/
├── Projem/
└── Projem-Ozel/
```

`Projem-Ozel`, `Projem` klasörünün altı değildir. Sadece isimleri aynı karakterlerle başlar. Bu örnekte `..` kullanmaya gerek kalmadan zayıf bir sınır kontrolü yanlış karar verebilir.

**“Adı benziyor” ile “izin verilen klasörün içinde” aynı şey değildir.**

Uygulama, hedefin gerçekten izin verilen dizin ağacında kalmasını denetlemelidir. Gerçek uygulamada sembolik bağlantılar ve kontrol ile kullanım arasında dosya sisteminin değişmesi gibi ayrıntılar da önemlidir; yalnızca metin karşılaştırması genel bir güvenlik çözümü değildir.

## 5. Sandbox ne sağlar?

Bu derste sandbox'ı, programın erişebileceği kaynakları sınırlayan çalışma ortamı olarak ele alıyoruz. Örnek politika:

> Program Projem içindeki dosyaları okuyabilir; Ozel klasörüne erişemez.

Araç tarafındaki yol kontrolü ile sandbox farklı katmanlardır. Yol kontrolü istenen hedefi değerlendirir. Uygun yapılandırılmış sandbox ise programın gerçekleştirebileceği erişimi sınırlar. Araçta hata olması durumunda ikinci bir engel sağlayabilir.

Her sandbox aynı korumaları sağlamaz. Politikanın kapsamı, uygulanma biçimi ve doğru yapılandırılması belirleyicidir. Ayrı bir process başlatmak da tek başına dosya erişimini daraltmaz.

## 6. Güvenlik kontrolünü nasıl sınarız?

Eğitim ortamında gerçek şifre yerine sahte içerikli bir test dosyası kullanırız:

| Deneme | Beklenen gözlem | Değerlendirme |
|---|---|---|
| Sandbox kapalı, kapsam dışı dosyaya erişim | Örneğimizde erişim gerçekleşir. | Sorunun gerçekten üretilebildiği görülür. |
| Sandbox açık, izinli rapora erişim | Normal rapor okunur. | Korumanın meşru işi bozmadığı görülür. |
| Sandbox açık, kapsam dışı dosyaya erişim | Erişim engellenir. | Politikanın istenmeyen erişimi sınırlandırdığı araştırılır. |

Hem özel dosya hem proje raporu okunamıyorsa çözümü başarılı sayamayız. İzinli iş bozulmuştur.

Öte yandan dosyanın okunamaması tek başına sandbox'ın engellediğini kanıtlamaz. Dosya bulunamamış, program hata vermiş veya istek yanlış hazırlanmış olabilir. Sonuçla birlikte hata nedeni ve mümkün olduğunda erişim reddi kayıtları incelenir.

**Başarılı kontrol, izinli işi çalıştırırken izinsiz işlemi engellemeyi hedefler.**

## 7. MCP araştırmasıyla bağlantı

MCP-FSD çalışması, yerel MCP sunucularında araçların açıklanan kapsamı ile sunucu sürecinin gerçek dosya erişimi arasındaki farkı inceler. Üç koşullu test yaklaşımı, sızıntının üretilebilmesini, normal işin korunmasını ve sınırlandırmanın etkisini ayrı değerlendirmeye yardımcı olur.

Bu sayfadaki klasörler ve anahtar benzetmesi ders için hazırlanmış açıklama örnekleridir. Burada gerçek bir laboratuvar çalıştırılmamış, deney sonucu üretilmemiştir.

## Kaynak

- Huang ve arkadaşları, [“My Credentials, Please”: Detecting Filesystem Capability Laundering in MCP Servers at Scale](https://arxiv.org/html/2610.22301v1), ön baskı.
- Bu sayfa, 26 Ekim 2026 tarihli soru-cevap dersindeki açıklama ve düzeltmelerden düzenlenmiştir.

[AI ve MCP Güvenliği](README.md)
