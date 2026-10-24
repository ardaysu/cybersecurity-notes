# MITRE ATT&CK Technique–Telemetry Eşleştirmesi

Tactic saldırganın amacını, technique yöntemi, sub-technique özel yöntemi açıklar. ATT&CK etiketi tek başına gerçek coverage kanıtı değildir. Her teknik; gözlemlenebilir davranış, gerekli telemetri/alanlar, detection mantığı, yakalanan varyasyonlar ve kör noktalarla belgelenmelidir.

Örnek eşleşmeler:

- PowerShell execution → process creation + PowerShell logging
- Dosya oluşturma → file telemetry
- Run key persistence → registry telemetry
- Beaconing/C2 ihtimali → network/NetFlow
- Password spraying → authentication telemetry; Timestamp, SourceIp, User ve Result
