# YZM301 — Kurulum Raporu

**Tarih:** 2026-10-26
**Kapsam:** G*Power 3.1.9.7 χ² hesabının tersine mühendisliği için ortam kurulumu ve doğrulaması.
**Not:** Bu oturumda hiçbir analiz yapılmadı; GPowerNT.exe çalıştırılmadı, açılmadı, decompile edilmedi.

## 1. Araçlar ve sürümler

| Araç | Sürüm | Durum |
|---|---|---|
| Node.js | v24.21.0 | ✅ |
| REA (`rea-agents`) | 6.7.0 | ✅ Sabit sürüm (npm'de 6.8.0 mevcut, bilerek güncellenmedi) |
| Claude Code | 2.1.310 | ✅ |
| Python | 3.13.14 | ✅ |
| Git | 2.53.0.windows.2 | ✅ |
| Java (JDK) | Temurin 21.0.12.1 LTS, 64-bit (`C:\Program Files\Eclipse Adoptium\jdk-21.0.12.101-hotspot`) | ✅ |
| GitHub CLI (`gh`) | 2.103.2 | ✅ (kurulu bulundu) |
| Ghidra (REA'nın kullandığı) | 12.1.4 — `C:\Users\elanu\Tools\ghidra_12.1.4_PUBLIC` | ✅ |
| Ghidra (elle kurulan) | 11.4.3 — `C:\yzm301\tools\ghidra_11.4.3_PUBLIC` | ⚪ Kullanılmayacak |
| G*Power | 3.1.9.7 (FileVersion = ProductVersion = 3.1.9.7, Company: Franz Faul) | ✅ |

## 2. G*Power program dosyası

- **Orijinal yol:** `C:\yzm301\tools\gpower-kurulum\GPower_3.1.9.7_143\GPowerNT.exe` (2 287 616 bayt)
- Aynı klasörde: `VC_redist.x86.exe`, `Close.wav`, `Minimieren.wav`
- **İnceleme kopyası:** `C:\yzm301\inceleme\GPowerNT.exe` — ✅ kopyalandı (2 287 616 bayt, FileVersion 3.1.9.7). Orijinal yerinde duruyor.
  Hedef yolda başta `GPowerNT.exe` adında **boş bir klasör** vardı. Kullanıcı onayıyla, klasör olduğu ve içinin boş olduğu (gizli dosyalar dahil 0 öğe, bağlantı değil) doğrulandıktan sonra yalnızca o boş klasör silindi.

## 3. SHA-256 doğrulaması

| | Değer |
|---|---|
| Beklenen | `C63E6A133EB6372932F810C08CC33DC35A06D1DDB658F897BD6C34A754EFC812` |
| Orijinal (hesaplanan) | `C63E6A133EB6372932F810C08CC33DC35A06D1DDB658F897BD6C34A754EFC812` |
| Sonuç | ✅ Orijinal **eşleşiyor** |
| Kopya (hesaplanan) | `C63E6A133EB6372932F810C08CC33DC35A06D1DDB658F897BD6C34A754EFC812` |
| Sonuç | ✅ Kopya **eşleşiyor** |

Ayrıntı: `C:\yzm301\gpower_hash.txt`

## 4. Tedarik zinciri kontrolü

`npm view rea-agents repository.url homepage` çıktısı:

```
repository.url = 'git+https://github.com/morluto/rea.git'
homepage = 'https://github.com/morluto/rea#readme'
```

✅ Paketin resmi kaynağı **github.com/morluto/rea** ile eşleşiyor. (Registry'deki en son sürüm 6.8.0; yerelde 6.7.0 kullanılıyor.)

## 5. REA durumu

- `rea doctor`: **`healthy: true`, `environment_healthy: true`** — tam çıktı `C:\yzm301\rea_doctor.txt`
- Ghidra sağlayıcısı: `configured: true`, `available: true`, `providerVersion: 12.1.4`, `JAVA_HOME` = Temurin JDK 21
- Eksik ama gerekmeyen sağlayıcılar: Hopper (Windows'ta desteklenmiyor), IDA, JADX, Kuna — yapılandırılmamış
- **Bu Claude Code oturumunda REA MCP araçları:** görünüyor, **207 araç** (doctor'daki `mcp_tools: 207` ile aynı)
- Canlı sunucu (`binary_session`, hedef açmadan): rea 6.7.0, istemci claude-code 2.1.310, açık hedef yok, **Ghidra adayı `available`**

## 6. Notlar

- Yönerge "Ghidra + JDK 21" diyor; REA'nın kurduğu **Ghidra 12.1.4, JDK 21 ile çalışıyor** (kanıt: `rea doctor` → `ghidra-java: 21.0.12.1; 64-bit; JDK … accepted a 64-bit full JDK 21 or newer`).
- Elle denenen **Ghidra 12.2 JDK 25 istedi**; kullanılmadı.
- G*Power Windows dağıtımı **kurulumsuz (taşınabilir)** geliyor; program dosyası **GPowerNT.exe**.
- **REA 6.8.0 güncellemesi bilerek yapılmadı** (proje boyunca sürüm 6.7.0'da sabit).
- `C:\yzm301\tools\ghidra_11.4.3_PUBLIC` elle kuruldu, kullanılmayacak (silinmedi).
