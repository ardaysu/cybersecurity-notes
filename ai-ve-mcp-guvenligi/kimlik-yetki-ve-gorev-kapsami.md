# Kimlik, Yetki ve Görev Kapsamı

## Authentication ve authorization

Authentication kimlik doğrulamadır: Bir kullanıcının veya uygulamanın iddia ettiği kimliği kanıtlamasını sağlar. Authorization ise o kimliğin belirli bir kaynakta belirli işlemi yapıp yapamayacağına karar verir. Başarılı giriş, bütün kaynaklara erişim veya bütün işlemleri gerçekleştirme izni anlamına gelmez.

Yetkiyi yalnızca kullanıcı adıyla düşünmek eksik kalır. Kararda kullanıcı veya agent kimliği, erişilen kaynak ve istenen işlem birlikte değerlendirilir. Bir kullanıcı kendi takviminde toplantı silebilirken ekip takviminde yalnızca okuma iznine sahip olabilir.

## Kullanıcı onayı neden yetki değildir?

“Bu toplantıyı sil” talebi, kullanıcının işlemi istediğini gösterir. Kullanıcının o toplantıyı silmeye yetkili olduğunu göstermez. Kullanıcıya tekrar “Emin misin?” diye sormak da eksik yetkinin yerine geçmez. Geçerli yetki kontrolü işlemi karşılayan sistem tarafından uygulanmalıdır.

Yönetici istediği iddiası da tek başına izinleri değiştirmez. Yetki değişimi, yetkili kişinin onay verdiği ve sistemin uyguladığı bir süreçle yapılır. Burada belirleyici olan isteğin sözlü veya yazılı olması değil, geçerli yetkilendirme sürecidir.

## MCP'nin rolü

MCP, AI uygulamalarının dış araçlara ve veri kaynaklarına standart biçimde bağlanmasını sağlayan bir protokoldür. Temel rolü agentlar arasında görev dağıtımı yapmak değildir. Araç bağlantısının bulunması, her işlemin güvenli veya yetkili olduğu garantisini de vermez.

Örnek sistemde agent Aysu adına çalışıyorsa erişim kurallarının bu kimlik ve görev bağlamını koruması gerekir. Gerçek bir uygulamada kullanıcı kimliği, agent kimliği ve araç servisinin kimliği ayrı olabilir; izinlerin aynı olduğu varsayılmamalıdır.

## En az ayrıcalık ve görevin sınırı

Agenta işi için gereken izinler verilir. “Dosya gönderme” izni de tek parça düşünülmemelidir: Hangi dosyayı, hangi alıcıya, hangi amaçla gönderebilir? Okuma, değiştirme, silme ve dışarı aktarma farklı işlemlerdir.

**Agentın yapabildiği her işlem, kullanıcının o görev için yapılmasını istediği bir işlem değildir.** Teknik yetki ile göreve uygunluk birlikte değerlendirilmelidir.

## Kaynak

- [Resmî MCP tanıtımı](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/docs/2026-07-28/getting-started/intro.mdx)

