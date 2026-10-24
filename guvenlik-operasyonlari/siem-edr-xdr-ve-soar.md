# SIEM, EDR, XDR ve SOAR

## SIEM

SIEM, çok sayıda kaynaktan log toplar, normalize eder, korelasyon ve sorgulama sağlar.

**Güçlü tarafı:** Kurum genelindeki farklı sistemleri aynı zaman çizgisinde ilişkilendirmek.

**Sınırı:** SIEM'in kalitesi, gelen logların kapsamına ve doğruluğuna bağlıdır. Loglanmayan veya yanlış parse edilen bir olay görünmez kalabilir.

## EDR

EDR endpoint üzerinde process creation, parent–child process, command line, file, registry, network connection ve kullanıcı davranışı gibi telemetri üretir.

**Neden bazı olaylarda daha güçlü kanıttır?**

Bir network alarmı “şüpheli bağlantı görüldü” diyebilir. EDR ise aynı anda:

- Hangi process'in bağlantıyı açtığını,
- Process'in parent'ını,
- Kullanılan command line'ı,
- Hangi kullanıcı bağlamında çalıştığını,
- Dosya veya registry değişikliğini

gösterebilir. Bu nedenle endpoint davranışını doğrudan destekleyen EDR kanıtı, tek başına bir network sinyalinden daha açıklayıcı olabilir.

> “EDR her zaman daha güvenilirdir” şeklinde mutlak bir kural yoktur. Güçlü kanıt, olayla en doğrudan ilişkili ve başka kaynaklarla doğrulanabilen kanıttır.

## XDR

XDR; endpoint, identity, email, network ve cloud telemetrilerini tek olay bağlamında birleştirmeyi amaçlar.

SIEM daha genel log yönetimi ve sorgulama katmanıyken XDR çoğunlukla güvenlik ürünleri arasındaki detection ve response korelasyonuna odaklanır. Ürünlere göre sınırlar değişebilir.

## SOAR

SOAR; tekrarlanan güvenlik süreçlerini playbook'larla otomatikleştirir ve araçlar arasında aksiyon alır.

Örnek playbook:

1. IOC enrichment
2. IP/domain reputation kontrolü
3. Kullanıcı ve cihaz bağlamı toplama
4. Ticket oluşturma
5. Belirlenen eşik aşılırsa endpoint izolasyonu
6. Analiste sonuçları sunma

**Kritik ayrım:** SOAR karar kalitesini kendiliğinden garanti etmez. Hatalı detection veya yanlış playbook, yanlış aksiyonu daha hızlı uygular. İnsan onayı gerektiren adımlar doğru seçilmelidir.
