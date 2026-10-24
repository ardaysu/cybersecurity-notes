# Faz 1 — Güvenlik Temelleri ve Ağlar

> **Durum:** Tamamlandı  
> **Amaç:** Ağ ve işletim sistemi sinyallerini ezberlenmiş terimler olarak değil, saldırı ve savunma bağlamında yorumlayabilmek.

## 1. Güvenliğin temel hedefi: CIA üçlüsü

Bilgi güvenliği yalnızca “veriyi gizlemek” değildir. Üç ayrı hedef birlikte korunur:

- **Confidentiality (Gizlilik):** Veriyi yalnızca yetkili kişiler okuyabilmelidir.
- **Integrity (Bütünlük):** Veri yetkisiz biçimde değiştirilememelidir.
- **Availability (Erişilebilirlik):** Sistem ve servisler gerektiğinde kullanılabilmelidir.

Bir olay birden fazla hedefi etkileyebilir. Ele geçirilen bir yönetici hesabı hem gizli veriyi okuyabilir hem değiştirebilir. DDoS ise öncelikle erişilebilirliği hedefler.

**Akılda kalacak ayrım:** Güvenlik sorusu yalnızca “veri çalındı mı?” değildir; “kim okuyabildi, kim değiştirebildi ve sistem çalışmaya devam etti mi?” sorularının tamamıdır.

## 2. OSI modeli: ezber değil, arızayı ve saldırıyı daraltma aracı

OSI katmanları, bir belirtiyi doğru yere bağlamak için kullanılır:

| Katman | Örnek | Güvenlik bağlantısı |
|---|---|---|
| Application | HTTP, DNS | Web saldırıları, DNS tunneling |
| Transport | TCP, UDP, portlar | SYN flood, port taraması |
| Network | IP, ICMP | Spoofing, routing, reconnaissance |
| Data Link | MAC, ARP | ARP poisoning, yerel MITM |

Bir siteye erişilemiyorsa alan adı çözümlenemiyor olabilir, TCP bağlantısı kurulamıyor olabilir veya rota bozuk olabilir. Katman düşüncesi, “internet çalışmıyor” gibi geniş bir problemi incelenebilir parçalara böler.

## 3. IP, port, oturum ve state

- **IP adresi** iletişimdeki cihazı veya ağ arayüzünü işaret eder.
- **Port**, cihaz içindeki servisi ayırır.
- **Session**, taraflar arasındaki mantıksal iletişim bağlamıdır.
- **State**, bağlantının hangi aşamada olduğunu gösterir.

Bir IP tek başına kullanıcı kimliği değildir. NAT, VPN, proxy, CDN ve dinamik adresleme yüzünden aynı IP birden fazla kullanıcıya veya zaman içinde farklı kişilere ait olabilir. Bu nedenle “zararlı IP görüldü” ile “incident doğrulandı” aynı cümle değildir.

## 4. TCP ve UDP

TCP bağlantı yönelimlidir. Üçlü el sıkışma kabaca `SYN → SYN/ACK → ACK` sırasıyla bağlantı durumunu kurar; sıra, teslim ve yeniden iletim mekanizmaları sağlar. UDP bağlantı kurmadan datagram gönderir; daha düşük ek yüke karşılık teslim garantisi vermez.

Güvenlik açısından:

- Çok sayıda yarım kalan TCP el sıkışması SYN flood ihtimalini düşündürebilir.
- Çok sayıda hedef porta kısa bağlantı denemesi port taraması olabilir.
- UDP'nin bağlantısız yapısı DNS/NTP amplification gibi kötüye kullanımlarda önemlidir.

Hiçbiri bağlamsız kesin hüküm değildir. Bir zafiyet tarayıcısı da çok sayıda porta bağlanabilir; onu saldırgandan ayıran varlık, zaman, yetki ve iş amacı bağlamıdır.

## 5. DNS güvenliği

DNS, alan adını IP adresine çeviren telefon rehberi gibidir; fakat güvenlik analizi sadece çözüm sonucuna bakmaz. Sorgulanan domain, alt alan adı yapısı, sorgu sıklığı, cevap türü, TTL ve isteği yapan process birlikte değerlendirilir.

Şüpheli örnekler:

- Çok uzun ve yüksek entropili alt alan adları
- Düzenli aralıklarla aynı domaine sorgu
- Yeni veya kurumsal bağlamda görülmemiş domain
- DNS sorgusunu yapan beklenmedik process

Bu davranışlar DNS tunneling veya C2 ihtimalini doğurabilir. Fakat CDN, telemetry ve güvenlik ürünleri de benzer görüntü üretebilir.

## 6. HTTP, HTTPS ve TLS

HTTP; method, URL, header, cookie, status code ve body gibi parçalarla uygulama iletişimini taşır. HTTPS, HTTP trafiğini TLS ile korur.

TLS üç şeyi hedefler:

1. Sunucunun kimliğini sertifikayla doğrulamak,
2. Aktarılan içeriği şifrelemek,
3. Aktarım sırasında değişikliği fark edebilmek.

HTTPS, sitenin güvenilir veya zararsız olduğunu kanıtlamaz. Zararlı bir site de geçerli sertifika kullanabilir. TLS içeriği korur; içeriğin niyetini onaylamaz.

## 7. Paket ve header mantığı

Paket içeriği kadar metadata da önemlidir: kaynak/hedef, port, protokol, flag, uzunluk, zaman ve akış yönü. Tek paket çoğu zaman yetersizdir; akış veya zaman çizelgesi gerekir.

```text
DNS sorgusu → IP cevabı → TCP bağlantısı → TLS/HTTP isteği → indirilen dosya
```

Bu zincir ayrı ürünlerde görülebilir. Analistin görevi kayıtları ortak zaman, kullanıcı, cihaz, IP ve process üzerinden ilişkilendirmektir.

## 8. Normal ve anormal trafik

Anomali, “alışılandan farklı” demektir; doğrudan “zararlı” demek değildir. Yeni bir yedekleme sistemi gece yüksek trafik üretebilir. Buna karşılık saldırgan, normal araçları ve çalışma saatlerini taklit ederek anomali oluşturmadan ilerleyebilir.

Bu yüzden baseline bir referans noktasıdır:

- Bu kullanıcı normalde hangi saatlerde çalışır?
- Bu sunucu hangi hedeflerle konuşur?
- Bu process normalde ağ bağlantısı kurar mı?
- Bu veri hacmi bu varlık için beklenen aralıkta mı?

## 9. Firewall, IDS ve IPS

- **Firewall:** Trafiğe kurallar doğrultusunda izin verir veya engeller.
- **IDS:** Şüpheli davranışı tespit edip alarm üretir.
- **IPS:** Trafik yolunda yer alıp tespit ettiği isteği engelleyebilir.

Bir isteğin engellenmesi alarmı gereksiz yapmaz. Bu, kontrolün çalıştığını gösterirken aynı zamanda girişimin kaynağı, hedefi ve tekrarı hakkında araştırma gerektirebilir. “Blocked” sonucu, girişimin başarılı olmadığını destekler; saldırganın cihazda başka davranış göstermediğini kanıtlamaz.

## 10. NIDS ve HIDS

- **NIDS**, ağ üzerindeki paket ve akışları görür.
- **HIDS**, endpoint içindeki dosya, process, kullanıcı ve sistem olaylarını görür.

NIDS dış IP bağlantısını görürken hangi process'in başlattığını bilemeyebilir. HIDS process zincirini görürken ağın başka segmentindeki trafiği kaçırabilir. İkisi rakip değil, birbirinin kör noktasını kapatan sensörlerdir.

## 11. Signature, anomaly ve hybrid detection

**Signature tabanlı tespit**, bilinen örüntüyü arar. Hızlı ve açıklanabilirdir; küçük değişikliklerle aşılabilir. **Anomali tabanlı tespit**, normalden sapmayı arar; bilinmeyeni yakalayabilir fakat baseline bozuksa gürültü üretir. **Hybrid yaklaşım**, bilinen davranışta kesin kuralı, belirsiz davranışta bağlam ve anomaliyi birlikte kullanır.

İyi tespit “üç şüpheli işaret mutlaka aynı anda olsun” diye gereğinden fazla katılaştırılmaz. Aksi halde saldırıların bir kısmı kaçırılır. Sinyaller ayrı kurallar veya puanlama ile birleştirilebilir.

## 12. MITRE ATT&CK temeli

MITRE ATT&CK saldırgan davranışlarını ortak bir dilde anlatır:

- **Tactic:** Saldırganın amacı; ör. Persistence veya Credential Access.
- **Technique:** Bu amaca ulaşma biçimi; ör. Scheduled Task.
- **Procedure:** Belirli aktörün tekniği gerçek olayda nasıl uyguladığı.

ATT&CK bir ürün, engelleme listesi veya saldırı kronolojisi değildir. Tespitin hangi davranışı kapsadığını ve nerede boşluk bulunduğunu konuşmak için haritadır.

## 13. Linux'ta güvenlik için gerekli temel

Hedef Linux yöneticisi olmak değil; güvenlik sinyallerini okuyabilmektir:

- Dosya sistemi, `find`, `grep`, pipe ve redirection
- İzinler, kullanıcılar, gruplar ve `sudo`
- Process ve servisler
- Sistem ve authentication logları
- `cron` ile zamanlanmış görevler ve persistence
- SSH hardening: root girişini kapatma, anahtar tabanlı erişim, kullanıcı sınırı
- UFW ile temel host firewall
- `sha256sum` ile bütünlük ve indirme doğrulama

Cron kaydı yalnızca bir komutun planlandığını; process kaydı ise gerçekten yürütüldüğünü gösterir. Bu “yapılandırma ≠ yürütme” ayrımı Windows servisleri ve scheduled task analizinde de tekrar karşımıza çıkar.

## Faz 1'den kalan düşünme modeli

Bir güvenlik sinyalini yorumlarken sırayla şunları sor:

1. **Ne gözlendi?** Ham kanıtı yaz.
2. **Bu hangi katman veya varlıkta?** Ağ, endpoint, identity, application?
3. **Normal açıklaması olabilir mi?** İş bağlamını ara.
4. **Başka hangi telemetri doğrular?** Tek kaynağa yaslanma.
5. **Kesin olanla olası sonucu ayır.** Anomaliyi incident diye etiketleme.
