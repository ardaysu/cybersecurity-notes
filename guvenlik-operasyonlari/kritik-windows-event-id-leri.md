# Kritik Windows Event ID'leri

## 4688 — Process Creation 

Windows yeni bir process oluşturduğunda, audit ayarları açıksa Security kanalında 4688 üretilebilir.

### Analizde önemli alanlar

- Yeni process adı ve tam dosya yolu
- New Process ID
- Parent / Creator Process ve PID
- Kullanıcı bağlamı
- Command line — ayrıca etkinleştirilmişse
- Zaman ve cihaz

### Parent–child ilişkisi

Normal örnek: **explorer.exe → chrome.exe**

Şüpheli örnek: **winword.exe → powershell.exe**

Office uygulamasının PowerShell başlatması; macro, exploit veya zararlı belge ihtimalini yükseltir. Tek başına saldırı kanıtı değildir; command line, dosya kaynağı, network bağlantısı ve kullanıcı davranışıyla doğrulanır.

### Command line

Process adı aracın ne olduğunu, command line aracın nasıl kullanıldığını gösterir.

**powershell.exe -NoProfile -WindowStyle Hidden -EncodedCommand ...** örneğinde gizli pencere ve encoded komut risk sinyalleridir. Encoding encryption değildir; Base64 içerik decode edilerek incelenebilir.

### PID ve dosya yolu

PID aynı isimli process örneklerini ayırır; ancak PID zamanla yeniden kullanılabileceğinden cihaz, başlangıç zamanı, kullanıcı ve process yolu birlikte değerlendirilir.

Beklenen yol: **C:WindowsSystem32svchost.exe**

Şüpheli masquerading örneği: **C:UsersAysuAppDataTempsvchost.exe**

Dosya adı tek başına güven kanıtı değildir. Tam yol, hash, dijital imza, parent process, command line, kullanıcı ve network bağlantıları birlikte incelenir.

### Örnek vaka

**outlook.exe → winword.exe → powershell.exe → Temp altında svchost.exe → malicious IP:443**

Zincirde şüpheli parent–child ilişkisi, gizli/encoded PowerShell, beklenmeyen dosya yolu ve zararlı reputation'lı network hedefi birlikte incident açılmasını destekler.

## 4720 — User Account Creation 

Yeni kullanıcı hesabı oluşturulduğunu gösterir. **Subject** hesabı oluşturan kimliği, **Target Account** ise oluşturulan hesabı ifade eder. İsim servis hesabına benzese bile onaylı ticket, HR kaydı, oluşturan hesabın yetkisi ve hesabın sonraki faaliyetleri doğrulanmalıdır.

## 4728 / 4732 — Group Membership Changes 

- **4728:** Global security grubuna üye eklenmesi
- **4732:** Yerel security grubuna üye eklenmesi
- **4729 / 4733:** İlgili gruplardan üye çıkarılması

Domain Admins üyeliği etki alanı genelinde, yerel Administrators üyeliği ise ilgili cihazda yüksek yetki sağlayabilir. Üyeliğin kısa süre sonra kaldırılması olayı güvenli yapmaz; geçici yetki penceresinde yapılan işlemler araştırılır.

## 4698 — Scheduled Task Creation 

Scheduled task; trigger, action ve RunAs bilgileriyle analiz edilir. SYSTEM olarak çalışan, sık/periyodik tetiklenen, gizli veya encoded PowerShell başlatan ve onaylı ticket'ı olmayan task kalıcılık göstergesi olabilir. Güncelleme için 4702, silme için 4699 görülebilir. Task'ın silinmesi önceki çalışmaları geçersiz kılmaz.

## 7045 — New Service Installed 

Genellikle **System** kanalında Service Control Manager tarafından üretilir. Security kanalındaki benzer servis kurulum kaydı, audit açıksa 4697 olabilir. Şüphe sinyalleri:

- Kullanıcı tarafından yazılabilir dizinde executable
- İmzasız veya yeni dosya
- Auto Start
- LocalSystem yetkisi
- Kurumda bulunmayan yazılım ve onaysız/gece kurulumu
- Meşru Windows bileşenini taklit eden ad
- Kurulum sonrası dış network bağlantısı

**Örnek zincir:** encoded PowerShell → 7045 ile otomatik/LocalSystem servis → executable'ın dış IP'ye bağlanması. Bu zincir execution, persistence, yüksek yetki ve olası command-and-control davranışlarını destekler.

## 1102 — Security Audit Log Cleared 

Security audit logunun temizlendiğini gösterir ve savunmadan kaçınma girişimi olabilir. Tek başına saldırı kanıtı değildir; planlı bakım ihtimali doğrulanır. Security logunun temizlenmesi olayın tamamen kanıtlanamayacağı anlamına gelmez. SIEM'e önceden aktarılmış kayıtlar, EDR, Sysmon, PowerShell Operational, System logları, domain controller/identity kayıtları, network cihazları ve dosya/registry kalıntıları gibi bağımsız kaynaklar araştırılır.
