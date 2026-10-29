# Token Audience ve Scope

## İki ayrı sınır

- **Audience:** Tokenın hangi alıcı veya servis için verildiğini belirtir.
- **Scope:** Tokenın temsil ettiği erişim kapsamını belirtir.

Bunlar aynı soru değildir: “Nerede kullanılabilir?” ile “Ne için kullanılabilir?” ayrılır. Scope isimlerinin anlamı uygulamaya ve yetkilendirme politikasına bağlıdır.

## İki servis örneği

Kurgusal şirketimizde Rapor API'si ve Ödeme API'si vardır. Token örneğimiz:

```text
Audience: Rapor API'si
Scope: raporları oku
```

| İstek | Değerlendirme |
|---|---|
| Rapor API'sinde rapor okuma | Örnekteki audience ve scope ile uyumlu; diğer kontrollerin de geçmesi gerekir. |
| Ödeme API'sinde işlem | Ödeme API'si hedef alıcı değildir. |
| Rapor API'sinde rapor silme | Audience uygun, fakat silme kapsamı yoktur. |

Tokenın süresinin dolmamış olması bu kontrollerin yerine geçmez. Bilginin token içinde bulunması da yeterli değildir; servis doğrulamalıdır.

## Teknik gösterim

JWT biçimindeki tokenlarda alıcı bilgisi aud claim'iyle temsil edilebilir. Her access token JWT değildir veya istemci tarafından okunabilir değildir. Bilgiler uygun doğrulama mekanizmasıyla edinilmelidir; yalnızca içeriği çözümlemek doğrulamak değildir.

Bu ders tam token doğrulama kontrol listesi değildir.

## Sızmış bearer token örneği

Saldırgan geçerli tokenı ele geçirirse, Rapor API'sine doğru kapsamla erişmeyi deneyebilir. Ödeme API'sinin reddetmesi, rapor okuma riskini ortadan kaldırmaz.

**Tokenın kullanım alanını sınırlamak, o alan içindeki kötüye kullanımı bütünüyle önlemek değildir.**

Bu ayrım ders içi sentezimizdir; ayrıca yeni tez fişi açılmamıştır, çünkü mevcut bearer token notlarıyla örtüşür.

## İnceleme soruları

Token nasıl sızdı? Geçerliyken hangi kaynaklarda kullanıldı? Eski tokenın kullanımı gerçekten durduruldu mu? Servislerin doğrulama davranışı aynı kabul edilmemelidir.

## Kaynaklar

- [RFC 8707 §1 — Resource Indicators](https://www.rfc-editor.org/rfc/rfc8707.html#section-1): Hedef kaynak ile scope ayrımı.
- [RFC 7519 §4.1.3 — Audience](https://www.rfc-editor.org/rfc/rfc7519.html#section-4.1.3): JWT aud tanımı.
- [Bearer token dersimiz](bearer-token-ve-sizinti.md).

Servis adları ve karar tablosu öğretim örneğidir; gerçek API çağrısı yapılmamıştır.

[AI ve MCP Güvenliği](README.md)
