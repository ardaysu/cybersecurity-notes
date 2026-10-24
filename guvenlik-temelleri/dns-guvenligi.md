# DNS Güvenliği

DNS alan adını IP adresine çözer. İstemci recursive resolver'a sorar; resolver gerektiğinde root, TLD ve authoritative sunucularla iletişim kurar.

Temel riskler:

- **DNS spoofing / cache poisoning**
- **DNS tunneling**
- **DNS amplification**
- **DGA davranışı**

Şüpheli işaretler:

- Çok uzun ve yüksek entropili subdomain'ler
- Çok sık sorgu veya çok sayıda başarısız çözümleme
- Yeni veya nadir domain'ler
- Normal dışı sorgu tipi ve yanıt boyutu

DNS trafiğindeki sapmalar güçlü detection sinyali olabilir; yine de tek başına kesin saldırı kanıtı değildir.
