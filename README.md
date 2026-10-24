# Siber Güvenlik Çalışma Notlarım

Bu depo, çalışma sohbetlerindeki ayrıntılı konu anlatımlarını, kritik kavram ayrımlarını ve analist düşünme biçimini kalıcı bir ders arşivine dönüştürür. Kısa konu dosyaları hızlı tekrar; **kapsamlı ders notları** ise ana referanstır.

## Yol haritası ve ana notlar

| Faz | Durum | Kapsamlı not |
|---|---|---|
| 1 — Güvenlik Temelleri ve Ağlar | Tamamlandı | [Ana ders notu](guvenlik-temelleri/kapsamli-ders-notlari.md) |
| 2 — Güvenlik Operasyonları | Tamamlandı | [Ana ders notu](guvenlik-operasyonlari/kapsamli-ders-notlari.md) |
| 3 — Tespit Mühendisliği | Kavramsal bölüm tamamlandı | [Ana ders notu](tespit-muhendisligi/kapsamli-ders-notlari.md) |
| 4 — Windows Güvenliği | 5/10 tamamlandı, park edildi | [İşlenen konular](windows-guvenligi/kapsamli-ders-notlari.md) |
| 5 — Threat Intelligence ve DFIR | 4/10 tamamlandı, park edildi | [İşlenen konular](tehdit-istihbarati-ve-olay-inceleme/kapsamli-ders-notlari.md) |
| 6 — Güvenlikte Makine Öğrenmesi / Tez | Devam ediyor | [Ana ders notu](guvenlikte-makine-ogrenmesi/kapsamli-ders-notlari.md) |
| Ek — AI ve MCP Güvenliği | Bağımsız çalışma alanı | [Konu dizini](ai-ve-mcp-guvenligi/README.md) |

## Notların okuma biçimi

Her ana notta yalnızca kavram tanımı değil, kavramın neden önemli olduğu, hangi kanıtla doğrulanacağı ve hangi aşamada kesin hüküm verilemeyeceği açıklanır. Temel analiz ilkesi şudur:

```text
Gözlenen kanıt → bağlam → alternatif açıklama → ek doğrulama → ölçülü karar
```

Örneğin “zararlı listesinde IP görüldü” gözlemdir; “cihaz ele geçirildi” ise ancak process, identity, dosya ve ağ telemetrisiyle desteklenebilecek sonuçtur. Benzer biçimde servis veya scheduled task oluşturulması persistence hazırlığını; ilgili process'in oluşması gerçek execution'ı gösterir.

## Depo düzeni

- Her klasördeki `kapsamli-ders-notlari.md` o fazın ana anlatımıdır.
- Diğer `.md` dosyaları belirli konular için hızlı tekrar notlarıdır.
- Park edilen fazlarda tamamlanmayan başlıklar açıkça işaretlenmiştir; yol haritası işlenmiş içerik gibi sunulmaz.
- Örnek olaylar eğitim amaçlıdır. Gerçek laboratuvar veya incident çıktısı eklendiğinde ortam, veri kaynağı ve gözlem ayrıca belgelenir.

## Çalışma hedefi

Arşiv; junior SOC/Blue Team temeli, Detection Engineering düşüncesi, Windows telemetrisi, Threat Intelligence/DFIR farkındalığı ve güvenlikte ML tez yönünü birbirine bağlayacak şekilde ilerler. Nihai hedef yalnız terimleri bilmek değil; bir saldırı iddiasını hangi verinin desteklediğini ve hangi belirsizliklerin kaldığını açıklayabilmektir.
