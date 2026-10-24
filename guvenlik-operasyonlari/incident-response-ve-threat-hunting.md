# Incident Response ve Threat Hunting

## Incident Response yaşam döngüsü

1. **Preparation:** Loglama, roller, playbook, iletişim ve araç hazırlığı
2. **Detection & Analysis:** Alarmın doğrulanması, kapsam ve önem değerlendirmesi
3. **Containment:** Yayılmayı sınırlama
4. **Eradication:** Zararlı bileşen ve kök nedenin kaldırılması
5. **Recovery:** Sistemin kontrollü biçimde normale alınması
6. **Lessons Learned:** Süreç ve detection eksiklerinin düzeltilmesi

Containment ile eradication aynı değildir. Bir endpoint'i izole etmek yayılmayı durdurabilir; persistence mekanizmasını kaldırmak ise eradication kapsamındadır.

## Threat Hunting

Threat hunting, mevcut bir alarmı beklemeden hipotez üzerinden tehdit aramaktır.

Örnek hipotez:

> Bir saldırgan, normal yönetim aracı gibi görünen PowerShell'i kullanarak encoded command çalıştırıyor olabilir.

Hunt sırasında amaç yalnızca şüpheli kayıt bulmak değil; hipotezi destekleyen veya çürüten telemetriyi sistematik biçimde toplamaktır. Hunt sonucu yeni detection rule'a dönüşebilir.
