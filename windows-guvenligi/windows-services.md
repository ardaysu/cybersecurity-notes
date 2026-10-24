# Windows services

## Temel fikir

Windows service, kullanıcı oturum açmasa bile arka planda çalışabilen sistem görevidir. Otomatik başlayabilmesi ve `LocalSystem` gibi yüksek yetkili hesaplarla çalışabilmesi nedeniyle hem meşru yönetimde hem saldırılarda önemlidir.

## Güvenlik açısından kullanım

- **Persistence:** Otomatik başlangıçla yeniden başlatma sonrasında çalışabilir.
- **Privilege escalation:** Düşük yetkili saldırgan servis yapılandırmasını değiştirebiliyorsa kodu SYSTEM bağlamında çalıştırabilir.
- **Defense evasion:** Güvenilir görünen servis adı veya mevcut servis kullanılabilir.

## Analiz soruları

1. Servisi kim oluşturdu veya değiştirdi?
2. `BinaryPath` hangi dosyayı gösteriyor?
3. Servis hangi hesapla ve hangi başlangıç türüyle çalışıyor?
4. Dosyanın yolu, imzası ve kurum içindeki meşruiyeti nedir?
5. Servis gerçekten başlatılmış mı; `services.exe` ilgili binary'yi çalıştırmış mı?
6. Binary çalıştıktan sonra hangi dosya, registry ve ağ davranışlarını göstermiş?

## Sık karşılaşılan kanıtlar

- System log Event ID **7045:** Yeni servis kurulması
- Security log Event ID **4697:** Audit açıksa servis kurulması
- Service Control Manager başlangıç/durdurma/hata olayları
- `HKLM\SYSTEM\CurrentControlSet\Services` değişiklikleri
- Process telemetrisi: `services.exe → servis binary'si`

## Kritik ayrımlar

- `BinaryPath` değişikliği, dosyanın çalıştırılacağını gösterir; çalıştığını kanıtlamaz.
- `services.exe → shell.exe` ilişkisi, binary'nin servis mekanizmasıyla çalıştırıldığına güçlü kanıttır.
- Otomatik servis oluşturulmuş fakat process kaydı yoksa persistence hazırlanmış olabilir; yürütme henüz kanıtlanmamıştır.
- Servisin sonradan silinmesi, önceki çalıştırma ve ağ hareketlerini geçersiz kılmaz.
- `svchost.exe` gibi güvenilir isimler, özellikle olağan dışı dosya yolundaysa meşruiyet kanıtı değildir.

## Final vaka sonucu

PowerShell tarafından oluşturulan, `C:\ProgramData\svchost.exe` dosyasını LocalSystem olarak çalıştıran otomatik servis; ardından `services.exe → svchost.exe` ve `ADMIN$` erişimi görülmesiyle birlikte yüksek güvenli şüpheli zincir oluşturur. Servis silinse de incident araştırılmalıdır.
