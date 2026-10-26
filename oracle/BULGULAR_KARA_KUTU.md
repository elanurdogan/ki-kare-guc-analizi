# Kara Kutu Bulguları — K4 chi2-contingency

> Bu dosya, G*Power 3.1.9.7'nin arayüzünde **gözlenen** davranışı kaydeder; yorum ve tahmin içermez.
> LEDGER.md ve README "Yorum kararları" bölümü için kaynaktır.

**Kaynaklar:**
- `K4_gui_protokol.txt`: Protocol of power analyses, 1. tur, 2026-10-26 20:21–21:04. Kayıt referansı `[n]`.
- `K4_gui_protokol_EK.txt`: ek tur, 21:36–21:52; G*Power yeniden açıldığı için numaralar 1'den başlıyor. Kayıt referansı `EK[n]`.
- `K4_hata_notları.txt`: ham notlar; ek tur notları sona eklendi.
- `K4_hata_notlari_EK.txt`
- `screenshots/K4-001.png … K4-043.png`, ayrıca ilk çekimler `K4-031_ilk.png`, `K4-033_ilk.png`, `K4-034_ilk.png`
- `K4_gui_results.csv`

**Kapsam:** K4-001 … K4-043 (K4_plan.csv; K4-043 plan dışı ek). İki protokolde toplam 37 kayıt var; 36'sı girdilerine göre bir vektörle eşleşti. Eşleşmeyen 1 kayıt ([32], yanlış modla yapılmış deneme) vektör setine dahil değil; bkz. `K4_hata_notlari_EK.txt`.

## Özet

| Tepki | Sayı | Vektörler |
|---|---|---|
| Sonuç üretti | 31 | K4-001 … K4-030, K4-032 |
| Sonuç üretti, girdi sözleşmeye göre geçersiz | 5 | K4-036, K4-039, K4-040, K4-041, K4-043 |
| Hata diyaloğu ("Input error"), sonuç yok | 7 | K4-031, K4-033, K4-034, K4-035, K4-037, K4-038, K4-042 |

## B-01 · Kalibrasyon CONTRACT.md Bölüm 9 ile birebir aynı

| id | Girdi | Alan | CONTRACT.md §9 | G*Power | Fark |
|---|---|---|---|---|---|
| K4-001 | A priori · w=0.3 · α=0.05 · power=0.95 · df=5 | ncp | 19.8000000 | 19.8000000 | 0 |
| | | critical_chi2 | 11.0704977 | 11.0704977 | 0 |
| | | n_total | 220 | 220 | 0 |
| | | actual_power | 0.9502155 | 0.9502155 | 0 |
| K4-002 | Post hoc · w=0.3 · α=0.05 · N=100 · df=5 | ncp | 9.0000000 | 9.0000000 | 0 |
| | | critical_chi2 | 11.0704977 | 11.0704977 | 0 |
| | | power | 0.6235846 | 0.6235846 | 0 |

Ekran görüntüsü: `K4-001.png`, `K4-002.png`. Çelişki: yok.

## B-02 · Hata veren girdiler

Yedi vektörün hepsinde tepki aynı biçimde: "Input error" başlıklı bir diyalog ve tek düğme ("Tamam"). Output Parameters alanlarında "?" görünüyor, dağılım grafiği boş ve protokole kayıt düşmüyor.

> **Kanıt olarak esas alınan: ekran metni.** `K4_gui_results.csv` içindeki `g_tepki` sütunu ekran görüntüsündeki diyalog metnidir. Hata notu metni ham veri olarak yanında duruyor (`K4_hata_notları.txt` değiştirilmedi).

| id | Girdi | Diyalog metni (ekran görüntüsünden) = `g_tepki` | Hata notu metni (ham) | Ekran görüntüsü | CONTRACT.md |
|---|---|---|---|---|---|
| K4-031 | A priori · w=0.3 · α=0.05 · power=**0.03** · df=1 | `Power must be greater than or equal to alpha.` | `Input : power must be greater than or equal to alpha. hesaplamadı.` | K4-031.png | §2.4: örnek hata metni "Power, alpha değerinden büyük olmalı" (kesin büyük); G*Power metni "greater than or equal". Bkz. B-04 (power = α kabul edildi) |
| K4-033 | A priori · w=**0** · α=0.05 · power=0.95 · df=5 | `Effect size w must be greater 1e-06.` | `Input : Effect size w must be greater 1e-06. hesaplamadı.` | K4-033.png | §5 (w > 0) ile uyumlu |
| K4-034 | A priori · w=**−0.3** · α=0.05 · power=0.95 · df=5 | `Effect size w must be greater 1e-06.` | `Input : Effect size w must be greater 1e-06. hesaplamadı.` | K4-034.png | §5 (w > 0) ile uyumlu |
| K4-035 | A priori · w=0.3 · α=0.05 · power=0.95 · df=**0** | `Degrees of Freedom must be greater or equal one.` | `Input : Degrees of Freedom must be grester or equal one` | K4-035.png | §5 (df ≥ 1) ile uyumlu |
| K4-037 | A priori · w=0.3 · α=0.05 · power=**1** · df=5 | `Power is outside the admissible range (1e-07, 1).` | `Input : Power is outside the admissible range (1e-07, 1)` | K4-037.png | §5 (0 < power < 1) ile uyumlu |
| K4-038 | Post hoc · w=0.3 · α=**0** · N=100 · df=5 | `Alpha is outside the admissible range (1e-07, 1).` | `Input : Alpha is outside the admissible range (1e-07, 1)` | K4-038.png | §5 (0 < alpha < 1) ile uyumlu |
| K4-042 | Post hoc · w=**−0.3** · α=0.05 · N=100 · df=1 | `Effect size w must be non-negative.` | `Hata verdi. Input: Effect size w must be non-negative.` | K4-042.png | §5 (w > 0) ile uyumlu; metin a-priori'den farklı (bkz. B-09) |

Notlar:
- **Yeniden çekim:** K4-031, K4-033 ve K4-034 ek turda yeniden çekildi (21:32–21:35). Diyalog kenara kaydırıldığı için bütün girdi alanları okunuyor ve plandaki değerlerle eşleşiyor. Diyalog metni ilk çekimle aynı. İlk çekimler `K4-031_ilk.png`, `K4-033_ilk.png`, `K4-034_ilk.png` adıyla duruyor.
- K4-035, K4-037 ve K4-038 yeniden çekilmedi. Bu üçünde diyalog hâlâ "Effect size w" alanını örtüyor (w=0.3 görüntüden okunamıyor). Sınırdaki değer (df=0, power=1, α=0) ve diğer alanlar görünüyor.
- Hata notlarındaki metinler, diyalog metninden şu yönlerden farklı:
  - "Input :" ön eki ve sonradan eklenmiş "hesaplamadı." gibi açıklamalar var.
  - Bazılarında sondaki nokta yok.
  - K4-031'de "power" küçük harfle yazılmış.
  - K4-035'te "grester" yazılmış; diyalogda "greater".

## B-03 · Ondalık df kabul edildi ve hesaplandı

| id | Girdi | Tepki | Ekran görüntüsü | CONTRACT.md |
|---|---|---|---|---|
| K4-036 | A priori · w=0.3 · α=0.05 · power=0.95 · df=**2.5** | Hata yok. Df alanında ve protokolde `2.5`. Çıktı: ncp=16.3800000 · critical χ²=6.9280761 · N=182 · actual power=0.9502356 | K4-036.png | **Çelişki — §5:** df tam sayı ≥ 1; §2.4: tam sayı yerine ondalık `INVALID_VALUE` |

## B-04 · power = α kabul edildi

| id | Girdi | Tepki | Ekran görüntüsü | CONTRACT.md |
|---|---|---|---|---|
| K4-030 | A priori · w=0.3 · α=0.05 · power=**0.05** · df=1 | Hata yok. ncp=0.0900000 · critical χ²=3.8414588 · N=**1** · actual power=0.0603726 | K4-030.png | **Çelişki — §2.4:** örnek hata "Power, alpha değerinden büyük olmalı" (power = α'yı dışlar). **§5:** çıktı N=1, n_total alt sınırı ≥ 2 |

## B-05 · a-priori çıktısında N < 2

| id | Girdi | Çıktı N | Diğer çıktılar | Ekran görüntüsü | CONTRACT.md |
|---|---|---|---|---|---|
| K4-025 | A priori · w=**5.0** · α=0.05 · power=0.80 · df=1 | **1** | ncp=25.0000000 · critical χ²=3.8414588 · actual power=0.9988173 | K4-025.png | **Çelişki — §5:** n_total ≥ 2 (girdi aralığı; çıktı için ayrı kural yok) |
| K4-030 | (B-04) | **1** | (B-04) | K4-030.png | Aynı |
| K4-024 | A priori · w=**2.0** · α=0.05 · power=0.80 · df=1 | 2 | ncp=8.0000000 · critical χ²=3.8414588 · actual power=0.8074304 | K4-024.png | §5 alt sınırına eşit |

## B-06 · Ondalık gösterim basamağı

| id | Girdi | Gözlem | Ekran görüntüsü | CONTRACT.md |
|---|---|---|---|---|
| K4-027 | Post hoc · w=0.3 · α=0.05 · N=100 · df=**100** | critical χ² hem protokolde hem Output alanında `124.3421` (4 ondalık). Aynı vektörde ncp=`9.0000000` ve power=`0.1582365` 7 ondalık | K4-027.png | **Çelişki — §6:** "G*Power ondalıkları 7 basamakla gösterir" |
| K4-039 | Post hoc · w=**0** · α=0.05 · N=100 · df=1 | ncp hem protokolde (EK[1]) hem Output alanında `0` (ondalıksız). Aynı vektörde critical χ²=`3.8414588` ve power=`0.0500000` 7 ondalık | K4-039.png | **Çelişki — §6:** aynı ifade |

Sonuç veren diğer vektörlerde ncp, critical χ², actual power ve power alanlarının hepsi 7 ondalıkla gösterildi.

## B-07 · Farklı girdiler, aynı çıktılar

| id | Girdi | ncp | critical χ² | N | actual power / power |
|---|---|---|---|---|---|
| K4-005 | A priori · w=0.5 · α=0.05 · power=0.80 · df=1 | 8.0000000 | 3.8414588 | 32 | 0.8074304 |
| K4-014 | Post hoc · w=0.5 · α=0.05 · N=32 · df=1 | 8.0000000 | 3.8414588 | — | 0.8074304 |
| K4-023 | A priori · w=1.0 · α=0.05 · power=0.80 · df=1 | 8.0000000 | 3.8414588 | 8 | 0.8074304 |
| K4-024 | A priori · w=2.0 · α=0.05 · power=0.80 · df=1 | 8.0000000 | 3.8414588 | 2 | 0.8074304 |

Aynı biçimde: K4-003 ile K4-015 (ncp 7.8500000, güç 0.8000569) ve K4-004 ile K4-013 (ncp 7.9200000, güç 0.8035275) aynı çıktıları verdi.
Çelişki: yok.

## B-08 · Sınırdaki diğer girdiler: sonuç üretildi

| id | Girdi | Çıktı | Ekran görüntüsü |
|---|---|---|---|
| K4-021 | A priori · w=**0.01** · α=0.05 · power=0.80 · df=1 | ncp=7.8489000 · critical χ²=3.8414588 · N=78489 · actual power=0.8000020 | K4-021.png |
| K4-022 | Post hoc · w=**0.02** · α=0.05 · N=100 · df=1 | ncp=0.0400000 · critical χ²=3.8414588 · power=0.0545947 | K4-022.png |
| K4-023 | A priori · w=**1.0** · α=0.05 · power=0.80 · df=1 | ncp=8.0000000 · critical χ²=3.8414588 · N=8 · actual power=0.8074304 | K4-023.png |
| K4-026 | A priori · w=0.3 · α=0.05 · power=0.80 · df=**50** | ncp=30.2400000 · critical χ²=67.5048065 · N=336 · actual power=0.8006734 | K4-026.png |
| K4-028 | A priori · w=0.3 · α=0.05 · power=**0.99** · df=1 | ncp=18.4500000 · critical χ²=3.8414588 · N=205 · actual power=0.9902383 | K4-028.png |
| K4-029 | A priori · w=0.3 · α=**0.001** · power=0.80 · df=1 | ncp=17.1000000 · critical χ²=10.8275662 · N=190 · actual power=0.8008574 | K4-029.png |
| K4-032 | Post hoc · w=0.3 · α=0.05 · N=**2** · df=1 | ncp=0.1800000 · critical χ²=3.8414588 · power=0.0708635 | K4-032.png |

Çelişki: yok. Tipik vektörlerin (K4-003 … K4-020) tam sonuçları `K4_gui_results.csv` içinde.

## B-09 · w=0 ve w<0: tepki moda göre değişiyor

| id | Girdi | Tepki | Protokol | Ekran görüntüsü |
|---|---|---|---|---|
| K4-033 | **A priori** · w=**0** · α=0.05 · power=0.95 · df=5 | Hata: `Effect size w must be greater 1e-06.` | kayıt yok | K4-033.png |
| K4-039 | **Post hoc** · w=**0** · α=0.05 · N=100 · df=1 | Hata yok. w alanı 0 olarak kaldı. ncp=`0` · critical χ²=3.8414588 · power=0.0500000 | EK[1] | K4-039.png |
| K4-034 | **A priori** · w=**−0.3** · α=0.05 · power=0.95 · df=5 | Hata: `Effect size w must be greater 1e-06.` | kayıt yok | K4-034.png |
| K4-042 | **Post hoc** · w=**−0.3** · α=0.05 · N=100 · df=1 | Hata: `Effect size w must be non-negative.` | kayıt yok | K4-042.png |

Gözlenenler:
- w=0 a-priori modunda reddedildi, post-hoc modunda kabul edildi.
- w<0 iki modda da reddedildi, ama hata metinleri farklı.
- K4-039'da gösterilen güç (0.0500000), girilen α ile aynı.

CONTRACT.md ile ilişkisi:
- **Çelişki — §5:** w > 0. K4-039 sözleşmeye göre `OUT_OF_RANGE` olmalı, G*Power ise sonuç üretiyor.
- **§2.1:** Sözleşme modlar arasında farklı bir aralık tanımlamıyor; G*Power'ın kabul ettiği aralık ise moda göre değişiyor.

## B-10 · Post-hoc'ta N=1 kabul edildi

| id | Girdi | Tepki | Protokol | Ekran görüntüsü | CONTRACT.md |
|---|---|---|---|---|---|
| K4-040 | Post hoc · w=0.3 · α=0.05 · N=**1** · df=1 | Hata yok. Total sample size alanı 1 olarak kaldı. ncp=0.0900000 · critical χ²=3.8414588 · power=0.0603726 | EK[2] | K4-040.png | **Çelişki — §5:** n_total ≥ 2; sözleşmeye göre `OUT_OF_RANGE` |

Bu çıktılar, a-priori modunda N=1 sonucunu veren K4-030'un (B-04) ncp ve güç değerleriyle aynı: 0.0900000 ve 0.0603726.

## B-11 · Post-hoc'ta ondalık N: alanda gösterilen ile hesapta kullanılan farklı

| id | Girilen N | Alanda ve protokol girdisinde görünen N | Protokol çıktısı λ | λ / w² (w=0.3, w²=0.09) | Protokol | Ekran görüntüsü |
|---|---|---|---|---|---|---|
| K4-043 | 50.2 | `50.2` | 4.5000000 | **50** | EK[4] | K4-043.png |
| K4-041 | 50.5 | `50.5` | 4.5900000 | **51** | EK[3] | K4-041.png |

Diğer güç çıktıları: K4-043 için 0.5641160, K4-041 için 0.5724114. Hata ya da uyarı verilmedi.

Ondalık olmayan N girilen bütün post-hoc vektörlerde λ / w², girilen N'ye birebir eşit (`K4_gui_results.csv`, `n_kullanilan` sütunu boş). Tek istisna K4-039: w=0 olduğu için λ / w² hesaplanamıyor.

Gözlenenler:
- 50.2 → 50 sonucu, yukarı yuvarlamayla (tavan, ceil) uyumsuz.
- 50.5 → 51 sonucu, yarıyı çifte yuvarlamayla (round-half-to-even; Python `round(50.5)` → 50) uyumsuz.
- İki gözlem de "en yakın tam sayıya, tam yarıda yukarı" ile uyumlu.
- Gözlemlerin hepsi N > 0 için. Negatif ya da başka yarım değerler (ör. 49.5) denenmedi.

CONTRACT.md ile ilişkisi:
- **Çelişki — §5:** n_total tam sayı ≥ 2.
- **Çelişki — §2.4:** Tam sayı yerine ondalık girilmesi `INVALID_VALUE` olmalı. G*Power ise girdiyi hata vermeden kabul ediyor ve hesapta farklı bir N kullanıyor.
