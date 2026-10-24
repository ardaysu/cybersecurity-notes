# Engelleme Sonrası Olay İnceleme: Kanıt ve Şüphe

## IPS engellediyse neden inceleme sürer?

IDS şüpheli etkinliği tespit edip uyarı üretir. IPS tespitle birlikte engelleme uygulayabilir. SIEM farklı kaynaklardan gelen kayıtları ilişkilendirerek olayın daha geniş bağlamını görmeye yardımcı olur. Ürünlerin yetenekleri örtüşebilir; bunlar temel rolleridir.

Bir isteğin engellenmesi, önceki bütün girişimlerin de engellendiğini göstermez. Başarılı erişim daha önce gerçekleşmiş, başka bir oturum devam ediyor veya başka bir sistem etkilenmiş olabilir. Uyarının yanlış pozitif olup olmadığı da kontrol edilir.

## Eğitim senaryosu

| Zaman | Gözlenen kayıt |
|---|---|
| 10.01 | Bir hesaba aynı IP'den 20 başarısız giriş |
| 10.03 | Aynı hesaba aynı IP'den başarılı giriş |
| 10.05 | Hesabın normalden daha fazla dosya indirmesi |
| 10.07 | IPS'nin aynı IP'den gelen şüpheli isteği engellemesi |

Bu kayıtlar hesap ele geçirme şüphesi doğurur. Ancak başarısız girişlerden sonra başarı görülmesi tek başına parola kırıldığını veya dosyaların saldırgan tarafından indirildiğini kanıtlamaz.

## Alternatif açıklama ve ek kanıt

Yakın zamandaki parola değişikliği, eski parolayı kullanan bir uygulamanın başarısız girişlerini açıklayabilir. Girişin cihaz, oturum ve kimlik doğrulama ayrıntıları; parola değişikliği geçmişi ve dosya erişim kayıtları birlikte incelenir.

İndirilen dosyaların iş bağlamına da bakılır. İK hesabının finans dosyalarına erişmesi araştırma sebebidir; ortak görev veya geçerli erişim ihtiyacı da olabilir. Anormallik, otomatik olarak ihlal değildir.

**Bir hesabın dosyayı okumaya teknik olarak yetkili olması, işlemi hesabın gerçek sahibinin yaptığı veya işlemin meşru olduğu anlamına gelmez.**

## Analiz sonucu nasıl yazılır?

- **Gözlenen:** Başarısız ve başarılı girişler ile dosya indirme kayıtları var.
- **Hipotez:** Hesap ele geçirilmiş olabilir.
- **Gerekli kanıt:** Cihaz/oturum, MFA, dosya listesi, işlem bağlamı ve ilişkili ağ kayıtları.
- **Amaç:** Etkiyi, kapsamı ve kök nedeni incelemek; tekrar riskini azaltacak aksiyonları belirlemek.

Kök neden giderilmezse risk sürebilir; tekrar saldırı olması kaçınılmaz diye ifade edilmez. Saldırganın gerçek kimliğini belirlemek her zaman mümkün olmayabilir.

## Kaynak

- [NIST SP 800-94: IDS, IPS ve SIEM ilişkisi](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=50951)
