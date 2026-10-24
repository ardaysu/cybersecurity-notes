# SIEM Sorgu Mantığı

Password spraying vakasında failure event'leri filtrelendi; SourceIp'ye göre gruplandı; belirli zaman penceresinde distinct User sayıldı ve ardından gelen başarılı girişle korelasyon kuruldu. Aggregation benzer event'leri özetler; correlation farklı örüntüleri bağlar; suppression ise gürültüyü azaltırken kritik gelişmeleri gizleyebilir. Proxy/NAT ortamında SourceIp'nin tek kişiyi temsil etmeyebileceği kontrol edilmelidir.
