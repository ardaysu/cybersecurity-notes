# Faz 6 — Güvenlikte Makine Öğrenmesi ve Tez Hazırlığı

> **Durum:** Hızlandırılmış tez keşif turu devam ediyor  
> **İşlenen çekirdek:** Problem tanımı, metrikler, train/test, genelleme–ezberleme, leakage/shortcut learning ve adversarial ML'e giriş

## 1. Neden ML tabanlı saldırı tespiti?

Signature ve elle yazılmış kurallar bilinen davranışlarda açıklanabilir ve hızlıdır; ancak saldırgan küçük değişikliklerle göstergeleri yenileyebilir. ML, çok sayıda özellik arasındaki örüntüyü öğrenerek daha önce birebir görülmemiş varyasyonlara genelleme potansiyeli taşır.

Bu, “ML her zaman daha doğru ve kapsamlıdır” anlamına gelmez. Model:

- Hatalı/temsilsiz veri öğrenebilir,
- Sınıf dengesizliğinde çoğunluk sınıfına yaslanabilir,
- Ortam değişince bozulabilir,
- Saldırgan tarafından yanıltılabilir,
- Yüksek skor üretip yanlış nedene dayanabilir.

Bu nedenle pratikte hybrid yaklaşım değerlidir: kesin bilinen davranış için kural/signature, karmaşık örüntü için ML, karar için insan ve bağlam.

## 2. Dataset, feature ve label

- **Dataset:** Gözlem örneklerinin bütünü.
- **Feature:** Modelin karar verirken kullandığı ölçülebilir alan.
- **Label:** Öğrenilmek istenen doğru sınıf; ör. benign/attack.

Ağ IDS örneğinde source/destination port, duration, byte/packet sayısı, TCP flag oranları ve akış yönleri feature olabilir. IP adresini doğrudan feature yapmak modelin saldırı davranışı yerine laboratuvardaki tek IP'yi ezberlemesine yol açabilir.

## 3. Train, validation ve test

- **Train:** Model parametrelerini öğrenir.
- **Validation:** Model/hiperparametre seçimi ve geliştirme kararı için kullanılır.
- **Test:** En sonda, görülmemiş veri üzerindeki tarafsız performans tahminidir.

Test verisi geliştirme sırasında tekrar tekrar kullanılırsa artık gerçek test değildir; kararlarımız o sete uyum sağlar.

Referans noktası olmadan modelin gerçekten öğrendiğini bilemeyiz. Bu yüzden basit bir baseline gerekir: majority class, logistic regression, decision tree veya basit kural.

## 4. Accuracy neden yeterli değildir?

100.000 olayın 99.000'i benign, 1.000'i saldırı olsun. Her şeye benign diyen model %99 accuracy elde eder ama hiçbir saldırıyı yakalamaz.

- **Precision:** Alarm verdiklerinin ne kadarı gerçekten saldırı?
- **Recall:** Gerçek saldırıların ne kadarını yakaladın?
- **F1:** Precision ve recall'un harmonik ortalaması.

Güvenlik kullanımında maliyet bağlama bağlıdır. Kritik sistemde false negative pahalıdır; fakat aşırı false positive alarm yorgunluğu yaratıp fiilen false negative'e dönüşebilir.

Metrik mutlaka confusion matrix, sınıf dağılımı ve karar eşiğiyle birlikte okunmalıdır. ROC-AUC tek başına dengesiz veride yanıltıcı olabilir; PR-AUC saldırı sınıfına odaklanmada daha anlamlı olabilir.

## 5. Genelleme ve ezberleme

**Ezberleyen model**, eğitim verisindeki yüzeysel ayrıntıları hatırlar. **Genelleyen model**, altta yatan örüntüyü yeni örneklere taşır.

Örnek:

- Ezber: `185.x.x.x` gelirse saldırı.
- Öğrenme: Kısa sürede çok hedefe bağlantı, anormal flag oranı ve beklenmedik veri hacmi birlikteyse saldırı olasılığı yükselir.

Saldırgan farklı IP kullandığında ilk model bozulur; ikinci model davranış korunuyorsa yakalayabilir. Fakat feature'lar hâlâ veri toplama ortamına özgüyse ikinci model de görünüşte öğrenmiş olabilir.

## 6. Overfitting ve underfitting

- **Overfitting:** Train performansı çok iyi, yeni veride kötü; model gürültüyü ezberler.
- **Underfitting:** Model hem train hem testte zayıf; örüntüyü öğrenemeyecek kadar basit veya feature'lar yetersizdir.

Overfitting yalnızca “model çok karmaşık” demek değildir. Aynı campaign'in neredeyse kopya kayıtlarını rastgele train/test'e bölmek de test skorunu yapay yükseltir.

## 7. Data leakage

Leakage, modelin tahmin anında erişemeyeceği veya hedefi doğrudan ele veren bilginin eğitim/değerlendirmeye sızmasıdır.

Örnekler:

- Olay kapandıktan sonra eklenen `incident_confirmed` alanını feature yapmak
- Aynı akışın parçalarını train ve testte bulundurmak
- Preprocessing'i tüm veri üzerinde fit etmek
- Label üretiminde kullanılan kuralın çıktısını feature olarak vermek

Leakage modeli gerçekten iyileştirmez; sınavın cevap anahtarını masaya bırakır.

## 8. Shortcut learning ve spurious correlation

Model doğru etiketi yanlış nedenden tahmin edebilir. Laboratuvardaki tüm saldırılar gece üretilmişse model saldırı davranışını değil saati öğrenebilir. Belirli capture dosyası, IP bloğu veya araç izi de shortcut olabilir.

Kontroller:

- Feature importance/SHAP ile neye baktığını incelemek
- Zaman veya campaign bazlı ayrım yapmak
- IP/host gibi kimlik alanlarını kaldırarak ablation testi
- Farklı ortam/dataset üzerinde external validation
- Counterfactual veya küçük kontrollü değişikliklerle kararın sabitliğini test etmek

## 9. Veri bölme stratejisi

Random split çoğu tabular problemde başlangıçtır ama cybersecurity'de sızıntı yaratabilir. Daha gerçekçi seçenekler:

- **Time-based split:** Geçmişte eğit, gelecekte test et.
- **Group split:** Aynı host, kullanıcı, flow veya campaign parçalarını aynı tarafta tut.
- **Cross-environment test:** Başka ağ veya veri setinde değerlendir.

Amaç deploy anındaki bilinmeyeni simüle etmektir.

## 10. Baseline ve deney disiplini

Karmaşık deep learning modelinden önce basit modeller denenmelidir. Eğer decision tree aynı sonucu veriyorsa karmaşık modelin maliyeti açıklanmalıdır.

Deneyde sabitlenmesi gerekenler:

- Problem ve threat model
- Veri sürümü ve temizleme adımları
- Split yöntemi
- Feature listesi
- Preprocessing'in yalnız train üzerinde fit edilmesi
- Hiperparametre ve random seed
- Metrikler, güven aralığı ve çalışma maliyeti
- Kod/ortam sürümleri

## 11. Dataset shift

Üretim verisinin dağılımı eğitimden farklılaşabilir:

- Yeni uygulama veya protokol
- Kullanıcı davranışındaki değişim
- Saldırgan TTP değişimi
- Sensör/log şeması değişikliği

Model deploy edildiğinde çalışma bitmez. Feature dağılımı, alarm oranı, etiket gecikmesi ve periyodik performans izlenmelidir.

## 12. Adversarial ML ve evasion

Adversarial ML'de saldırgan yalnız sisteme saldırmaz; modelin karar mekanizmasını hedefler. **Evasion**, test/inference zamanında girdiyi değiştirerek saldırının benign sınıflandırılmasını sağlamaya çalışır.

Threat model net olmalıdır:

- Saldırgan model/gradient biliyor mu? White-box mı black-box mı?
- Hangi feature'ları değiştirebilir?
- Değişiklik gerçek ağ/protokol davranışında uygulanabilir mi?
- Saldırı işlevselliği korunuyor mu?
- Maliyeti ve sorgu bütçesi nedir?

Feature-space'te küçük sayısal değişiklik üretmek yeterli değildir. Ortaya çıkan örnek geçerli pakete/akışa dönüştürülemiyorsa problem-space saldırısı değildir.

## 13. Robustness

Robustness, modelin anlamı koruyan değişiklikler, gürültü, ortam farkı ve saldırgan manipülasyonu altında güvenilir kalabilmesidir.

Yalnız clean accuracy raporlanmaz:

- Clean performance
- Attack success rate
- Perturbation maliyeti
- Farklı saldırı/parametreler
- Adaptive attacker karşısındaki sonuç
- Savunmanın latency ve false-positive maliyeti

Adversarial training, feature squeezing, ensemble veya input validation gibi savunmalar değerlendirilebilir; her savunmanın kendi varsayımı ve bypass riski vardır.

## 14. XAI bağlantısı

XAI, modelin kararında hangi feature'ların etkili olduğunu açıklamaya çalışır. SOC için açıklama, alarmın araştırılabilir olmasını sağlar; araştırma için shortcut/leakage şüphesini gösterebilir.

Fakat açıklama doğru nedensellik garantisi değildir. SHAP/LIME gibi yöntemler model davranışını yaklaşık açıklar; modelin dünyayı doğru öğrendiğini ispatlamaz.

## 15. Tez yönü açısından çıkarım

Şu ana kadarki ilgi çizgisi özellikle şu kesişime yakındır:

```text
Detection Engineering
+ ML tabanlı IDS
+ adversarial evasion / robustness
+ açıklanabilirlik ve operasyonel kullanılabilirlik
```

İyi bir tez yalnız yüksek accuracy aramamalı; gerçekçi split, leakage kontrolü, saldırgan threat model'i, clean–adversarial performans dengesi ve SOC'a aktarılabilir açıklama üretmelidir.

## Faz 6'da sıradaki başlıklar

- Feature engineering ve preprocessing ayrıntıları
- Baseline modellerin karşılaştırılması
- Sınıf dengesizliği yöntemleri
- Adversarial example üretimi ve gerçekçilik
- Robustness enhancement
- XAI deneyleri
- Federated learning ve GNN'e kısa yön keşfi
- Tekrarlanabilir deney tasarımı
- Tez konularının ilgi, süre, veri ve iş değeriyle karşılaştırılması
