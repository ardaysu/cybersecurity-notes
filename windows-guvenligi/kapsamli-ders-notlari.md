# Faz 4 — Windows Güvenliği ve İç Yapılar

> **Durum:** 5/10 tamamlandı, park edildi  
> **Tamamlananlar:** Process–thread–token, Registry, Services, Scheduled Tasks, LSASS/Credential Access  
> **Dönüş noktası:** PowerShell ve Windows scripting

Bu faz tamamlanmış gibi gösterilmemiştir. Aşağıdaki içerik yalnızca gerçekten işlenen beş başlığın kapsamlı kaydıdır.

## 1. Process, thread ve token

**Process**, çalışan programın kaynak ve bellek bağlamıdır. **Thread**, process içindeki yürütme akışıdır. **Access token**, process veya thread'in hangi kullanıcıyı temsil ettiğini ve hangi yetkilere sahip olduğunu belirtir.

Dosya adı kimlik değildir. `svchost.exe` adlı dosya olağan dışı bir klasördeyse veya beklenmedik parent tarafından başlatıldıysa güvenilir sayılmaz. Analizde:

- Image path ve dijital imza
- Parent–child ilişkisi
- Command line
- Kullanıcı ve integrity level
- Token/privilege değişiklikleri
- Child process, dosya ve ağ davranışı

birlikte değerlendirilir.

Örneğin Word'ün PowerShell başlatması saldırıyı kesinleştirmez; fakat kullanıcı belgesi üzerinden execution zincirini düşündürür. PowerShell'in indirme yapması, Defender ayarına dokunması ve yeni child process başlatması güveni yükseltir.

## 2. Registry

Registry, Windows ve uygulamaların merkezi yapılandırma alanıdır.

- **HKCU:** Kullanıcıya özgü ayarlar
- **HKLM:** Makine genelindeki ayarlar

Saldırgan registry'yi persistence, defense evasion, privilege escalation veya discovery için kullanabilir. Kritik soru:

> Hangi process, hangi anahtarı, hangi değerle, hangi kullanıcı bağlamında değiştirdi?

`HKCU\Software\Microsoft\Windows\CurrentVersion\Run` altında komut oluşturmak kullanıcı oturum açtığında yürütme sağlayabilir. Fakat kayıt yazılması dosyanın çalıştığını kanıtlamaz. Kayıt tetiklenmeden silinmiş olabilir; process telemetrisi aranmalıdır.

Defender veya logging ayarını zayıflatan registry değişikliği persistence değil, **Impair Defenses / defense evasion** davranışıdır. Windows sürümü ve merkezi politika nedeniyle yazılan değer etkisiz de kalabilir; yapılandırma değişikliği ile fiili etki ayrılır.

## 3. Windows Services

Service, kullanıcı oturumu olmadan arka planda çalışabilir ve `LocalSystem` gibi yüksek yetkili hesapları kullanabilir.

Güvenlik etkileri:

- Automatic başlangıç → persistence
- Değiştirilebilir binary path + SYSTEM → privilege escalation
- Güvenilir servis adı veya mevcut servisin değiştirilmesi → defense evasion

### Analiz soruları

1. Servisi kim ve hangi process oluşturdu/değiştirdi?
2. `BinaryPath` nereye işaret ediyor?
3. Başlangıç tipi ve service account nedir?
4. Dosya yolu, imzası ve kurum içi onayı var mı?
5. Servis gerçekten başlatıldı mı?
6. Binary çalışınca ne yaptı?

### Kanıtlar

- System 7045 ve Security 4697: servis kurulumu
- Service Control Manager olayları
- `HKLM\SYSTEM\CurrentControlSet\Services` değişiklikleri
- `services.exe → service_binary.exe` process ilişkisi

`BinaryPath` değişikliği hazırlığı; `services.exe → shell.exe` ilişkisi yürütmeyi destekler. Servisin sonradan silinmesi, daha önceki execution ve ağ davranışını ortadan kaldırmaz.

```text
powershell.exe → servis BinaryPath değişikliği
services.exe   → C:\Users\Public\shell.exe
shell.exe      → dış IP:443
```

Bu zincir yapılandırma, yürütme ve sonraki davranışı ayrı kanıtlarla gösterir.

## 4. Scheduled Tasks

Scheduled task dört parçayla okunur:

- **Task:** Oluşturulan görev
- **Trigger:** Ne zaman çalışacağı
- **Action:** Hangi komutu çalıştıracağı
- **Run As:** Hangi kimlik/yetkiyle çalışacağı

```text
Task oluşturuldu → çalışması planlandı
Task tetiklendi  → çalıştırılmaya çalışıldı
Process oluştu   → action gerçekten yürütüldü
```

Görev 03:00 için oluşturulup 12:05'te silindiyse ve process kaydı yoksa persistence hazırlanmış olabilir; execution kanıtlanmamıştır.

Sık kanıtlar: Event 4698 (oluşturma), 4699 (silme), 4702 (güncelleme), Task Scheduler Operational logları ve `taskeng.exe`/Task Scheduler ile action process ilişkisi.

Güvenilir görünen task adı kanıt değildir. `ChromeUpdate` adlı görev `C:\ProgramData\chrome_update.exe` çalıştırıyor, SYSTEM yetkisi kullanıyor ve dış IP'ye bağlanıyorsa isim yalnızca maskeleme olabilir.

## 5. LSASS ve Credential Access

`lsass.exe`, Windows kimlik doğrulaması ve güvenlik politikalarında kritik rol oynar. Aktif oturumlarla ilişkili hash, Kerberos ticket'ı veya başka credential materyali bellekte bulunabilir. “Bütün parolalar LSASS içinde düz metindir” ifadesi doğru değildir.

Onaysız process'in LSASS belleğine okuma erişimi istemesi credential dumping şüphesidir. Ancak:

```text
LSASS erişimi denendi ≠ credential ele geçirildi
Dump oluştu           ≠ geçerli parola çıkarıldı
Dosya gönderildi      ≠ içeriğin ne olduğu kesinleşti
```

### Güçlü saldırı zinciri

```text
Office → PowerShell → reader.exe
reader.exe → lsass.exe erişimi (Allowed)
→ auth.dmp
→ auth.zip
→ dış sunucuya HTTP 200
→ ayrıcalıklı hesapla yeni cihazdan ADMIN$ erişimi
```

Bu zincir olası phishing, credential dumping, exfiltration ve lateral movement için kritik incident gerektirir. Yine de düz metin parola mı, hash mi, ticket mı kullanıldığı ek kanıt ister.

### Meşru kullanım ve dual-use araçlar

Microsoft imzalı ProcDump onaylı support işlemi olabilir; saldırgan da kullanabilir. İmza niyeti kanıtlamaz. Ticket, bakım penceresi, kullanıcı, hedef, çıktı yolu ve sonraki davranış doğrulanır.

### Koruma mekanizmaları

- **PPL:** Yetkisiz process'lerin LSASS'a erişmesini zorlaştırır.
- **Credential Guard:** Bazı hassas credential materyalini sanallaştırma tabanlı izole ortamda korur.

LSASS yöntemi engellense bile browser credential store, Credential Manager, token, ticket, script veya yapılandırma dosyaları hedeflenebilir. Credential Access, LSASS'tan geniştir.

## Faz boyunca ana kanıt ilkesi

Windows analizinde aynı ayrımı tekrar tekrar kullan:

| Aşama | Ne söylenebilir? |
|---|---|
| Yapılandırma oluşturuldu | Mekanizma hazırlanmış olabilir |
| Tetikleyici görüldü | Çalıştırma girişimi oluşmuş olabilir |
| Process kaydı görüldü | Kod yürütülmüş |
| Sonraki davranış görüldü | Etki ve amaç hakkında bağlam oluşmuş |

Bir iz daha sonra silinse bile tarihsel olay yok olmaz. Buna karşılık yalnızca hazırlık görülmüşse başarılı execution iddia edilmez.

## Henüz tamamlanmayan başlıklar

- PowerShell ve Windows scripting
- DLL loading, injection ve memory davranışları
- Authentication internals ve lateral movement ayrıntıları
- Defense evasion ve log tampering
- Windows investigation capstone
