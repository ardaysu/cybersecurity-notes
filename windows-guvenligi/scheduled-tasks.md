# Scheduled tasks

## Temel fikir

Scheduled task, belirli bir tetikleyici oluştuğunda belirli bir komutu seçilen kullanıcı/yetki bağlamında çalıştırır.

- **Task:** Oluşturulan görev
- **Trigger:** Ne zaman/neyin ardından çalışacağı
- **Action:** Çalıştıracağı komut veya dosya
- **Run As:** Hangi kimlik ve yetkiyle çalışacağı

## Güvenlik açısından kullanım

Kullanıcı oturum açtığında, sistem açıldığında veya periyodik olarak çalışan görevler persistence sağlayabilir. SYSTEM bağlamı yüksek etki; gizli/encoded PowerShell, olağan dışı dosya yolu ve güvenilir görünen task adı defense evasion şüphesini artırır.

## Kritik ayrım

```txt
Task oluşturuldu → Çalışması planlandı
Task tetiklendi  → Çalıştırılmaya çalışıldı
Process oluştu   → Action gerçekten yürütüldü
```

Görev oluşturulmuş fakat tetiklenmeden silinmişse persistence hazırlanmış olabilir; execution kanıtlanmamıştır.

## Sık karşılaşılan kanıtlar

- Security Event ID **4698:** Task oluşturuldu
- Security Event ID **4699:** Task silindi
- Security Event ID **4702:** Task güncellendi
- Task Scheduler Operational logları: Kayıt, tetiklenme ve action başlangıcı
- Process telemetrisi: Task Scheduler process'i → action process'i

## Analiz soruları

1. Görevi hangi kullanıcı ve process oluşturdu?
2. Trigger, action ve Run As nedir?
3. Onaylı ticket veya beklenen yazılım var mı?
4. Task gerçekten tetiklendi mi?
5. Action process'i oluştu mu ve sonrasında ne yaptı?
6. Task'ın silinmesi iz temizleme amacı taşıyor olabilir mi?

## Final vaka sonucu

Onaysız `helpdesk.admin` hesabının oluşturduğu, her 15 dakikada SYSTEM olarak `rundll32.exe` ile DLL çalıştıran task; gerçekten tetiklenip dış IP bağlantısı kurduğunda incident açılmalıdır. Task silinse bile geçmiş yürütme geçerlidir ve `helpdesk.admin` hesabı da incelenmelidir.
