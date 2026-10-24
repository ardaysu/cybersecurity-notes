# IOC ve IOA Farkı

## IOC — Indicator of Compromise

Saldırıda kullanılan veya geride bırakılan teknik değerdir: hash, IP, domain, URL, dosya yolu, registry değeri ve e-posta/attachment bilgisi. Kurum genelinde hızlı arama ve kapsam belirleme sağlar.

IOC'ler kolay değişebilir: dosyadaki küçük değişiklik hash'i, yeni altyapı IP/domain'i değiştirir. IOC değerlendirilirken kaynak güvenilirliği, confidence, first/last seen, bağlam ve yaş dikkate alınır. IOC'lerin zamanla değer kaybetmesi indicator decay olarak ifade edilebilir.

## IOA — Indicator of Attack

Saldırganın gerçekleştirdiği davranış veya örüntüdür: Office → hidden/encoded PowerShell, Run key persistence, password spraying, ayrıcalıklı grup üyeliği, LSASS erişimi, beaconing veya log temizleme.

IOA teknik değer değişikliklerine daha dayanıklıdır; ancak fazla geniş davranış kuralları gürültü üretir. Birden fazla anlamlı koşulu ilişkilendirmek güveni yükseltir, aşırı daraltmak ise küçük değişikliklerle atlatılmaya yol açabilir.

## Temel ayrım ve kullanım

- **IOC:** Saldırgan hangi teknik izi kullandı/bıraktı?
- **IOA:** Saldırgan nasıl bir davranış gerçekleştirdi?

IOC'ler kurum genelinde aranır; farklı IOC'lerle aynı saldırı davranışını bulmak için IOA tabanlı hunting yapılır. Aynı cihazda IOC ve IOA'nın birleşmesi olayın güvenini ve önceliğini artırır.
