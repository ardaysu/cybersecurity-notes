# Dosya Silme ve Veri Kalıntıları

## Silmek ile güvenli temizlemek

Dosyanın görünmemesi, içeriğinin geri kazanılamaz biçimde yok edildiğini garanti etmez. Sonuç dosya sistemi, depolama türü ve kullanılan işlemlere bağlıdır; silinen her dosya mutlaka kurtarılabilir de denemez.

İçindekiler bölümünden başlık kaldırmak sayfayı yok etmek değildir. Bu, farkı anlatan bir benzetmedir; her dosya sisteminin gerçek silme davranışının tarifi değildir.

## HDD ve SSD

- **HDD:** Veriyi dönen manyetik disklerde saklar; hareketli parçalar içerir.
- **SSD:** Veriyi elektronik bellek hücrelerinde saklar; hareketli parçaları yoktur.

SSD yazmaları farklı hücrelere yönlendirebilir. Normal dosya üstüne yazma işlemi, eski verinin bulunduğu bütün fiziksel alanlara ulaşmayı garanti etmez.

## Kriptografik silme

Uygun biçimde şifrelenmiş veriyi çözmek için gereken anahtarların güvenli şekilde ortadan kaldırılmasıdır. Etkinliği, şifreleme ve anahtar yönetiminin koşullarına bağlıdır; anahtar kopyaları ayrıca değerlendirilir.

## Kopyaları ayrı düşünmek

Bilgisayarın temizlenmesi bulut yedeğini veya başka cihazdaki kopyaları kendiliğinden silmez.

Ders örneği: Satılacak bilgisayarda dosyaları silip çöp kutusunu boşaltmak, güvenli temizleme yapıldığını kanıtlamaz. Depolama türüne uygun yöntem ve doğrulama gerekir.

## Kaynak

[NIST SP 800-88 Rev. 2 — Guidelines for Media Sanitization](https://csrc.nist.gov/pubs/sp/800/88/r2/final)

Kavramsal ders notudur; cihazda silme veya laboratuvar işlemi yapılmamıştır.

[Güvenlik Temelleri](README.md)
