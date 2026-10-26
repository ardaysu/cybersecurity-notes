# Tez Rehberi: Kaynaklar, Argümanlar ve Araştırma Fikirleri

**Tez başlığı:** AI Agent Sistemlerinde MCP Tabanlı Araç ve Veri Erişiminin Güvenliği: Authentication ve Authorization Odaklı Bir İnceleme

Bu rehber, derslerde karşılaştığımız bilgileri tez yazımında yeniden bulmak için hazırlanmıştır. Nihai tez metni veya kapsam kararı değildir. Kaynakta bildirilen sonuçlar, kendi yorumlarımız ve henüz sınanmamış deney önerileri ayrı tutulur.

## 1. Tez bölümlerine göre kullanım haritası

| Olası bölüm | Kullanılabilecek konu | Dikkat edilecek sınır |
|---|---|---|
| Problem tanımı | Onaylanan işlem ile gerçek kaynak erişimi arasındaki fark | Bütün MCP dağıtımları aynı değildir. |
| Temel kavramlar | Kimlik doğrulama, yetkilendirme, kullanıcı/workload/agent kimlikleri | Kimliği kanıtlamak görev uygunluğunu kanıtlamaz. |
| İlgili çalışmalar | MCP-FSD ve erişim sınırlarının incelenmesi | Ön baskı; test ortamı ve seçilim sınırlılıkları var. |
| Mimari inceleme | Ayrı agent kimliği, dar izinler ve denetim kayıtları | Üretici belgesi bağımsız güvenlik deneyi değildir. |
| Değerlendirme yöntemi | Güvenlik yanında meşru görev başarısı ve maliyet | MSQ bir güvenlik metriği değildir. |

Bu tablo yazım için önerilen yerleşimdir; araştırmalar bu bölüm yapısını önermiş sayılmaz.

## 2. Kaynak kartları

### K01 — MCP-FSD

**Künye:** Huang ve arkadaşları, “My Credentials, Please”: Detecting Filesystem Capability Laundering in MCP Servers at Scale, 2026, ön baskı.

**Birincil kaynak:** https://arxiv.org/html/2610.22301v1

**Kaynağın desteklediği nokta:** Yerel MCP sunucularında araç sözleşmesi ve dağıtım kapsamı ile sunucu sürecinin gerçek dosya erişimi arasında açıklık oluşabilir. Çalışma statik tarama, sınır çıkarımı ve dinamik testler kullanır.

**Yöntemden alınabilecek fikir:** Koruma olmadan kapsam dışı erişim; koruma altında meşru işlem; koruma altında aynı erişim girişimi ayrı sınanır.

**Sınırlılık:** Sonuçlar incelenen, çalıştırılabilen dağıtımlara ve çıkarılan sınırlara bağlıdır. Bütün MCP ekosisteminin aynı açıklara sahip olduğu söylenemez.

**Bizim tez yorumumuz:** Kullanıcı onayı ve programın teknik kaynak izinleri ayrı incelenmeli. Bu yorum, kullanıcı onayının her sistemde etkisiz olduğu iddiası değildir.

**Ders bağlantısı:** [Dosya erişim sınırları ve sandbox](../ai-ve-mcp-guvenligi/dosya-erisim-sinirlari-ve-sandbox.md)

### K02 — MS-Eval

**Künye:** Ding ve arkadaşları, MS-Eval: Benchmarking Sub-Agent Delegation and Orchestration in MCP-Intensive Working Scenarios, 2026, ön baskı.

**Birincil kaynak:** https://arxiv.org/html/2610.22869v1

**Kaynağın desteklediği nokta:** Görev devrinin uygunluğu ile performans, kritik işlem adımları ve maliyet birlikte değerlendirilir. Tek agentlı sistem karşılaştırma noktasıdır.

**Kullanım yeri:** Güvenlik mekanizmasının meşru iş üzerindeki maliyetini ölçmek için yöntemsel referans.

**Sınırlılık:** MSQ güvenlik yüzdesi değildir; yüksek puan saldırılara dayanıklılık kanıtlamaz.

**Bizim tez yorumumuz:** İşlevsel başarı ölçütleri ile yetkisiz erişim ölçütleri birlikte raporlanabilir. Makalenin böyle bir güvenlik deneyi yaptığı ileri sürülmez.

**Ders bağlantısı:** [MS-Eval ders notu](../ai-ve-mcp-guvenligi/ms-eval-gorev-devri-ve-degerlendirme.md)

### K03 — Google Cloud MCP kimlik belgesi

**Tür:** Üretici teknik belgesi; hakemli araştırma veya bağımsız güvenlik testi değildir.

**Birincil kaynak:** https://docs.cloud.google.com/mcp/authenticate-mcp

**Kaynağın desteklediği nokta:** Kullanıcı, workload ve agent kimlikleri ayrılır. Ayrı kimliklere dar IAM rolleri verilebilir; kullanıcı kimliğiyle yapılan işlemler kullanıcıya atfedilebilir.

**Kullanım yeri:** Kimlik modelleri ve erişim mimarisi incelemesi.

**Sınırlılık:** Google Cloud'a özgü mekanizmalar bütün MCP sunucularına genellenemez.

**Bizim tez yorumumuz:** Ayrı kimlik, işlemi kimin gerçekleştirdiğini ayırmaya yardımcı olur; kullanıcı niyeti veya görevin meşruiyetini tek başına kanıtlamaz.

Bu kart dersin şu ana kadar incelenen kısmına dayanır. SPIFFE, sertifika ve token bağlama ayrıntıları burada tamamlanmış bir inceleme olarak sunulmamıştır.

## 3. Yazarken açıklanabilecek temel ayrımlar

Aşağıdakiler derslerde geliştirdiğimiz sentezdir. Nihai tezde her iddiaya uygun kaynak ve bağlam eşleştirilecektir.

- **Kimlik ile yetki:** Kimliği doğrulanan tarafın her kaynağa erişmesi gerekmez.
- **Onay ile yetki:** Kullanıcının işlemi istemesi, o işlem için yetkili olduğunu göstermez.
- **Teknik yetki ile görev kapsamı:** Agentın yapabildiği her işlem, mevcut görev için gerekli veya istenmiş değildir.
- **Bağlam ile erişim izolasyonu:** Ayrı konuşma geçmişleri, ayrı dosya izinleri sağlamaz.
- **Çalışma dizini ile güvenlik sınırı:** Başlangıç klasörü, erişimin yalnızca o klasörde kaldığı anlamına gelmez.
- **Engelleme ile kullanılabilirlik:** İstenmeyen erişimin engellenmesi yanında izinli işin korunması gerekir.
- **Kayıt ile önleme:** Denetim kaydı incelemeye yardım eder; tek başına işlemi durdurmaz.

## 4. Henüz sınanmamış araştırma soruları

### Soru A — Göreve göre daraltılmış erişim

Aynı görevde geniş kullanıcı erişimi ile ayrı ve dar yetkili agent kimliği kullanımı, yetkisiz kaynak erişimini ve meşru görev başarısını nasıl etkiler?

**Örnek deney taslağı:** Sahte belgeler içeren izole bir ortamda aynı görevler farklı izin düzenleriyle yürütülür. Gerçek kimlik bilgileri veya kişisel veriler kullanılmaz.

**Ölçüt adayları:** Yetkisiz erişim denemeleri ve gerçekleşen erişimler; izinli görev başarısı; yanlış engellemeler; gecikme, API maliyeti ve yeniden deneme sayısı.

### Soru B — Görev zincirinde kapsamın korunması

Ana agentın görevi alt agenta devretmesi sırasında kaynak ve işlem sınırları nasıl korunabilir?

**Ölçüt adayları:** Zincirde kapsam dışına çıkan çağrılar, erişilen kaynaklar, görev başarısı ve kayıtların kullanıcı–agent–işlem ilişkisini açıklayabilmesi.

Bu sorular uygulanmış deneyler veya doğrulanmış tez katkısı değildir. Literatür kapsamı, mevcut çalışmalarla fark, geliştirme yükü ve danışman görüşüyle daraltılmalıdır.

## 5. Kaynak kullanma kuralımız

Her yeni kartta kaynağın türü ve bağlantısı, desteklediği iddia, sınırlılık, olası tez bölümü ve bizim yorumumuz yer alır. Bir sonuç yazılacaksa kaynak içindeki bölüm, tablo veya şekil ayrıca doğrulanır. Nicel bulgular ölçüt ve paydası belirtilmeden aktarılmaz.

Tez metnine dönüşmeden önce künye, yayın durumu ve sürüm yeniden kontrol edilir. Üretici önerisi, deney sonucu ve bizim varsayımımız aynı kesinlikte yazılmaz.
