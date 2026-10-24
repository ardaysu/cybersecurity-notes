# Detection Rule Geliştirme

Use case'ten önce geniş temel davranış oluşturuldu, gerçek veri üzerinde hacim ve meşru örnekler görüldükçe şüpheli koşullarla daraltıldı. Geniş ilk taslak doğrudan yüksek öncelikli production alarmı yerine hunting/backtesting/shadow mode'da değerlendirilebilir.

## Geliştirilen mantık

1. Office parent → PowerShell child
2. Hidden, encoded veya download göstergelerinden en az biri
3. Aynı PowerShell'in kısa sürede executable oluşturması
4. PowerShell'in child olarak payload'ı çalıştırması
5. Payload'ın zararlı dış hedefe bağlanması

## Korelasyon

- Aynı process davranışları ProcessGuid ile bağlanır.
- Child process, ProcessGuid ve ParentProcessGuid eşleşmesiyle parent'a bağlanır.
- Aynı host, doğru olay sırası ve makul zaman penceresi korunur.
- Aynı dosya adı, kullanıcı veya gün tek başına nedensel bağ kurmaz.

## Risk artırma

- Yalnız Office → şüpheli PowerShell: Medium başlangıç sinyali
- Ek executable oluşturma/çalıştırma: High
- Zararlı hedef bağlantısı ve kritik varlık/kimlik bağlamı: Critical adayı

Event'lerin aynı hostta bulunması yeterli değildir. Network bağlantısı dosyanın oluşturulmasından önceyse eski veya başka bir process instance'ına ait olabilir; doğru ProcessGuid ilişkisi ve zaman sırası aranır.
