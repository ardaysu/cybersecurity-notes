# Bearer Token: Sızıntı ve Erişim Sınırları

## Mantık

Bearer token, elinde bulunduranın ayrıca ayrı bir kriptografik anahtara sahip olduğunu kanıtlamadan sunabildiği erişim bilgisidir. Geçerlilik ve yetki kontrolleri yine uygulanır. Her bearer token her kaynağı açmaz.

Ders benzetmesi: Vestiyer fişi kimdeyse montu istemek için onu sunabilir. Bu benzetme teknik kontrol ayrıntılarını kapsamaz.

## Süre ve kapsam

Ders örneğinde iki token düşünelim:

| Token | İzin | Süre |
|---|---|---|
| A | Bütün raporları okuma ve silme | 30 gün |
| B | Belirli raporu okuma | 10 dakika |

Dar kapsam yapılabilecek işlemleri, kısa ömür kullanım penceresini sınırlar. Sızıntının kendisini önlemez.

## Sızıntı sonrası

İptal mekanizması sisteme bağlıdır. Tokenın süresinin dolması veya iptali daha önce indirilmiş dosyayı geri almaz. Yeni token üretmek eski tokenı otomatik geçersizleştirmeyebilir; eski erişimin reddedildiği doğrulanmalıdır.

Hata kaydına yazılan token logdan kaldırılsa bile önceden kopyalanmış olabilir. Geçmiş kullanımlar incelenmeli, sızıntının kaynağı giderilmelidir.

HTTPS aktarımı korur; uygulamanın tokenı loga yazmasını engellemez.

## Üç ayrı amaç

- Maskeleme: Sırrın kayıtta görünmesini önlemek.
- Süre sonu veya iptal: Sonraki token kullanımını durdurmak.
- İnceleme: Daha önce ne yapıldığını araştırmak.

## Kaynak

[RFC 6750 §1.2 ve §5 — Bearer Token Usage](https://www.rfc-editor.org/rfc/rfc6750.html)

Örnekler ders için hazırlanmıştır; canlı sistemde token üretilmemiş veya iptal edilmemiştir.

[AI ve MCP Güvenliği](README.md)
