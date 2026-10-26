# Kullanıcı, Workload ve Agent Kimlikleri

## Kimlikleri neden ayırıyoruz?

Bir kullanıcı raporlarını özetlemek için bir AI uygulamasından yardım istesin. İşi isteyen insan, çalışan uygulama ve belirli agent aynı kavram değildir.

| Kimlik | Temsil ettiği taraf |
|---|---|
| Kullanıcı | İnsan kullanıcı |
| Workload | Çalışan uygulama veya hizmet |
| Agent | Belirli AI agentı |

Servis hesabı, uygulama kimliği için kullanılabilen mekanizmalardan biridir. Bu kimlikler her istekte birlikte bulunmak zorunda değildir; kullanılan mimariye göre değerlendirilir.

Google Cloud belgesi kullanıcı, workload ve agent kimliklerini ayrı seçenekler olarak açıklar. Ayrı kimliğe dar izinler tanımlanabilir; kullanıcı kimliğiyle yapılan işlemler kullanıcıya atfedilebilir. Bu, Google Cloud'a özgü teknik belgedir; bütün MCP dağıtımları için ortak uygulama garantisi değildir.

## Ayrı kimlik ile dar izin aynı şey değil

Ders örneğimizde insan kullanıcının raporları okuma ve silme izni var. Özet çıkaran uygulamanın ise yalnızca okuması yeterli. Uygulama için ayrı kimlik tanımlayıp buna sadece gerekli okuma izinlerini verebiliriz.

Ancak ayrı kimliğe yine geniş izinler verirsek yalnızca isim değiştirmiş oluruz. Güvenlik katkısı, ayrılan kimliğe hangi izinlerin verildiğine ve bunların nasıl uygulandığına bağlıdır.

**Kullanıcı adına iş yapan programın, kullanıcının bütün yetkilerine ihtiyacı olmayabilir.**

## Denetim kayıtlarında kimlik

Basitleştirilmiş iki kayıt:

```text
Kimlik: aysu
İşlem: rapor oku
```

```text
Kimlik: rapor-ozetleyen-agent
İşlem: rapor oku
```

İlk satır tek başına insanın doğrudan mı yoksa uygulama üzerinden mi işlem yaptığını açıklamayabilir. Ayrı kimlik uygulamayı ayırt etmeyi kolaylaştırabilir. Bunlar ders için hazırlanmış kayıt örnekleridir, gerçek ürünün log şeması değildir.

Kendi tasarımımızda kullanıcı, agent, görev, kaynak, işlem ve sonucu ilişkilendirmek isteyebiliriz. Kimlik kaydı tek başına bütün bu bilgileri sağlamaz.

Kayıt tutmak ile engelleme farklıdır. İstenmeyen bir işlemin kaydedilmesi, işlemin durdurulduğu anlamına gelmez.

## SPIFFE, X.509 ve token bağlama

SPIFFE, yazılım iş yüklerine doğrulanabilir kimlikler sağlamak için kullanılan standarttır. X.509 sertifikası kimlik bilgisini açık anahtarla ilişkilendirir. Sertifikanın sunulması tek başına yeterli değildir; güven zinciri ve ilgili anahtarın kontrolüne ilişkin kanıtlar uygun protokolle doğrulanmalıdır.

Google belgesinin Agent Identity bölümünde Google Cloud erişim tokenlarının agentın X.509 sertifikasına kriptografik olarak bağlandığı belirtilir. Bu, tokenı ele geçiren başka bir tarafın onu tek başına kullanmasına karşı koruma sağlamayı amaçlar.

Bu mekanizma bütün MCP istemcilerinin otomatik özelliği değildir. Ayrıntılı kriptografik protokol incelemesi bu dersin kapsamı dışındadır.

## Kimlik kanıtı yanlış işlemi engeller mi?

Ders örneği: Gerçek agent doğru kimliğiyle bağlanıyor; rapor okuma ve e-posta gönderme izni var. Kullanıcı yalnızca raporun özetini istemiş. Agent raporu yanlış bir dış alıcıya gönderiyor.

Kimliğin doğru doğrulanması bu gönderimi tek başına durdurmaz. Gerçek agent da yanlış karar verebilir veya kötü niyetli içerikle yönlendirilebilir.

Üç kontrol ayrı düşünülür:

| Kontrol | Soru |
|---|---|
| Kimlik doğrulama | İsteği kim gönderiyor? |
| Yetkilendirme | Bu kimlik, bu kaynakta bu işlemi yapabilir mi? |
| Görev kapsamı | İşlem, kullanıcının mevcut isteğinin parçası mı? |

Alıcı sınırı, veri paylaşım politikası veya işleme özel onay gibi mekanizmalar ayrıca tasarlanabilir. Görev kapsamı ayrı bir düşünme eksenidir; bunu uygulayan her sisteme ait zorunlu üçüncü bir standart katman olduğu ileri sürülmez. Görev koşulları yetkilendirme politikası içinde de temsil edilebilir.

**Kimliği doğru doğrulanan agent da yanlış işlem yapabilir.**

## Tezde kullanım

Bu ders kimlik mimarisini, en az ayrıcalığı ve görev düzeyindeki yetkilendirme ihtiyacını birlikte tartışmak için kullanılabilir. Güçlü kimlik doğrulamanın güvenli davranışı garanti ettiğini söylemek yerine, hangi tehdide karşı ne sağladığı ayrı yazılmalıdır.

## Kaynak ve sınır

- [Google Cloud: Authenticate to Google and Google Cloud MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp), özellikle Authentication identities ve Use an agent identity for authentication bölümleri.

Belge üretici mimarisini açıklar; bağımsız saldırı deneyi veya nicel güvenlik başarısı sunmaz. Rapor ve log örnekleri ders sentezidir. Herhangi bir bulut kurulumu yapılmamıştır.

[AI ve MCP Güvenliği](README.md)
