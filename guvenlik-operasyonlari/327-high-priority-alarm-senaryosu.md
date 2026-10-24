# 327 High-Priority Alarm Senaryosu

Bir sistemde 327 alarmın “high” görünmesi, 327 olayın da gerçekten aynı aciliyette olduğu anlamına gelmez. Vendor severity yalnızca başlangıç sinyalidir.

## Önceliklendirme ölçütleri

1. **Asset criticality:** Domain controller ile test cihazı eşit değildir.
2. **Identity privilege:** Admin hesabı ile standart kullanıcı eşit değildir.
3. **Detection confidence:** Tek zayıf sinyal ile çoklu doğrulama eşit değildir.
4. **Behavior / technique:** Credential dumping ile basit policy ihlali eşit değildir.
5. **Exposure:** İnternete açık sistem, iç sistemden farklı değerlendirilir.
6. **Blast radius:** Tek endpoint ile çok sayıda sisteme yayılan olay farklıdır.
7. **Corroboration:** EDR, identity ve network verisinin aynı hikâyeyi desteklemesi güveni artırır.

## EDR kanıtı neden öne çıkmıştı?

Şüpheli davranış endpoint üzerinde process, command line, parent process ve network bağlantısıyla birlikte görülüyorsa, alarm yalnızca reputation veya tek paket sinyaline dayanmaz. Davranış zinciri oluşur.

İdeal analist sonucu:

> “High etiketi tek başına öncelik belirlemez. Kritik varlık, ayrıcalıklı kimlik, detection confidence, saldırı tekniği, yayılma ihtimali ve bağımsız telemetriyle doğrulama birlikte değerlendirilir.”
