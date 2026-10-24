# Genelleme, Ezberleme ve Modelin Öğrendiğini Sınama

Sohbetteki kavramsal açıklamalardan düzenlenmiştir. Sayısal örnekler varsayımsaldır; deney sonucu değildir.

- Model saldırının davranışını öğrendiyse, kaynak IP değişse bile diğer özelliklerden saldırıyı tanıyabilir.
- Model `bu IP → saldırı` kestirmesini ezberlediyse, yeni IP’den gelen aynı saldırıyı normal sanabilir. Bu da **false negative** üretir.

Burada önemli kavram **invariance — değişmezlik**: Saldırının özü aynı kalırken IP gibi yüzeysel bir özellik değiştiğinde modelin kararının mümkün olduğunca değişmemesini isteriz.

Fakat modelin ne öğrendiğini içeriden doğrudan göremeyiz. Bunu deneylerle test ederiz:

1. **IP’yi feature listesinden çıkarırız.** Başarı çöküyorsa model IP’ye aşırı bağımlı olabilir.
2. **Test setine eğitimde hiç görülmeyen IP’leri koyarız.** Yeni kaynaklara genelleyebiliyor mu bakarız.
3. **Zamana göre bölme yaparız.** Geçmiş trafikle eğitip gelecekteki trafik üzerinde test ederiz.
4. **Feature importance veya SHAP kullanırız.** Modelin kararında hangi özelliklerin etkili olduğunu inceleriz.
5. **IP ve değiştirilebilir alanları kontrollü biçimde değiştiririz.** Modelin kararı kolayca saldırıdan normale dönüyor mu ölçeriz.

Üç sektörel/akademik kavram burada birleşiyor:

- **Feature importance:** Model hangi bilgilere ne kadar dayanıyor?
- **Explainability / XAI:** Model bu kararı neden verdi?
- **Robustness:** Küçük ve gerçekçi değişikliklerde kararını koruyabiliyor mu?

Bu yüzden XAI ve adversarial robustness birbirinden tamamen kopuk tez alanları değil. XAI bize modelin kırılgan biçimde neye dayandığını gösterebilir; adversarial test de bu bağımlılığın gerçekten istismar edilip edilemeyeceğini ölçebilir.

