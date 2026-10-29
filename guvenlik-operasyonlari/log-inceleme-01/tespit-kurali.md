# Tespit Kuralı Tasarımı ve Örnek Veride Test

Bu uygulama [kurgusal CSV](olaylar.csv) üzerinde yerel olarak çalıştırıldı. Canlı sisteme kural kurulmadı.

## Hedef davranış

Aynı kaynaktan kısa sürede çok sayıda farklı hesaba başarısız giriş yapılmasını bulmak; ardından hedeflenen hesaplardan birine aynı kaynaktan başarılı giriş gelirse bunu ilişkilendirmek.

Bu bir password spraying kanıtı değil, araştırılacak örüntüdür.

## Tasarım kararları

- Yalnızca identity kaynağındaki login olayları değerlendirilir.
- Başarısız girişler kaynak IP ve kayan zaman penceresiyle gruplanır.
- Hem toplam deneme hem farklı kullanıcı sayısı tutulur.
- Son 5 dakikada en az 5 farklı kullanıcı başlangıç eşiğidir.
- İlişkilendirilen başarı aynı IP'den, hedeflenen hesaplardan birine ve pencerenin bitişinden sonraki 5 dakika içinde gelmelidir.

5 hesap ve 5 dakika eğitim için seçildi; gerçek ortam için doğrulanmış eşikler değildir. Toplam deneme sayısı analiste sunulur, bu sürümde alarm eşiğine dahil değildir.

## Kayan pencere

09.04'te üç, 09.06'da üç başka hesaba giriş denemesi sabit 09.00–09.05 ve 09.05–09.10 pencerelerinde 3+3 olarak bölünebilir. Kayan pencere bu altı hesabı birlikte görebilir. Bu belirli sınır kaçırmasını azaltır; her durumda üstünlük iddiası değildir.

Kod pencereyi (bitiş - 300 saniye, bitiş] olarak tanımlar. Sol uç dışarıda, sağ uç içeridedir. Yalnızca olay zamanına bakılır.

## Çalışan örnek

- [Python uygulaması](detection.py)
- [Testler](test_detection.py)
- [CSV üzerinde üretilen sonuç](sonuc.json)

Aynı klasörde çalıştırma:

```sh
python3 detection.py
python3 -m unittest test_detection.py
```

CSV sonucu: 198.51.100.24 için E03–E07 kayıtları, 5 deneme ve 5 farklı hesap. Ardından E10, Deniz, 09.05, S300 eşleşti. E09 farklı IP nedeniyle eşleşmedi.

## Doğrulanan dört test

1. Sabit pencere sınırını aşan denemeler kayan pencerede birlikte bulunur.
2. Tek hesaba 50 deneme farklı hesap eşiğini sağlamaz.
3. Başarı eşleşmesi IP, hedef kullanıcı ve zaman sırasını gerektirir; ilgisiz, önceki veya geç başarılar eşleşmez.
4. Pencerenin tam sol sınırındaki kayıt dışarıda tutulur.

Dört test geçti. Bunlar eğitim mantığının belirli koşullarını kontrol eder; üretim başarısı veya yanlış pozitif oranı ölçümü değildir.

## Korelasyonun sınırları

Başarı farklı IP'den gelirse çok hesaplı başarısızlık alarmı yine oluşabilir; başarıyla kurulan bağlantı kaçırılır. IP koşulunu kaldırmak ise ilgisiz girişleri bağlama riskini artırır. Daha geniş adaylarda hesap, zaman, cihaz ve istemci bilgileriyle bağlam zenginleştirilebilir.

Başarı kuralda tanımlı zaman aralığından sonra gelirse bağlantı kurulmaz. Bu, başarının güvenli olduğunu göstermez. Başarı örüntü eşiğinin oluşmasından önce gerçekleşirse bu sürüm onu da ilişkilendirmez.

## Ortak şirket IP'sini tamamen dışlamamak

Ortak çıkıştan çok sayıda meşru kullanıcı gelebilir; bu yanlış pozitif sebebidir. Ancak bütün şirket IP'sini istisna listesine almak, o kaynaktan gelen saldırıları da saklayabilir.

Geniş istisna yerine doğrulanabilir kullanıcı, uygulama, cihaz, zaman ve iş akışı bağlamı değerlendirilir. İstisnaların kapsamı ve gerekçesi belgelenmelidir.

## Üretimden farkı

Kod tek gün ve eşzamanlı saat varsayar; tarih, zaman dilimi veya gece yarısını yönetmez. Geç gelen olay, yinelenen kayıt, alarm bastırma ve veri kaynağı değişimleri ele alınmaz. Aynı örüntü farklı pencere bitişlerinde tekrar aday üretebilir.

Dosyadaki kimlik alanları normalleştirilmiş kabul edilir. Gerçek ortamda kullanıcı alanının doluluğu, hesap kimliğinin tutarlılığı ve log kapsamı doğrulanmalıdır.

Bu sınırlar uygulamanın parçasıdır; eksik kayıt veya eşleşme yokluğundan güvenli sonuç çıkarılmaz.

[Olay incelemesine dön](README.md)
