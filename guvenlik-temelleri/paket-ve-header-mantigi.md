# Paket ve Header Mantığı

Paket, taşınan veri ile bu verinin nasıl işleneceğini belirten header alanlarının birleşimidir.

## IPv4'te önemli alanlar

- **Version:** IP sürümü.
- **IHL:** IPv4 header uzunluğu. Değer 32-bit word sayısıdır; minimum 5 yani 20 byte'tır. IHL > 5, IP options bulunduğunu gösterir.
- **Total Length:** Header ve payload dahil toplam paket boyutu.
- **Identification / Flags / Fragment Offset:** Fragmentation yönetimi.
- **TTL:** Her router geçişinde azalır; sıfıra ulaşınca paket düşürülür. Routing loop'larını sınırlar.
- **Protocol:** Üst katmanda TCP, UDP veya ICMP bulunduğunu gösterir.
- **Header Checksum:** Yalnızca IPv4 header bozulmasını kontrol eder; kriptografik bütünlük sağlamaz.
- **Source / Destination IP:** Kaynak ve hedef.

## TTL, traceroute ve ICMP

Traceroute farklı TTL değerleriyle paket gönderir. TTL sıfıra düştüğünde router ICMP Time Exceeded yanıtı üretir; böylece yol üzerindeki router'lar yaklaşık olarak görünür.

ICMP, IPv4 içinde taşınır; TCP veya UDP portu kullanmaz. Ping genellikle ICMP Echo Request ve Echo Reply mesajlarını kullanır.

## Checksum ayrımı

Checksum iletim hatalarındaki bit bozulmalarını yakalamaya yöneliktir. Saldırgan paketi değiştirip checksum'u yeniden hesaplayabilir. Bu nedenle checksum, hash veya dijital imza düzeyinde güvenlik kanıtı değildir.
