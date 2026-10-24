# Temel Linux — Security İçin

## Dosya sistemi ve inceleme

Önemli konumlar: **/etc** konfigürasyonlar, **/var/log** loglar, **/home** kullanıcı dizinleri, **/tmp** geçici dosyalar, **/proc** process/kernel bilgileri.

Araçlar: **cat, less, head, tail, grep, find**.

## Pipe ve redirection

- **\|** bir komutun çıktısını diğerine aktarır.
- **>** dosyanın üzerine yazar.
- **>>** dosyanın sonuna ekler.
- **2>** hata çıktısını yönlendirir.

Örnek: **grep "Failed password" /var/log/auth.log \| tail**

## Permissions, owner ve sudo

rwx sırasıyla read, write ve execute yetkileridir. Yetkiler owner, group ve others için ayrı tutulur.

- **chmod:** İzinleri değiştirir.
- **chown:** Owner/group değiştirir.
- **sudo:** Komutu yükseltilmiş yetkiyle çalıştırır.

Aşırı geniş izinler yetki yükseltme ve dosya manipülasyonu riskini artırır. Least privilege esastır.

## Process, service ve log

**ps/top** process'leri, **systemctl** service durumunu, **ss** dinleyen port ve bağlantıları gösterir.

Authentication, sudo ve service loglarında kim, ne zaman, nereden, hangi işlemle, başarılı mı başarısız mı soruları cevaplanır. Dağıtıma göre **/var/log/auth.log**, **/var/log/secure** veya **journalctl** kullanılır.
