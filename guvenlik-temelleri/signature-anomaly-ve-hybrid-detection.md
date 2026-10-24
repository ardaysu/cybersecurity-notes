# Signature, Anomaly ve Hybrid Detection

## Signature-based

Bilinen saldırı örüntüsü veya IOC ile eşleşme arar. Bilinen saldırılarda açıklanabilir ve düşük hata oranlı olabilir; yeni, değiştirilmiş veya zero-day davranışı kaçırabilir.

## Anomaly-based

Normal davranış profilinden sapmayı arar. Bilinmeyen saldırıları yakalayabilir; baseline kalitesine bağlıdır ve normal ama nadir davranışlarda false positive üretebilir.

### SSH anomaly örneği

Son 7 günde saatlik ortalama 2 login varken bugün aynı saatte 20 deneme, çok sayıda başarısız giriş ve farklı kaynak IP görülmesi anomali puanını artırır.

Feature örnekleri:

- Saatlik login sayısı
- Failed login sayısı
- Distinct source IP
- Kullanıcının normal çalışma saati
- Hedef sistem kritikliği

## Hybrid

Signature ve anomaly yaklaşımını birleştirerek bilinen tehditleri güvenilir imzalarla, bilinmeyen sapmaları davranış analiziyle yakalamayı amaçlar.
