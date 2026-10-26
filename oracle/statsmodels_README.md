# İKİNCİL KÂHİN: G*Power değildir

> `statsmodels_vectors.csv` içindeki değerler **G*Power 3.1.9.7'den alınmamıştır.** Açık kaynak `statsmodels` kütüphanesinin `GofChisquarePower` sınıfıyla üretilmiştir.
> Birincil kâhin (sözleşmenin ve değerlendirme düzeneğinin esas aldığı referans) her zaman G*Power'dır: `K4_gui_results.csv` ve `public_vectors.jsonl`.
> Bu dosya yalnızca G*Power'da elle denenemeyecek kadar geniş bir ızgarada ikinci bir referans sağlar.

## Üretim

| | |
|---|---|
| Betik | `oracle/make_statsmodels_vectors.py` |
| Ortam | Python 3.13.14 · statsmodels 0.15.0 · scipy 1.18.1 · numpy 2.5.4 (repo içi `.venv`) |
| Sınıf | `statsmodels.stats.power.GofChisquarePower` |
| df eşlemesi | statsmodels `n_bins` parametresini alır: **`n_bins = df + 1`** |
| Hassasiyet | Sonuçlar `repr(float)` ile tam double olarak yazılır, yuvarlanmaz |

Yeniden üretmek için:

```
.venv/Scripts/python oracle/make_statsmodels_vectors.py
```

## Izgara (1920 vektör)

| Mod | Değişkenler | Çıktı sütunu | Sayı |
|---|---|---|---|
| a-priori | w ∈ {0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.7, 1.0} × df ∈ {1, 2, 3, 4, 5, 6, 8, 10} × α ∈ {0.01, 0.05, 0.10} × power ∈ {0.80, 0.90, 0.95} | `sm_n_fractional`: `solve_power` ile bulunan kesirli N, yuvarlanmamış | 720 |
| post-hoc | aynı w × df × α × n_total ∈ {20, 50, 100, 200, 500} | `sm_power`: `power` | 1200 |

## Sütunlar

`id` (SM-0001 …), `kaynak` ("statsmodels <sürüm>"), `mode`, `w`, `alpha`, `power`, `n_total`, `df`, `sm_n_fractional`, `sm_power`.

## G*Power ile ilişkisi

G*Power GUI vektörleriyle karşılaştırma için bkz. `STATSMODELS_KARSILASTIRMA.md` (`compare_statsmodels_vs_gpower.py`).
