# Detection-as-code

Detection kurallarını yalnızca SIEM arayüzünde değil; Git ile sürümlenen, review edilen, test edilen ve kontrollü deploy edilen dosyalar olarak yönetme yaklaşımıdır.

## Temel kazanımlar

- Kim, neyi, neden ve ne zaman değiştirdiği izlenir.
- Pull request ile varsayımlar ve kör noktalar farklı kişilerce incelenir.
- Syntax/lint, fonksiyonel ve regression testleri otomatikleştirilebilir.
- Kötü değişiklik bilinen son güvenli sürüme rollback edilebilir.
- Test, pilot/shadow ve production geçişleri kontrol edilir.

## Örnek vaka

Gürültüyü azaltmak için bütün IT kullanıcılarını hariç tutmak, ele geçirilmiş IT hesabını görünmez kılan geniş bir kör nokta oluşturdu. İstisna; belirli yönetim sunucusu, onaylı script, imza/hash, service account ve beklenen zaman gibi koşullarla daraltıldı.

**Önemli ayrım:** Syntax testinin geçmesi kuralın saldırıyı yakaladığını kanıtlamaz. Gerçek saldırı örneğiyle pozitif test, normal örnekle negatif test ve önceki hatanın dönmesini engelleyen regression testi gerekir.
