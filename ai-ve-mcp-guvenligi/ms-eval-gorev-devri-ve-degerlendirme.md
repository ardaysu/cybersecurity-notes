# MS-Eval: Görev Devri, Fayda ve Güvenlik Ayrımı

## Ana fikir

**Daha fazla agent kullanmak, tek başına daha iyi sonuç demek değildir. İş bölümünün sağladığı faydayı, getirdiği ek yükle karşılaştırmalıyız.**

## Görev devri ve koordinasyon

Delegation, bir alt işi başka agenta vermektir. Orchestration, işlerin kime ve hangi sırayla verileceğini, bağımlılıkların nasıl yönetileceğini ve sonuçların nasıl birleştirileceğini düzenlemektir.

Ders için hazırlanan örnekte bir şirketin şüpheli hesap hareketini inceliyoruz:

- Ana agent araştırmayı planlıyor.
- Bir alt agent giriş kayıtlarını inceliyor.
- Diğeri dosya indirme kayıtlarını inceliyor.
- Ana agent sonuçları zaman sırası ve hesap/oturum ilişkileri açısından birleştiriyor.

İncelemeler birbirinden bağımsız yürüyebiliyorsa paralellik faydalı olabilir. Ama görevleri açıklamak, sonuçları kontrol etmek ve birleştirmek de iş yüküdür. Tek bir kayıttaki saati bulmak için aynı düzeni kurmak gereksiz olabilir.

Bu örnek araştırmanın deneylerinden aktarılmamıştır; mekanizmayı açıklayan eğitim senaryosudur.

## Araştırmanın değerlendirme yaklaşımı

MS-Eval, MCP araçlarının yoğun kullanıldığı görevlerde çok agentlı düzeni tek agentlı baseline ile karşılaştırır. Görev devrinin uygunluğunu ve koordinasyonun faydasını değerlendirir:

| Boyut | İncelenen konu |
|---|---|
| Görev devri | Gereksiz veya eksik devir; beklenen alt işlerle eşleşme |
| Performans | Görevlerin başarıyla tamamlanması |
| Verimlilik | Kritik işlem adımları |
| Maliyet | Tahmini API ücreti |

Verimlilik ölçütü doğrudan kronometre süresi değildir. MSQ, görev devri uygunluğu ile normalize edilmiş performans, verimlilik ve maliyet faydalarını birleştirir.

## Bulguyu doğru okumak

Araştırmanın uygulanabilir varyant karşılaştırmasında uzmanlaşmış alt agent düzeni en yüksek MSQ'yu alır. Görev devri genellikle maliyeti artırır; faydası model ve iş bölümüne bağlıdır. Sonuç, her ortamda daha fazla agent kullanılması gerektiği anlamına gelmez.

**%20,8 MSQ, görev başarı oranı veya güvenlik yüzdesi değildir.**

## Bir sonucu tek metrikle değerlendirmemek

Aşağıdaki sayılar yalnızca ders örneğidir:

| Sistem | Tamamlanan görev | Maliyet |
|---|---:|---:|
| Tek agent | 10 görevden 8'i | 1 birim |
| Çok agent | 10 görevden 9'u | 3 birim |

İkinci sistem daha fazla görevi tamamlıyor ama daha pahalı. Bu tablo tek başına hangisinin seçilmesi gerektiğini söylemez. Bir görevin kaçırılmasının etkisi, bütçe ve beklenen kalite de önemlidir.

Ayrıca örnek sayısı azsa görülen farkın ne kadar güvenilir olduğu sorgulanmalıdır. Açıklayıcı bir tablo, gerçek deney ve istatistiksel değerlendirme yerine geçmez.

## Bağlam izolasyonu ile yetki izolasyonu farklıdır

İki agentın konuşma geçmişlerinin ayrı olduğunu düşünelim. Biri diğerinin konuşmasını görmüyor olabilir. Fakat ikisine de aynı klasörü okuma izni verilmişse ikisi de o klasördeki dosyalara ulaşabilir.

- Bağlam izolasyonu: Agentın konuşma ve çalışma bilgisinin ayrılması.
- Yetki izolasyonu: Hangi kimliğin hangi kaynakta hangi işlemi yapabileceğinin sınırlandırılması.

**Birinin bulunması diğerini kanıtlamaz.**

Bu nedenle “MSQ yükseldi, sistem güvenli oldu” sonucu çıkarılamaz. Güvenlik iddiası için tehdit modeli, erişim politikaları ve saldırı testleri ayrıca değerlendirilmelidir.

## Tezim için araştırma fikri

Bu bölüm dersteki önerimizdir; makalenin doğrulanmış güvenlik sonucu değildir.

Görev bazlı dar izinler eklediğimiz bir agent sistemini önceki hâliyle karşılaştırabiliriz:

1. Yetkisiz erişim girişimleri engelleniyor mu?
2. İzinli görevler tamamlanabiliyor mu?
3. Ek onay ve yeniden denemeler gerekiyor mu?
4. Gecikme ve maliyet nasıl değişiyor?

Güvenlik kontrolü bütün işlemleri durdurarak saldırıyı engelliyorsa, meşru işin korunup korunmadığı da incelenmelidir. Böyle bir deneyde MS-Eval benzeri işlevsel ölçütler, ayrı güvenlik ölçütleriyle birlikte kullanılabilir.

## Kaynak ve kapsam

Ding ve arkadaşları, [MS-Eval: Benchmarking Sub-Agent Delegation and Orchestration in MCP-Intensive Working Scenarios](https://arxiv.org/html/2610.22869v1), ön baskı.

Bu not 26 Ekim 2026 dersindeki açıklama, örnek ve değerlendirmelerden hazırlanmıştır. Benchmark çalıştırılmamış, sonuçlar bağımsız yeniden üretilmemiştir.

[AI ve MCP Güvenliği](README.md)
