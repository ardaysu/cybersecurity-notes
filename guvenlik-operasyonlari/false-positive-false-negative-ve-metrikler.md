# False Positive, False Negative ve Metrikler

| Sonuç | Anlamı | SOC etkisi |
| --- | --- | --- |
| True Positive | Gerçek saldırı doğru tespit edildi | Doğru müdahale başlatılır |
| False Positive | Normal olay saldırı olarak işaretlendi | Alarm yorgunluğu ve zaman kaybı |
| False Negative | Gerçek saldırı kaçırıldı | Tehdit görünmeden ilerleyebilir |
| True Negative | Normal olay doğru biçimde normal kabul edildi | Gereksiz alarm oluşmaz |

## Kanser taraması benzetmesi

- **False Positive:** Sağlıklı kişiye “kanser olabilirsin” denmesi; stres ve ek test maliyeti doğurur.
- **False Negative:** Hasta kişiye “sağlıklısın” denmesi; gerçek hastalık kaçırıldığı için daha tehlikelidir.

Güvenlikte FN çoğu senaryoda daha yüksek risk taşır; fakat sınırsız alarm üreterek recall artırmak operasyonu kullanılamaz hale getirebilir.

## Precision ve Recall

- **Precision:** Modelin “saldırı” dediği olayların ne kadarı gerçekten saldırı?
- **Recall:** Gerçek saldırıların ne kadarı yakalandı?
- **F1:** Precision ve recall arasındaki dengeyi özetler.

Banka/fraud senaryosunda eşik seçimi iş riskine bağlıdır. Çok düşük eşik gerçek dolandırıcılığı daha fazla yakalayabilir fakat meşru işlemleri engeller. Çok yüksek eşik müşteri deneyimini korur fakat fraud kaçırabilir.
