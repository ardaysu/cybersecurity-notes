# TCP ve UDP

## TCP

TCP connection-oriented ve stateful bir protokoldür. Bağlantı genellikle üçlü el sıkışma ile kurulur:

1. Client → SYN
2. Server → SYN-ACK
3. Client → ACK

TCP; sıra numarası, acknowledgment ve yeniden iletim ile güvenilir teslim sağlamaya çalışır. “Güvenilir” burada güvenlik veya şifreleme değil, verinin düzenli teslimidir.

- **SYN flood:** Çok sayıda SYN ile sunucunun yarım açık bağlantı kaynakları tüketilir.
- **Port scanning:** Farklı portlara gönderilen SYN paketleri açık servisleri keşfetmek için kullanılabilir.
- **Flag anomalileri:** Olağan dışı flag kombinasyonları tarama veya kaçınma davranışını gösterebilir.

## UDP

UDP connectionless'tır; handshake ve bağlantı state'i tutmaz. Daha düşük ek yük ve gecikme sağlar.

- Kaynak IP spoofing daha kolaydır.
- DNS ve NTP gibi servisler amplification saldırılarında kötüye kullanılabilir.
- Teslim ve sıra garantisi yoktur.
- DNS sorgularında hız nedeniyle sıklıkla UDP; büyük yanıtlar veya zone transfer gibi durumlarda TCP kullanılabilir.

> **Temel fark:** TCP state tuttuğu için SYN flood gibi state tüketen saldırılara; UDP connectionless olduğu için spoofing ve amplification saldırılarına uygun yüzey oluşturur.
