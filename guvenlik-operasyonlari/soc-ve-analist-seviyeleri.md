# SOC ve Analist Seviyeleri

## SOC'nin amacı

Security Operations Center; farklı güvenlik kaynaklarından gelen telemetriyi izleyen, alarmları önceliklendiren, olayları araştıran ve gerektiğinde müdahale sürecini başlatan operasyon yapısıdır.

SOC yalnızca “ekrana alarm düşmesini bekleyen ekip” değildir. Temel iş akışı:

1. Telemetri toplama
2. Detection rule veya analitik ile alarm üretme
3. Triage
4. Investigation
5. Containment / escalation
6. Recovery
7. Lessons learned ve detection iyileştirmesi

## L1 — Triage

- Alarmın temel doğrulamasını yapar.
- Kullanıcı, cihaz, IP, zaman, olay tipi ve ilk kanıtları inceler.
- Bilinen false positive senaryolarını eler.
- Playbook uygular ve gerekli verileri toplar.
- Yetkisini aşan veya doğrulanan olayları L2'ye aktarır.

**L1'in görevi her saldırıyı tamamen çözmek değil; gerçek olay olma ihtimalini hızlı ve tutarlı biçimde değerlendirmektir.**

## L2 — Investigation

- Alarmın bağlamını genişletir.
- Endpoint, network, identity ve uygulama loglarını ilişkilendirir.
- Olayın kapsamını ve etkilenen varlıkları belirler.
- Timeline oluşturur.
- Persistence, lateral movement ve credential access ihtimallerini inceler.
- Containment önerir veya uygular.

## L3 — Advanced Analysis / Detection

- Karmaşık ve yeni saldırıları araştırır.
- Threat hunting yapar.
- Malware veya ileri artifact analizi yürütür.
- Detection gap'lerini bulur.
- Yeni kural geliştirir ve mevcut kuralları tune eder.
- Incident sonrası kök neden ve kalıcı iyileştirme üzerinde çalışır.
