# Tez İçin Fikir ve Cümle Fişleri

**Tez:** AI Agent Sistemlerinde MCP Tabanlı Araç ve Veri Erişiminin Güvenliği: Authentication ve Authorization Odaklı Bir İnceleme

Bu arşiv derslerden, okumalardan ve tartışmalardan tezde kullanılabilecek fikirleri seçer. Cümleler doğrudan alıntı değil, tez yazımı için Türkçe taslaklardır. “Kaynaklı” fişlerde belirtilen bölüm desteği vardır; “ders sentezi” fişlerde yorum bize aittir ve nihai akademik iddia için kaynaklandırma tamamlanmalıdır. Bunlar kanıtlanmış özgün katkılar olarak sunulmaz.

## F01 — Kullanıcı onayı kaynak sınırını uygulamaz

**Cümle taslağı:** “Bir araç çağrısına verilen kullanıcı onayı, çağrıyı gerçekleştiren sunucu sürecinin dosya erişiminin görev kapsamıyla sınırlandırıldığını tek başına göstermez.”

**Dayanak:** Kaynaklı özet. [MCP-FSD §2.1–2.2](https://arxiv.org/html/2610.22301v1#S2.SS1), yerel stdio sunucuları ve sunucu tarafındaki kapsam dışı etkileri ele alır.

**Tezde yeri:** Girişte problem tanımı; onay ve yetkilendirme ayrımı.

**Kullanım sınırı:** Yerel dağıtım bağlamını belirt. Bütün MCP istemcilerinin aynı biçimde davrandığını ileri sürme.

## F02 — Güvenlik değerlendirmesi meşru işin korunmasını da ölçmeli

**Cümle taslağı:** “Bir erişim kontrolünün değerlendirilmesinde, kapsam dışı işlemlerin engellenmesi ile kapsam içi işlemlerin korunması birlikte incelenmelidir.”

**Dayanak:** Kaynaklı yöntem uyarlaması. [MCP-FSD §3.3](https://arxiv.org/html/2610.22301v1#S3.SS3), korumasız saldırıyı, sandbox altında meşru işlemi ve sandbox altında saldırıyı ayrı test eder.

**Tezde yeri:** Deney tasarımı ve değerlendirme ölçütleri.

**Bizim kullanımımız:** Başarısız meşru görevleri de raporlamak. Bu, tez deneyimizin uygulanmış olduğu anlamına gelmez.

## F03 — Dosya yolunun görünümü ile gerçek kapsam farklı olabilir

**Cümle taslağı:** “Kaynak sınırlarının uygulanması, dosya yollarının yalnızca metinsel benzerliğine değil, çözümlenen hedefin izin verilen alanda kalmasına dayanmalıdır.”

**Dayanak:** Kaynakla ilişkili ders sentezi. [MCP-FSD §1 ve §3.1](https://arxiv.org/html/2610.22301v1#S3.SS1), yol denetimi hatalarını tartışır. Dersteki Projem / Projem-Ozel örneği bizim açıklama örneğimizdir.

**Tezde yeri:** Tehditler ve uygulama düzeyindeki yetkilendirme hataları.

**Kullanım sınırı:** Bu cümle tek başına eksiksiz güvenli dosya erişimi algoritması değildir; sembolik bağlantılar ve yarış durumları ayrıca ele alınır.

## F04 — Çok agentlı sistemin işlevsel başarısı güvenlik kanıtı değildir

**Cümle taslağı:** “Görev devrinin kalitesini ölçen bir performans göstergesi, ayrıca tanımlanmış bir tehdit modeli ve güvenlik testleri olmadan yetkisiz erişime dayanıklılık kanıtı olarak yorumlanmamalıdır.”

**Dayanak:** Kaynaktan hareketle yöntemsel yorumumuz. [MS-Eval §4.3](https://arxiv.org/html/2610.22869v1#S4.SS3), görev devri uygunluğu ile başarı, kritik adım ve maliyet faydalarını değerlendirir.

**Tezde yeri:** Metrik seçimi ve ilgili çalışmaların karşılaştırılması.

**Kullanım sınırı:** MSQ güvenlik yüzdesi veya görev başarı oranı diye yazılmaz.

## F05 — Bağlam izolasyonu ve yetki izolasyonu ayrı eksenlerdir

**Cümle taslağı:** “Agentların ayrı bağlam pencerelerinde çalışması, erişebildikleri kaynakların ve gerçekleştirebildikleri işlemlerin de birbirinden yalıtıldığı sonucunu doğurmaz.”

**Dayanak:** Ders sentezi. MS-Eval'in [§3.1](https://arxiv.org/html/2610.22869v1#S3.SS1) bölümü ayrı bağlamları ve araç kısıtlarını anlatır; bunlar farklı mekanizmalardır.

**Tezde yeri:** Mimari varsayımlar ve güven sınırları.

**Örneğimiz:** Konuşma geçmişleri ayrı olan iki agent aynı dosya okuma izinlerini paylaşabilir.

**Kullanım sınırı:** MS-Eval'in erişim kontrolünü ihlal ettiğinin gösterildiği iddia edilmez.

## F06 — Güvenlik maliyeti baseline ile görünür kılınabilir

**Cümle taslağı:** “Önerilen yetkilendirme yaklaşımının etkisi, güvenlik kazanımına ek olarak meşru görev başarısı ve kaynak maliyeti bakımından bir referans düzenle karşılaştırılabilir.”

**Dayanak:** Ders içindeki deney önerimiz. MS-Eval'in tek agentlı karşılaştırması ve [§4.3.2](https://arxiv.org/html/2610.22869v1#S4.SS3.SSS2) ölçütleri yöntemsel esin kaynağıdır.

**Tezde yeri:** Yöntem; değerlendirme.

**Araştırma fikri:** Geniş erişim ile görev bazında dar erişimi aynı görev kümesinde karşılaştırmak.

**Kullanım sınırı:** Gecikme ile kritik işlem adımları aynı ölçüt değildir; kullanılacak ölçüler ayrıca tanımlanır.

## F07 — Kullanıcının bütün yetkileri agenta aktarılmak zorunda değildir

**Cümle taslağı:** “Uygulama için ayrı kimlik kullanımı, insan kullanıcının geniş erişiminden bağımsız olarak uygulamanın ihtiyaç duyduğu izinlerin tanımlanmasına olanak verebilir.”

**Dayanak:** Kaynaklı özet. [Google Cloud MCP belgesi, User, workload, and agent identities](https://docs.cloud.google.com/mcp/authenticate-mcp#user_workload_and_agent_identities), ayrı kimlik ve en az gerekli IAM izinlerini önerir.

**Tezde yeri:** Kimlik modelleri; en az ayrıcalık.

**Kullanım sınırı:** Kimliği ayırmak tek başına yeterli değildir; kimliğe gerçekten hangi izinlerin verildiği belirleyicidir. Google Cloud mimarisi bütün MCP sunucularına genellenmez.

## F08 — Kimliğin izlenebilirliği görev meşruiyetini kanıtlamaz

**Cümle taslağı:** “Bir işlemin belirli bir agent kimliğine atfedilebilmesi, işlemin kullanıcı niyeti ve görevin kapsamıyla uyumlu olduğunu tek başına kanıtlamaz.”

**Dayanak:** Ders sentezi. Google belgesinin [MCP requests and authentication](https://docs.cloud.google.com/mcp/authenticate-mcp#how_mcp_requests_and_authentication_work) bölümü işlemlerin kullanılan kimliğe atfedilmesini açıklar; görev uygunluğu ayrımı bizim yorumumuzdur.

**Tezde yeri:** Hesap verebilirlik, denetim ve görev bağlamı.

**Araştırma fikri:** Kullanıcı–agent–görev–kaynak–işlem ilişkisini kayıtlarla izlemek.

**Kullanım sınırı:** Bu bilgilerin her üründe kendiliğinden kaydedildiği varsayılmaz.

## F09 — Araç çıktısı görev verme yetkisine sahip değildir

**Cümle taslağı:** “Dış kaynaklardan veya araçlardan gelen içerik, kullanıcı tarafından tanımlanan görevi değiştirebilen yetkili bir talimat olarak kabul edilmemelidir.”

**Dayanak:** Kaynaklı savunma ilkesi. [Anthropic, Indirect prompt injection](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks#indirect-prompt-injection), üçüncü taraf içerikteki yönlendirici talimatları ve güvenilmeyen içerik ayrımını açıklar.

**Tezde yeri:** Tehdit modeli; veri ve talimat arasındaki güven sınırı.

**Kullanım sınırı:** Üretici savunma önerisidir; tek başına saldırıların tamamen engellendiğine dair deneysel kanıt değildir.

## F10 — Prompt injection her zaman yeni yetki kazandırmaz

**Cümle taslağı:** “Bir prompt injection girişimi, yeni bir teknik ayrıcalık elde etmeksizin agentın mevcut izinlerini kullanıcı tarafından istenmeyen bir amaçla kullanmasına neden olabilir.”

**Dayanak:** Ders sentezi; yukarıdaki prompt injection kaynağı bağlam sağlar. Yeni yetki elde etme ile mevcut yetkiyi yanlış amaçla kullanma ayrımını dersimizde kurduk.

**Tezde yeri:** Saldırı sınıflandırması ve yetkilendirmenin motivasyonu.

**Örneğimiz:** Belge özetleyen agentın zaten sahip olduğu gönderme aracını kötü niyetli belge içeriği doğrultusunda kullanması.

**Kullanım sınırı:** Her prompt injection yetki yükseltmedir veya bütün girişimler başarılı olur diye yazılmaz.

## F11 — Yetkili hesap hareketi ile meşru kullanım aynı şey değildir

**Cümle taslağı:** “Bir işlemin hesap izinleriyle uyumlu olması, hesabın gerçek sahibi tarafından veya meşru bir amaçla gerçekleştirildiğini tek başına göstermez.”

**Dayanak:** Ders sentezi; şu anda belirli bir akademik kaynağa atfedilmemiştir.

**Tezde yeri:** Yetkilendirmenin sınırları ve tehdit modeli.

**Ders bağlantısı:** [Kanıt ve şüphe ayrımı](../tehdit-istihbarati-ve-olay-inceleme/engelleme-sonrasi-inceleme.md).

**Tez bağlantısı:** Hesap ele geçirme ile agentın yanlış yönlendirilmesi ayrı tehditler olsa da mevcut izinlerle istenmeyen işlem yapılması açısından birlikte tartışılabilir.

**Sonraki adım:** Nihai tezde kullanılmadan önce uygun erişim kontrolü ve hesap kötüye kullanımı kaynakları bulunmalı.

## F12 — Başarısız çağrı, engelleme mekanizmasını tek başına açıklamaz

**Cümle taslağı:** “Bir erişim girişiminin başarısız olması, başarısızlığın önerilen yetkilendirme mekanizmasından kaynaklandığını göstermeye yeterli değildir.”

**Dayanak:** Ders sentezi; deney tasarımı önerisi.

**Tezde yeri:** Deney geçerliliği ve ölçüm yöntemi.

**Örneğimiz:** Dosya bulunamamış, istek yanlış hazırlanmış veya uygulama çökmüş olabilir. Politika reddi ile ilgisiz yürütme hatası ayrılmalıdır.

**Araştırma fikri:** Çağrı sonucu, politika kararı ve gerçek kaynak etkisini ayrı gözlemlemek; reddi, engellenmiş işlemle karıştırmamak.

## F13 — Görev devri yetki genişletme gerekçesi olmamalı

**Cümle taslağı:** “Bir görevin alt agenta devredilmesi sırasında, görev için gerekli kaynak ve işlem sınırlarının korunması ayrı bir tasarım gereksinimi olarak ele alınabilir.”

**Dayanak:** Bizim araştırma önerimiz; henüz doğrulanmış sonuç veya kanıtlanmış literatür boşluğu değildir.

**Tezde yeri:** Araştırma soruları ve önerilen mimari.

**Araştırma sorusu:** Ana agent–alt agent–MCP aracı zincirinde görev kapsamını taşıyan bir mekanizma, meşru işleri korurken kapsam dışı işlemleri azaltabilir mi?

**İnceleme gereği:** Görev/işlem/kaynak/süre sınırlarının temsili, kapsamın genişletilmesinin nasıl önleneceği ve mevcut çalışmalarla fark.

## F14 — Kayıt ile önleme birbirini tamamlar

**Cümle taslağı:** “Denetim kayıtları bir işlemin sonradan incelenmesini desteklerken, erişim kontrolü işlem sırasında izin sınırının uygulanmasına yöneliktir.”

**Dayanak:** Ders sentezi; belirli bir ürüne ait garanti olarak sunulmaz.

**Tezde yeri:** Mimari katmanlar ve değerlendirme.

**Örneğimiz:** İstenmeyen dosya aktarımının kaydının bulunması, aktarımın engellendiği anlamına gelmez. Tersine bir reddin kaydı da işlemin gerçekte uygulanmadığını doğrulayan etki gözlemiyle güçlendirilebilir.

**Sonraki adım:** Tezde kullanılacak kayıt şeması ve politika uygulama noktası açıkça tanımlanmalı.

## Bu fişler nasıl kullanılacak?

Cümleler kopyalanmaya hazır nihai akademik metin değil, kaynak ve yorum sınırları belirtilmiş yazım malzemesidir. Kaynaklı cümleler bile tez bağlamına uyarlanmalı; sürüm, bölüm ve yayın durumu yazım sırasında kontrol edilmelidir. Ders sentezleri araştırma motivasyonu sağlayabilir, ancak özgün katkı iddiası için literatür karşılaştırması ve deney gerekir.

[Tez rehberi](README.md)
