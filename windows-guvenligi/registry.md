# Registry

## Temel fikir

Registry, Windows ve uygulamaların yapılandırma bilgisini tuttuğu merkezi ayar yapısıdır. Saldırganlar bu yapıyı yalnızca persistence için değil; güvenlik kontrollerini zayıflatma, yetki yükseltme ve sistem keşfi gibi amaçlarla da kullanabilir.

- **HKCU:** İlgili kullanıcının ayarlarıdır; etkisi çoğunlukla o kullanıcıyla sınırlıdır.
- **HKLM:** Makine genelindeki ayarlardır; etki alanı daha geniştir ve değişiklik genellikle daha yüksek yetki ister.

## Kritik analiz sorusu

> Hangi process, hangi registry konumunu, hangi değerle ve hangi kullanıcı bağlamında değiştirdi?

Yaygın registry telemetrisi:

- Anahtar/değer oluşturma veya silme
- Değer yazma/değiştirme
- Anahtar/değer yeniden adlandırma
- Sysmon kullanılıyorsa çoğunlukla Event ID 12–14 ailesi

## Persistence örneği

`HKCU\Software\Microsoft\Windows\CurrentVersion\Run` altına komut eklenmesi, kullanıcı oturum açtığında programın çalışmasını sağlayabilir. `Hidden`, `EncodedCommand`, kullanıcı profilindeki imzasız EXE ve Office process'inin kaydı oluşturması şüpheyi güçlendirir.

## Persistence dışındaki kullanım

Defender veya logging ayarlarının registry üzerinden zayıflatılmaya çalışılması, persistence değil **defense evasion / Impair Defenses** davranışıdır.

## Analiz nüansları

- HKCU veya `update.exe` adı tek başına zararlı kanıtı değildir.
- Güvenilir görünen değer adı meşruiyet kanıtlamaz.
- Bir registry kaydının sonradan silinmesi, geçmişte oluşturulduğu gerçeğini ortadan kaldırmaz.
- Run kaydı oturum açılmadan silinmişse persistence tetiklenmemiş olabilir; process telemetrisiyle çalıştırma doğrulanmalıdır.
- Registry değeri yazılmış olsa bile Windows sürümü veya merkezi politika nedeniyle ayar fiilen etkisiz kalabilir.

## Final vaka sonucu

Office → gizli PowerShell → Run key ile `sync.exe` → Defender ayarı değiştirme girişimi → dış IP bağlantısı zinciri; persistence, savunmayı zayıflatma ve command-and-control ihtimallerini birlikte destekler. Incident açılıp process, file, registry ve network telemetrisi ilişkilendirilmelidir.
