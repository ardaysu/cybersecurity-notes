# OSI Modeline Güvenlik Gözüyle Bakış

OSI modeli ezberlenecek yedi isimden çok, problemin ve saldırı sinyalinin hangi katmanda oluştuğunu ayırmak için kullanılır.

| Katman | Örnek | Güvenlik bağlantısı |
| --- | --- | --- |
| Application | HTTP, DNS | Web saldırıları, DNS tunneling |
| Transport | TCP, UDP, port | SYN flood, port scanning |
| Network | IP, ICMP | IP spoofing, routing ve reconnaissance |
| Data Link | MAC, ARP | ARP poisoning ve local MITM |

Bir siteye erişilemiyorsa sorun domain çözümlemesinde DNS, bağlantı kurulmasında TCP, yönlendirmede IP veya yerel ağ çözümlemesinde ARP olabilir. Katman yaklaşımı analizi daraltır.
