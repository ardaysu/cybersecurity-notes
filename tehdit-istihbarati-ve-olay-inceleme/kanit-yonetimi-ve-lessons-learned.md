# Kanıt Yönetimi ve Lessons Learned

## Kanıt değerlendirme

- Kaynağın güvenilirliği
- Timestamp ve zaman dilimi
- Log bütünlüğü
- Olayın ham kaydı ile yorumun ayrılması
- Aynı davranışın bağımsız kaynaklarla doğrulanması
- Toplanan verinin kapsamı ve kör noktaları
- Yapılan analist aksiyonlarının kaydı

Bir alarm kanıt değildir; araştırılması gereken bir iddiadır. Kanıt, alarmı destekleyen veya çürüten gözlemlenebilir veridir.

## Lessons Learned

Olay kapatıldıktan sonra yalnızca “çözüldü” denmez:

- İlk erişim nasıl gerçekleşti?
- Hangi kontrol başarısız oldu?
- Hangi log veya detection eksikti?
- Olay neden erken görülmedi?
- Playbook yeterli miydi?
- Yeni detection veya tuning gerekli mi?
- Benzer olayın tekrarını önlemek için hangi sahip ve tarih belirlendi?

Lessons learned çıktısı; kontrol iyileştirmesi, yeni log kaynağı, kural, tuning, playbook veya eğitim aksiyonuna dönüşmelidir.
