# IP, Port, Session ve State

- **IP adresi:** Ağ üzerindeki kaynağı veya hedefi mantıksal olarak belirtir; NAT, proxy, VPN ve spoofing nedeniyle kimliği kesin kanıtlamaz.
- **Port:** Cihaz üzerindeki mantıksal servis uç noktasıdır.
- **Session:** İki uç arasındaki mantıksal iletişim bağlamıdır.
- **State:** Bağlantının hangi aşamada olduğunun takibidir.

Stateful firewall, yalnızca kaynak/hedef bilgisine değil bağlantının beklenen akışına da bakar. İçeriden başlatılmış bağlantının dönüş trafiğine izin verebilir; bağlam dışı paketi reddedebilir.
