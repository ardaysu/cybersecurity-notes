# Tez Danışmanı Görüşmesi — İlerleme ve Kapsam Notu

**Tarih:** 31 Ekim 2026  
**Tez:** AI Agent Sistemlerinde MCP Tabanlı Araç ve Veri Erişiminin Güvenliği: Authentication ve Authorization Odaklı Bir İnceleme

## Görüşmede aktarılacak mevcut durum

Tez başlığı netleştikten sonraki çalışma, kavramsal hazırlık, seçilmiş kaynakları okuma ve araştırma sorusunu daraltma düzeyindedir. MCP üzerinde çalışan özgün bir güvenlik mekanizması henüz geliştirilmemiştir. Aşağıdaki başlıkların tümü uygulama yapılmış veya tam uzmanlık kazanılmış gibi sunulmamalıdır.

## 1. AI ve agent sistemleri için kurduğumuz temel

Agentın yalnızca metin üretmekle kalmayıp dış araçlarla işlem yapabilmesini, ana agent–alt agent görev devrini ve orkestrasyonu ele aldık. Görev devrinin bağımsız alt işlerde faydalı olabileceğini, fakat koordinasyon ve maliyet yükü getirdiğini konuştuk.

MCP'nin araç ve veri kaynaklarıyla standart bağlantı sağlaması üzerinde durduk. MCP'yi agentlar arası görev yönetimi protokolü olarak tanımlama karışıklığını düzelttik.

**Teze katkısı:** İncelenecek akışı doğru tanımlamak: kullanıcı → uygulama/agent → MCP aracı → kaynak. Görev devri varsa zincire alt agentlar da eklenir.

## 2. Kimlik, yetki ve görev kapsamı

Authentication ile authorization; kullanıcı onayı ile teknik yetki; teknik yetki ile mevcut görevin gerektirdiği erişim ayrımlarını çalıştık.

Kullanıcı, workload/servis ve agent kimliklerini karşılaştırdık. Ayrı kimlik tanımlamanın dar izinler ve izlenebilirlik için kullanılabileceğini, ancak ayrı kimliğin kendiliğinden dar yetki veya doğru davranış sağlamadığını gördük.

SPIFFE, X.509 ve sertifikaya bağlı token fikrini giriş düzeyinde ele aldık. Ayrıntılı kriptografik protokol uygulaması yapmadık.

**Teze katkısı:** Güvenli erişim gereksinimlerini katmanlara ayırmak. “Gerçek agent mı?” ile “Bu kaynağa bu işlemi yapabilir mi?” farklı sorulardır.

**Çıktılar:** [Kimlik modelleri](../ai-ve-mcp-guvenligi/kullanici-workload-agent-kimlikleri.md), [kimlik ve görev kapsamı](../ai-ve-mcp-guvenligi/kimlik-yetki-ve-gorev-kapsami.md).

## 3. Tokenların erişim sınırları

Bearer tokenın elde bulundurma esaslı kullanımını, sızıntıyı, geçerlilik süresini ve iptal mekanizmasının sisteme bağlılığını çalıştık. Yeni token üretmenin eskisini otomatik iptal etmeyebileceğini; erişimin kapatılmasının aktarılmış kopyaları geri almadığını ayırdık.

Audience ile hedef servisi, scope ile erişim kapsamını konuştuk. Doğru audience'ın bütün işlemleri yetkilendirmediğini; dar scope'un da tokenı yanlış kişinin kullanmasını tek başına önlemediğini gördük.

**Teze katkısı:** Erişimi kaynak, işlem ve süre açısından sınırlama; görevin bitmesi veya iptalinin türeyen erişimlere nasıl yansıyacağını araştırma.

**Çıktılar:** [Bearer token](../ai-ve-mcp-guvenligi/bearer-token-ve-sizinti.md), [audience ve scope](../ai-ve-mcp-guvenligi/token-audience-ve-scope.md).

## 4. Veri–talimat güven sınırı

Dolaylı prompt injection örneklerinde, dış belge veya araç çıktısının kullanıcı talimatı gibi uygulanması riskini çalıştık. Bu riskin her zaman yeni yetki elde etmek anlamına gelmediğini; mevcut yetkilerin yanlış amaçla kullanılabileceğini ayırdık.

Ayrı agent bağlamlarının ayrı kaynak izinleri anlamına gelmediğini konuştuk.

**Teze katkısı:** Tehdit modelini yalnız kimlik hırsızlığına daraltmamak; geçerli kimliğin ve izinlerin görev dışı kullanımını da ayrı değerlendirmek.

**Çıktı:** [Dolaylı prompt injection](../ai-ve-mcp-guvenligi/dolayli-prompt-injection.md).

## 5. Gerçek dosya erişimi ve sandbox

MCP-FSD okuması üzerinden kullanıcı onayı ile sunucu sürecinin gerçek dosya izinleri arasındaki farkı inceledik. Çalışma dizini, path traversal, benzer klasör adıyla hatalı kapsam kontrolü ve sandbox'ın rolünü örneklerle ele aldık.

**Teze katkısı:** Yetkilendirme politikasının gerçek kaynak erişiminde uygulanması; yalnızca arayüzde onay alınmasının yeterli olup olmadığının sorgulanması.

**Sınır:** Makalenin deneyleri yeniden üretilmedi; canlı MCP dosya erişim laboratuvarı kurulmadı.

**Çıktı:** [Dosya sınırları ve sandbox](../ai-ve-mcp-guvenligi/dosya-erisim-sinirlari-ve-sandbox.md).

## 6. Değerlendirme yaklaşımı

MS-Eval üzerinden görev devri uygunluğu ile işlevsel başarı, kritik adım sayısı ve maliyeti ayırdık. MSQ'nun güvenlik yüzdesi olmadığını gördük.

Güvenlik değerlendirmesinde saldırının engellenmesi yanında meşru görev başarısını ve yanlış engellemeleri de ölçme fikrini benimsedik. Başarısız çağrının politika reddinden mi, başka bir uygulama hatasından mı kaynaklandığını ayırma gereğini konuştuk.

**Teze katkısı:** Meşru görevleri bozan bir kontrolü yalnızca düşük saldırı başarısı nedeniyle başarılı saymamak. Güvenlik ve fayda ölçütlerini birlikte tasarlamak.

**Çıktı:** [MS-Eval](../ai-ve-mcp-guvenligi/ms-eval-gorev-devri-ve-degerlendirme.md).

## 7. Gerçekten yaptığımız uygulama

Kurgusal CSV'de giriş, oturum, dosya ve ağ olaylarını ilişkilendirerek olay incelemesi yaptık. Ardından kayan pencerede farklı hesaplara başarısız girişleri sayan ve başarılı oturumla eşleştiren Python örneğini çalıştırdık; dört mantık testi geçti.

Bu çalışma kanıt–hipotez ayrımı, korelasyon ve test disiplini kazandırır. **MCP yetkilendirme mekanizması veya tez deney sonucu değildir.** Kodun ilk taslağı asistan tarafından hazırlanmış, tasarım kararları ders sırasında birlikte tartışılmıştır; öğrencinin bağımsız geliştirdiği ürün olarak sunulmaz.

**Çıktı:** [Kod, veri, analiz ve testler](../guvenlik-operasyonlari/log-inceleme-01/README.md).

## 8. Kalıcı araştırma çıktıları

- GitHub'da konu bazlı ders arşivi.
- [Tez rehberi](README.md): Kaynakların olası kullanım yerleri.
- [Fikir ve cümle fişleri](fikir-ve-cumle-fisleri.md): Kaynak desteği, ders sentezi ve araştırma önerileri ayrı.

Fişler nihai tez metni veya tamamlanmış sistematik literatür taraması değildir. Seçicilik artırılacak; yalnızca somut bir tez argümanına katkı sağlayan ve mevcut fişleri tekrar etmeyen maddeler tutulacak.

## 9. Mevcut araştırma yönü — henüz karar değil

**Merkez soru:** Kullanıcının verdiği görev, agentın veya alt agentın MCP üzerinden yaptığı kaynak işlemlerine nasıl bağlanabilir ve bu sınırlar nasıl uygulanıp değerlendirilebilir?

Daraltılabilecek adaylar:

1. Tek agentta görevle sınırlı kaynak/işlem politikası ile daha geniş izinli erişimi karşılaştırmak.
2. İki alt agentta ortak görev bütçesinin ve görev iptalinin korunmasını incelemek.

Başlangıç için ilk seçenek daha küçük bir prototip kapsamı sunabilir; bu bir çalışma planlama önerisidir. Özgünlük ve literatür boşluğu henüz gösterilmemiştir.

Veri kökenini izleme yaklaşımı ilgili bir ek eksendir; otomatik olarak tezin ikinci büyük katkısı yapılmamalıdır.

## 10. Dünkü seçkinin durumu

| Kaynak | Mevcut durum |
|---|---|
| Decode-Time Provenance Binding | Açıklanmaya başlandı; mekanizma henüz tam oturmadı. Bugün daha sade yeniden ele alınacak. |
| NIST agent kimliği ilkeleri | Seçki paylaşılmış durumda; birlikte ayrıntılı çalışılmadı. |
| OAuth agent yetkilendirme taslağı v05 | Seçki paylaşılmış durumda; birlikte ayrıntılı çalışılmadı. |

Bu üç kaynak, bugün tamamlanacak okuma gündemidir; geçmişte bitmiş çalışma diye sunulmaz.

## 11. Hocaya sorulacak karar soruları

1. Tez ağırlığı mimari/literatür incelemesi mi, küçük bir deneysel prototip mi olmalı?
2. Başlangıçta tek agent–MCP–kaynak akışı yeterli mi, çok agentlı görev devri zorunlu mu?
3. Ana deney problemi görevle sınırlı erişim mi, ortak bütçe ve iptal mi seçilmeli?
4. Dosya veya veritabanı gibi tek kaynak türüne daraltmak uygun mu?
5. İlk teslim için literatür karşılaştırma tablosu, tehdit modeli ve deney taslağı yeterli mi?

## Görüşmede kullanılabilecek kısa anlatım

“Tez başlığını netleştirdikten sonra agentların araç kullanımı, MCP üzerinden erişim, kimlik doğrulama ve yetkilendirme ayrımı üzerinde çalıştım. Kullanıcı onayı, token kapsamı, gerçek kaynak izinleri ve görev sınırının aynı şey olmadığını örneklerle inceledim. Seçilmiş araştırmalar ve teknik belgeler için konu notları ve tezde kullanabileceğim kaynak fişleri hazırladım. Henüz MCP üzerinde özgün bir güvenlik prototipi veya karşılaştırmalı tez deneyi gerçekleştirmedim. Şimdi kapsamı daraltıp görevle sınırlı erişim için küçük ve ölçülebilir bir deney düzenine geçmek istiyorum. Bunun tek agentlı mı yoksa çok agentlı mı olması gerektiğini sizinle netleştirmek istiyorum.”

## Üç saatlik hazırlığın önerilen kullanımı

- 25 dakika: Bu ilerleme özetini anlama ve netleştirme.
- 30 dakika: İlk araştırmayı sade örnekle yeniden kurma.
- 5 dakika: Mola.
- 25 dakika: NIST ilkelerini kimlik–görev–yetki bağlarıyla okuma.
- 25 dakika: OAuth taslağını tek görev zinciri örneğiyle değerlendirme.
- 10 dakika: Eksikleri ve karşılaştırma tablosunu tamamlama.
- 30 dakika: Toplantıya hazırlık, kısa anlatım ve bağlantı payı.
- Kalan süre: Gerektiğinde bir bölüme ek açıklama; yeni konu eklememe.

Zamanlar hazırlık önerisidir; çalışılmış süre kaydı değildir.
