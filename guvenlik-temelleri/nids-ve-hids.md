# NIDS ve HIDS

## NIDS

Network segmentindeki paket ve akışları inceler.

- **Avantaj:** Birden fazla sistemi tek sensörle gözleyebilir.
- **Sınır:** Şifreli içerik, ağ segmentasyonu ve process bağlamının eksikliği.

## HIDS

Tek host üzerindeki log, dosya, process, kullanıcı ve konfigürasyon değişikliklerini inceler.

- **Avantaj:** Endpoint içindeki davranışı ayrıntılı görebilir.
- **Sınır:** Her sisteme agent/konfigürasyon gerekir; host ele geçirilirse telemetri etkilenebilir.

NIDS “hangi ağ davranışı oldu?”; HIDS “host içinde ne gerçekleşti?” sorusuna daha iyi cevap verir. Birlikte kanıtı güçlendirirler.
