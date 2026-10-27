# Parola Saldırıları ve Tespit: Hesaplar Arasındaki Örüntü

## Üç yöntemin ayrımı

| Yöntem | Mantık |
|---|---|
| Password guessing | Bilinmeyen parolayı adaylarla tahmin etme |
| Password spraying | Bir veya birkaç yaygın parolayı çok sayıda hesapta deneme |
| Credential stuffing | Başka sızıntılardan elde edilen kullanıcı adı–parola çiftlerini yeniden kullanma |

Günlük dilde yoğun parola tahminine brute force denebilir. MITRE ATT&CK'te Brute Force (T1110), bu yöntemleri ve password cracking'i kapsayan üst tekniktir.

Spraying hesap başına denemeleri düşük tutarak kilitleme eşiklerinden kaçınmayı hedefleyebilir. Credential stuffing ise kullanıcıların farklı hizmetlerde aynı parolayı kullanmasından yararlanır.

## Ders senaryosu

Aşağıdaki örnek varsayımsaldır; gerçek log incelemesi yapılmamıştır:

- Aynı IP'den 10 dakikada 60 farklı hesaba başarısız giriş.
- Her hesapta yalnızca bir veya iki deneme.
- Denenen parolalar kayıtlarda yok.

Bu örüntü spraying şüphesi doğurur. Ancak aynı parolanın tekrarlandığı kayıtlardan görülemediği için kesin sınıflandırma yapılamaz. Credential stuffing veya başka etkinlikler de benzer görünüm oluşturabilir.

**Gözlem ile yorum ayrılır:** “60 farklı hesapta başarısız giriş var” gözlemdir; “password spraying yapılıyor” bu gözlemin desteklediği hipotezdir.

## Tek hesap eşiğinin kör noktası

“Bir hesapta beş başarısız giriş olursa alarm üret” kuralı bu senaryoyu kaçırabilir. Hiçbir hesap beş denemeye ulaşmazken toplamda çok sayıda hesap hedeflenmiştir.

Ders sırasında verilen doğru örnek: Her hesapta dört deneme yapılması da beş denemelik hesap eşiğinin altında kalabilir. Bu, belirli eşik altında kalan işlemlerin toplam etkisini görmenin önemini anlatır; dört veya beş evrensel güvenlik eşikleri değildir.

Hesap başına başarısızlık sayısının yanında, belirli zaman aralığında aynı kaynaktan hedeflenen farklı hesap sayısı incelenebilir. Toplam istek sayısı ile benzersiz hesap sayısı aynı ölçüm değildir.

## IP'ye göre gruplama neden yeterli değil?

- Şirket ağı veya proxy arkasındaki çok sayıda meşru kullanıcı aynı IP'yi paylaşabilir.
- Saldırgan kaynak IP'lerini değiştirebilir.
- Ortak IP tek başına ortak aktör veya kötü niyet kanıtlamaz.

Bu nedenle zaman örüntüsü, mevcut cihaz/istemci bilgileri ve başarılı girişlerin devamındaki davranışlar bağlama eklenir. Bu alanlar her kayıtta bulunmayabilir; veri kaynağı kontrol edilmelidir.

Çok sayıda başarısız girişten sonra başarı görülmesi araştırma önceliğini artırabilir, ancak hesabın kesin ele geçirildiğini tek başına göstermez. Beklenen kullanıcı davranışı ve alternatif açıklamalar da değerlendirilir.

## Alarmın anlamı

Alarm, araştırılması gereken bir örüntüye işaret eder; doğrulanmış saldırı sonucu değildir. Tespit mantığında hangi log kaynağının kullanıldığı, hangi alanların gerektiği, zaman penceresi, eşik ve yanlış pozitif koşulları açıklanmalıdır.

Parolaları açık metin kaydetmek bu ayrımı yapmanın uygun yolu değildir. Analiz ihtiyacı, hassas kimlik bilgilerinin gereksiz toplanmasını haklı çıkarmaz.

Bu ders savunma ürününün yapılandırıldığı veya kuralın gerçek veride test edildiği bir laboratuvar değildir.

## Kaynaklar

- [MITRE ATT&CK — Brute Force T1110](https://attack.mitre.org/techniques/T1110/)
- [Password Guessing T1110.001](https://attack.mitre.org/techniques/T1110/001/)
- [Password Spraying T1110.003](https://attack.mitre.org/techniques/T1110/003/)
- [Credential Stuffing T1110.004](https://attack.mitre.org/techniques/T1110/004/)

Tanımlar MITRE'ye dayanır; log örneği ve eşik tartışması 27 Ekim 2026 dersimizdeki açıklama ve yorumlardır.

[Güvenlik Operasyonları](README.md)
