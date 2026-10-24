# ML Deney Tasarımı ve IDS Değerlendirmesi

Sohbetteki kavramsal açıklamalardan düzenlenmiştir. Sayısal örnekler varsayımsaldır; deney sonucu değildir.

## Dataset seçimi

IDS modeli; ağ bağlantıları, paketler veya sistem aktivitelerinden oluşan verilerle eğitilir. Hazır akademik datasetlere örnek olarak `UNSW-NB15`, `CIC-IDS2017` ve `CSE-CIC-IDS2018` verilebilir.

Dataset seçerken yalnızca büyüklüğüne bakmayız:

- Hangi saldırı türlerini içeriyor?
- Trafik güncel ve gerçekçi mi?
- Feature’lar gerçek sistemde üretilebilir mi?
- Sınıflar dengeli mi?
- Aynı oturumların train ve test tarafına karışma riski var mı?

Eski veya yapay bir datasette %99 başarı elde eden model gerçek kurumsal ağda aynı başarıyı göstermeyebilir. Buna **dataset shift** problemi bağlanır: Eğitim verisiyle gerçek dünya verisinin dağılımı farklıdır.

## Preprocessing

Ham veri doğrudan modele verilmeden hazırlanır:

```text
Eksik/hatalı değerleri temizleme
→ Kategorik alanları sayısallaştırma
→ Gerekirse ölçeklendirme
→ Gereksiz veya sızıntıya yol açan feature’ları çıkarma
→ Train/test ayrımı
→ Sınıf dengesizliğini ele alma
```

Kritik kural: Veriyi dönüştüren işlemler önce bütün dataset üzerinde öğrenilirse test bilgisi training tarafına sızabilir. Örneğin ölçeklendirme değerleri yalnızca training setinden öğrenilmeli, sonra test setine uygulanmalıdır.

## Baseline model

İlk olarak çok karmaşık model kurmayız. Decision Tree, Logistic Regression veya Random Forest gibi daha basit bir **baseline** oluştururuz.

Baseline, sonraki yöntemi karşılaştıracağımız referans noktasıdır:

```text
Basit Random Forest F1: %91
Karmaşık Deep Learning F1: %92
```

Deep Learning yalnızca %1 katkı sağlıyor ama eğitimi, açıklanması ve çalıştırılması çok daha zorsa gerçekten değerli olup olmadığını sorgularız.

Sektörel ilke:

> **Complexity must earn its place.**  
> Karmaşıklık, sağladığı katkıyı haklı çıkarmalıdır.

## Doğru değerlendirme

Tek bir accuracy sonucu yetmez. En azından:

- Confusion matrix
- Precision
- Recall
- F1
- Saldırı sınıfı bazında sonuçlar
- Farklı threshold sonuçları
- Mümkünse farklı zaman veya ortamdan test verisi

incelenir.

Bir modelin aynı datasette yüksek sonuç vermesi **in-dataset performance** gösterir. Başka bir dataset veya farklı dönem üzerinde başarılı olması ise **cross-dataset/generalization performance** açısından daha değerlidir.

Bu ilk paketin tez açısından sorusu şu:

> “Model gerçekten saldırıyı öğreniyor mu, yoksa datasetin kolaylıklarından mı faydalanıyor?”

Bu eksen seni çekerse tez; dataset leakage, shortcut learning, cross-dataset generalization veya gerçekçi IDS değerlendirmesi üzerine kurulabilir.

