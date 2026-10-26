# K4 Elle Giriş Listesi — chi2-contingency

**G*Power 3.1.9.7:** Test family = **χ² tests** · Statistical test = **Goodness-of-fit tests: Contingency tables**
**Mod:** Type of power analysis = **A priori: Compute required sample size** ya da **Post hoc: Compute achieved power**

Her satırda: değerleri gir → *Calculate* → sonuçları `K4_gui_results.csv`'ye yaz → ekran görüntüsünü `oracle/screenshots/<id>.png` olarak kaydet.
Hata çıkarsa mesajı **birebir** `g_tepki` sütununa yaz; alan değeri kabul etmiyorsa bunu da not et.

Toplam: **43 vektör**. Sınır satırlarının tabanı: a-priori w=0.3 · α=0.05 · power=0.80 · Df=1; post-hoc w=0.3 · α=0.05 · N=100 · Df=1.

## A. Kalibrasyon (2) — önce bunlar; tutmazsa DUR

| id | Mod | Girilecek değerler | Beklenen | ☐ |
|---|---|---|---|---|
| K4-001 | A priori | Effect size w = 0.3 · α err prob = 0.05 · Power (1-β err prob) = 0.95 · Df = 5 | Noncentrality parameter λ = 19.8000000 · Critical χ² = 11.0704977 · Total sample size = 220 · Actual power = 0.9502155 | ☐ |
| K4-002 | Post hoc | Effect size w = 0.3 · α err prob = 0.05 · Total sample size = 100 · Df = 5 | Noncentrality parameter λ = 9.0000000 · Critical χ² = 11.0704977 · Power (1-β err prob) = 0.6235846 | ☐ |

## B. Tipik a-priori (10)

| id | Mod | Girilecek değerler | Beklenen | ☐ |
|---|---|---|---|---|
| K4-003 | A priori | Effect size w = 0.1 · α err prob = 0.05 · Power (1-β err prob) = 0.80 · Df = 1 | — | ☐ |
| K4-004 | A priori | Effect size w = 0.3 · α err prob = 0.05 · Power (1-β err prob) = 0.80 · Df = 1 | — | ☐ |
| K4-005 | A priori | Effect size w = 0.5 · α err prob = 0.05 · Power (1-β err prob) = 0.80 · Df = 1 | — | ☐ |
| K4-006 | A priori | Effect size w = 0.3 · α err prob = 0.01 · Power (1-β err prob) = 0.90 · Df = 2 | — | ☐ |
| K4-007 | A priori | Effect size w = 0.1 · α err prob = 0.05 · Power (1-β err prob) = 0.95 · Df = 3 | — | ☐ |
| K4-008 | A priori | Effect size w = 0.5 · α err prob = 0.10 · Power (1-β err prob) = 0.90 · Df = 4 | — | ☐ |
| K4-009 | A priori | Effect size w = 0.3 · α err prob = 0.10 · Power (1-β err prob) = 0.80 · Df = 6 | — | ☐ |
| K4-010 | A priori | Effect size w = 0.1 · α err prob = 0.01 · Power (1-β err prob) = 0.80 · Df = 10 | — | ☐ |
| K4-011 | A priori | Effect size w = 0.5 · α err prob = 0.01 · Power (1-β err prob) = 0.95 · Df = 10 | — | ☐ |
| K4-012 | A priori | Effect size w = 0.3 · α err prob = 0.05 · Power (1-β err prob) = 0.90 · Df = 3 | — | ☐ |

## C. Tipik post-hoc (8)

| id | Mod | Girilecek değerler | Beklenen | ☐ |
|---|---|---|---|---|
| K4-013 | Post hoc | Effect size w = 0.3 · α err prob = 0.05 · Total sample size = 88 · Df = 1 | — | ☐ |
| K4-014 | Post hoc | Effect size w = 0.5 · α err prob = 0.05 · Total sample size = 32 · Df = 1 | — | ☐ |
| K4-015 | Post hoc | Effect size w = 0.1 · α err prob = 0.05 · Total sample size = 785 · Df = 1 | — | ☐ |
| K4-016 | Post hoc | Effect size w = 0.1 · α err prob = 0.01 · Total sample size = 1000 · Df = 10 | — | ☐ |
| K4-017 | Post hoc | Effect size w = 0.5 · α err prob = 0.10 · Total sample size = 20 · Df = 4 | — | ☐ |
| K4-018 | Post hoc | Effect size w = 0.3 · α err prob = 0.01 · Total sample size = 150 · Df = 2 | — | ☐ |
| K4-019 | Post hoc | Effect size w = 0.5 · α err prob = 0.05 · Total sample size = 50 · Df = 6 | — | ☐ |
| K4-020 | Post hoc | Effect size w = 0.3 · α err prob = 0.10 · Total sample size = 300 · Df = 3 | — | ☐ |

## D. Sınır değerler (12) — tabandan yalnızca **kalın** değer farklı

| id | Mod | Girilecek değerler | Beklenen | ☐ |
|---|---|---|---|---|
| K4-021 | A priori | Effect size w = **0.01** · α err prob = 0.05 · Power (1-β err prob) = 0.80 · Df = 1 | — | ☐ |
| K4-022 | Post hoc | Effect size w = **0.02** · α err prob = 0.05 · Total sample size = 100 · Df = 1 | — | ☐ |
| K4-023 | A priori | Effect size w = **1.0** · α err prob = 0.05 · Power (1-β err prob) = 0.80 · Df = 1 | — | ☐ |
| K4-024 | A priori | Effect size w = **2.0** · α err prob = 0.05 · Power (1-β err prob) = 0.80 · Df = 1 | — | ☐ |
| K4-025 | A priori | Effect size w = **5.0** · α err prob = 0.05 · Power (1-β err prob) = 0.80 · Df = 1 | — | ☐ |
| K4-026 | A priori | Effect size w = 0.3 · α err prob = 0.05 · Power (1-β err prob) = 0.80 · Df = **50** | — | ☐ |
| K4-027 | Post hoc | Effect size w = 0.3 · α err prob = 0.05 · Total sample size = 100 · Df = **100** | — | ☐ |
| K4-028 | A priori | Effect size w = 0.3 · α err prob = 0.05 · Power (1-β err prob) = **0.99** · Df = 1 | — | ☐ |
| K4-029 | A priori | Effect size w = 0.3 · α err prob = **0.001** · Power (1-β err prob) = 0.80 · Df = 1 | — | ☐ |
| K4-030 | A priori | Effect size w = 0.3 · α err prob = 0.05 · Power (1-β err prob) = **0.05** · Df = 1 | — | ☐ |
| K4-031 | A priori | Effect size w = 0.3 · α err prob = 0.05 · Power (1-β err prob) = **0.03** · Df = 1 | — | ☐ |
| K4-032 | Post hoc | Effect size w = 0.3 · α err prob = 0.05 · Total sample size = **2** · Df = 1 | — | ☐ |

## E. Geçersiz girdiler (6) — tepkiyi birebir yaz

| id | Mod | Girilecek değerler | Beklenen | ☐ |
|---|---|---|---|---|
| K4-033 | A priori | Effect size w = 0 · α err prob = 0.05 · Power (1-β err prob) = 0.95 · Df = 5 | — | ☐ |
| K4-034 | A priori | Effect size w = -0.3 · α err prob = 0.05 · Power (1-β err prob) = 0.95 · Df = 5 | — | ☐ |
| K4-035 | A priori | Effect size w = 0.3 · α err prob = 0.05 · Power (1-β err prob) = 0.95 · Df = 0 | — | ☐ |
| K4-036 | A priori | Effect size w = 0.3 · α err prob = 0.05 · Power (1-β err prob) = 0.95 · Df = 2.5 | — | ☐ |
| K4-037 | A priori | Effect size w = 0.3 · α err prob = 0.05 · Power (1-β err prob) = 1 · Df = 5 | — | ☐ |
| K4-038 | Post hoc | Effect size w = 0.3 · α err prob = 0 · Total sample size = 100 · Df = 5 | — | ☐ |

## F. Geçersiz girdiler — mod tutarlılığı (5) — tepkiyi birebir yaz

| id | Mod | Girilecek değerler | Beklenen | ☐ |
|---|---|---|---|---|
| K4-039 | Post hoc | Effect size w = 0 · α err prob = 0.05 · Total sample size = 100 · Df = 1 | — | ☐ |
| K4-040 | Post hoc | Effect size w = 0.3 · α err prob = 0.05 · Total sample size = 1 · Df = 1 | — | ☐ |
| K4-041 | Post hoc | Effect size w = 0.3 · α err prob = 0.05 · Total sample size = 50.5 · Df = 1 | — | ☐ |
| K4-042 | Post hoc | Effect size w = -0.3 · α err prob = 0.05 · Total sample size = 100 · Df = 1 | — | ☐ |
| K4-043 | Post hoc | Effect size w = 0.3 · α err prob = 0.05 · Total sample size = 50.2 · Df = 1 | — | ☐ |

## Yeniden çekilecekler

Hata diyaloğunu girdi alanlarını örtmeyecek bir yere sürükleyip ekran görüntüsünü yeniden al; dosyayı aynı adla `oracle/screenshots/<id>.png` üzerine kaydet.

| id | Mod | Girilecek değerler | Neden | ☐ |
|---|---|---|---|---|
| K4-031 | A priori | Effect size w = 0.3 · α err prob = 0.05 · Power (1-β err prob) = **0.03** · Df = 1 | diyalog w ve α alanlarını örtüyor | ☐ |
| K4-033 | A priori | Effect size w = 0 · α err prob = 0.05 · Power (1-β err prob) = 0.95 · Df = 5 | diyalog w alanını örtüyor (K4-034'ten ayırt edilemiyor) | ☐ |
| K4-034 | A priori | Effect size w = -0.3 · α err prob = 0.05 · Power (1-β err prob) = 0.95 · Df = 5 | diyalog w alanını örtüyor (K4-033'ten ayırt edilemiyor) | ☐ |
