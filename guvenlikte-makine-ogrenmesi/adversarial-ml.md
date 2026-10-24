# Adversarial ML ve Dayanıklılık

Sohbetteki kavramsal açıklamalardan düzenlenmiştir. Sayısal örnekler varsayımsaldır; deney sonucu değildir.

## Evasion attack

Model eğitildikten sonra saldırgan, saldırı davranışını sürdürecek küçük değişikliklerle modelin kararını değiştirmeye çalışır:

```text
Gerçekte saldırı
→ Feature’larda kontrollü değişiklik
→ Model “normal” tahmini yapıyor
```

Örneğin saldırgan trafiğin hızını, paket zamanlamasını veya bazı bağlantı özelliklerini değiştirerek IDS’den kaçmaya çalışabilir. Ama saldırının işlevi devam etmelidir.

## Adversarial example

Modeli yanıltmak amacıyla değiştirilmiş örneğe **adversarial example** denir.

Normal örnek:

```text
Model kararı: Saldırı
```

Değiştirilmiş örnek:

```text
Saldırı hâlâ çalışıyor
Model kararı: Normal
```

Buradaki kritik akademik sorun **gerçekçilik**. Excel tablosundaki sayıları istediğimiz gibi değiştirip modeli kandırabiliriz; fakat ortaya çıkan kayıt ağ dünyasında mümkün olmayabilir.

Örneğin:

- Paket sayısı negatif olamaz.
- Protokol TCP iken yalnızca UDP’ye ait bir alan kullanılamaz.
- Saldırının çalışması için gerekli feature’lar keyfî biçimde değiştirilemez.
- Saldırgan her feature’ı kontrol edemez.

Bu ayrıma:

- **Feature-space attack:** Dataset tablosundaki değerleri değiştirerek saldırı üretmek
- **Problem-space attack:** Gerçek ağ trafiğinde uygulanabilir bir değişiklik yapmak

diyebiliriz.

İyi bir adversarial IDS tezi yalnızca “modeli kandırdım” demez; **üretilen adversarial trafiğin geçerli, uygulanabilir ve hâlâ saldırı niteliğinde olduğunu** da göstermeye çalışır.

## Threat model

Deneyden önce saldırganın yeteneklerini tanımlarız:

- Modelin yapısını biliyor mu?
- Feature’ları biliyor mu?
- Modelin çıktısını sorgulayabiliyor mu?
- Hangi feature’ları değiştirebilir?
- Kaç değişiklik yapabilir?
- Hedefi yalnızca tespitten kaçmak mı?

Modeli ve parametrelerini biliyorsa **white-box**, yalnızca sorgulayabiliyorsa veya çok az bilgiye sahipse **black-box** senaryoya yaklaşırız.

## Robustness ölçümü

Önce temiz test verisindeki başarıyı ölçeriz:

```text
Clean F1: %94
```

Sonra adversarial örneklerle test ederiz:

```text
Adversarial F1: %48
Attack Success Rate: %70
```

Model normal koşullarda başarılı görünürken saldırganın kontrollü değişiklikleri altında ciddi biçimde bozuluyorsa robust değildir.

## Robustness enhancement

Dayanıklılığı artırmak için örneğin:

- Adversarial örneklerle yeniden eğitim
- Kolay değiştirilebilen feature’ları azaltma
- Birden fazla modeli birlikte kullanma
- Geçersiz feature kombinasyonlarını kontrol etme
- Çok belirsiz örnekleri otomatik “normal” kabul etmek yerine incelemeye gönderme

denenebilir.

En bilinen yaklaşım **adversarial training**: Modeli yalnızca temiz örneklerle değil, saldırganın ürettiği değiştirilmiş örneklerle de eğitmek.

Fakat bir saldırı yöntemine dayanıklı hâle gelmek bütün adversarial saldırılara dayanıklı olmak anlamına gelmez.

