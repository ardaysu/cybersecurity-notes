# Process, thread ve token

## Temel fikir

- **Process:** Çalışan programın bellek ve kaynaklarıyla birlikte oluşturduğu çalışma alanıdır.
- **Thread:** Process içindeki işi fiilen yürüten akıştır. Bir process birden fazla thread barındırabilir.
- **Token:** İşlemin hangi kullanıcı/grup kimliğiyle ve hangi yetkilerle hareket edebileceğini belirleyen güvenlik kimliğidir.

## Token türleri

- **Primary token:** Process'in temel güvenlik kimliğidir.
- **Impersonation token:** Bir thread'in geçici olarak başka bir kimlik adına işlem yapabilmesini sağlar. Erişim kontrolünde thread'in impersonation token'ı etkili olabilir.

## Analiz yaklaşımı

Bir process'in yalnızca adına veya kullanıcı adına bakmak yeterli değildir. Şunlar birlikte değerlendirilir:

- Parent process ve başlatılma yöntemi
- Komut satırı
- Dosya yolu ve dijital imza
- Kullanıcı, yetki ve integrity level
- Thread ve token davranışları
- Sonraki dosya, registry ve ağ hareketleri
- İşlemin kurumda beklenen bir davranış olup olmadığı

## Process injection ve token kötüye kullanımı

Meşru görünen bir process'in içine kod yerleştirilmesi, zararlı davranışın o process bağlamında yürütülmesine yardımcı olabilir. Amaç savunmadan kaçınmak ve bazı senaryolarda daha yüksek yetkili bağlamdan yararlanmak olabilir.

> Bir process'in adı meşru diye içindeki davranış otomatik olarak meşru kabul edilmez.

Process injection tek başına yeniden başlatma sonrasında kalıcılık sağlamaz. Persistence için ayrıca service, scheduled task veya Run key gibi bir mekanizma gerekir.

## Çalışılan vaka

```txt
10:01  winword.exe → powershell.exe        User: Ayse / Medium
10:02  powershell.exe → SYSTEM prosesine erişim
10:02  SYSTEM prosesi içinde yeni thread
10:03  SYSTEM prosesi → \\DC01\ADMIN$ bağlantısı
```

**Yorum:** Zincir; olası process injection veya token kötüye kullanımı, SYSTEM bağlamından yararlanma ve yönetim paylaşımı üzerinden yanal hareket ihtimalini destekler. Tek bir event yerine olayların sırası ve bağlamı değerlendirilmelidir.

## Analiz yaklaşımı

- “SYSTEM veya svchost gördüm, kesin güvenlidir” dememek
- Şüpheli davranışı fark edip bağlam olmadan kesin saldırı hükmü vermemek
- Process → thread/token → yetki → ağ hareketi zincirini birlikte değerlendirmek
- Persistence ile privilege escalation / defense evasion kavramlarını ayırmak
