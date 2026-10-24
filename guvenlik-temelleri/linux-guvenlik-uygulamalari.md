# Linux Güvenlik Uygulamaları

## Cron jobs

Cron zamanlanmış komut çalıştırır; saldırgan tarafından persistence için kötüye kullanılabilir. Kullanıcı crontab'ları, **/etc/crontab** ve **/etc/cron.**\* incelenebilir.

## SSH hardening

Temel ayarlar **/etc/ssh/sshd\_config** içindedir:

- **PermitRootLogin no**
- Key-based authentication
- Uygun ortamda **PasswordAuthentication no**
- Kullanıcı ve ağ erişimini sınırlandırma

Yanlış konfigürasyon erişimi kesebileceği için doğrulama gerekir.

## UFW

Temel komutlar: **sudo ufw allow 22/tcp**, **sudo ufw enable**, **sudo ufw status**.

SSH kuralını eklemeden firewall'ı etkinleştirmek bağlantıyı kesebilir.

## File integrity

**sha256sum dosya.txt** ve **md5sum dosya.txt** hash üretir. Sonradan farklı hash görülmesi dosyanın değiştiğini gösterir; değişikliğin kötü niyetli olduğunu veya ilk hash'in güvenilir olduğunu tek başına kanıtlamaz. SHA-256, MD5'e göre tercih edilir.
