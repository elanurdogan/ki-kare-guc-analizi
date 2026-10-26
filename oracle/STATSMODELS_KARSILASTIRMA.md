# statsmodels ↔ G*Power karşılaştırması (K4)

> İkincil kâhin: statsmodels 0.15.0 `GofChisquarePower` (`n_bins = df + 1`). Birincil kâhin: G*Power 3.1.9.7 GUI (`K4_gui_results.csv`).
> Kapsam: `g_tepki` değeri tam olarak `ok` olan vektörler. Hata verenler ve "ok (sözleşmeye göre geçersiz)" olanlar dahil değil.
> G*Power değerleri protokoldeki 7 ondalıklı metinden; statsmodels değerleri tam double.

## a-priori (19 vektör)

| id | w | α | power | df | G*Power N | statsmodels kesirli N | ceil(kesirli N) | G*Power N == ceil? | not |
|---|---|---|---|---|---|---|---|---|---|
| K4-001 | 0.3 | 0.05 | 0.95 | 5 | 220 | 219.7792708260668 | 220 | evet |  |
| K4-003 | 0.1 | 0.05 | 0.80 | 1 | 785 | 784.8860506688932 | 785 | evet |  |
| K4-004 | 0.3 | 0.05 | 0.80 | 1 | 88 | 87.20956138148837 | 88 | evet |  |
| K4-005 | 0.5 | 0.05 | 0.80 | 1 | 32 | 31.395442038122646 | 32 | evet |  |
| K4-006 | 0.3 | 0.01 | 0.90 | 2 | 194 | 193.62987852885158 | 194 | evet |  |
| K4-007 | 0.1 | 0.05 | 0.95 | 3 | 1717 | 1716.9897871472226 | 1717 | evet |  |
| K4-008 | 0.5 | 0.10 | 0.90 | 4 | 52 | 51.53085840596239 | 52 | evet |  |
| K4-009 | 0.3 | 0.10 | 0.80 | 6 | 124 | 123.65259865177195 | 124 | evet |  |
| K4-010 | 0.1 | 0.01 | 0.80 | 10 | 2218 | 2217.6553761209893 | 2218 | evet |  |
| K4-011 | 0.5 | 0.01 | 0.95 | 10 | 126 | 125.03050234159957 | 126 | evet |  |
| K4-012 | 0.3 | 0.05 | 0.90 | 3 | 158 | 157.46097012651202 | 158 | evet |  |
| K4-021 | 0.01 | 0.05 | 0.80 | 1 | 78489 | 78488.60509326236 | 78489 | evet |  |
| K4-023 | 1.0 | 0.05 | 0.80 | 1 | 8 | 7.8488605099785875 | 8 | evet |  |
| K4-024 | 2.0 | 0.05 | 0.80 | 1 | 2 | — | — | — | sonuç nan; uyarı: Failed to converge on a solution. The last value evaluated by the root finder was [10.]; returning nan instead. Solver details are stored in the ``cache_fit_res`` attribute. |
| K4-025 | 5.0 | 0.05 | 0.80 | 1 | 1 | — | — | — | sonuç nan; uyarı: Failed to converge on a solution. The last value evaluated by the root finder was [10.]; returning nan instead. Solver details are stored in the ``cache_fit_res`` attribute. |
| K4-026 | 0.3 | 0.05 | 0.80 | 50 | 336 | 335.59589077997 | 336 | evet |  |
| K4-028 | 0.3 | 0.05 | 0.99 | 1 | 205 | 204.1385479524987 | 205 | evet |  |
| K4-029 | 0.3 | 0.001 | 0.80 | 1 | 190 | 189.71829783446674 | 190 | evet |  |
| K4-030 | 0.3 | 0.05 | 0.05 | 1 | 1 | — | — | — | hata: only 0-dimensional arrays can be converted to Python scalars |

## post-hoc (12 vektör)

| id | w | α | n_total | df | G*Power güç | statsmodels güç | \|fark\| | not |
|---|---|---|---|---|---|---|---|---|
| K4-002 | 0.3 | 0.05 | 100 | 5 | 0.6235846 | 0.6235846116825697 | 1.168e-08 |  |
| K4-013 | 0.3 | 0.05 | 88 | 1 | 0.8035275 | 0.8035274844561174 | 1.554e-08 |  |
| K4-014 | 0.5 | 0.05 | 32 | 1 | 0.8074304 | 0.8074304194325567 | 1.943e-08 |  |
| K4-015 | 0.1 | 0.05 | 785 | 1 | 0.8000569 | 0.8000569268798245 | 2.688e-08 |  |
| K4-016 | 0.1 | 0.01 | 1000 | 10 | 0.3055578 | 0.30555784280491083 | 4.280e-08 |  |
| K4-017 | 0.5 | 0.10 | 20 | 4 | 0.5241841 | 0.5241841305687391 | 3.057e-08 |  |
| K4-018 | 0.3 | 0.01 | 150 | 2 | 0.7856135 | 0.7856134858771081 | 1.412e-08 |  |
| K4-019 | 0.5 | 0.05 | 50 | 6 | 0.7584630 | 0.758462978844812 | 2.116e-08 |  |
| K4-020 | 0.3 | 0.10 | 300 | 3 | 0.9985178 | 0.9985177520326477 | 4.797e-08 |  |
| K4-022 | 0.02 | 0.05 | 100 | 1 | 0.0545947 | 0.05459468552727531 | 1.447e-08 |  |
| K4-027 | 0.3 | 0.05 | 100 | 100 | 0.1582365 | 0.1582364703355915 | 2.966e-08 |  |
| K4-032 | 0.3 | 0.05 | 2 | 1 | 0.0708635 | 0.07086349410120675 | 5.899e-09 |  |

## Gözlem özeti

- a-priori: 19 vektörün 16 tanesinde G*Power N == ceil(statsmodels kesirli N).
- Tutmayan: yok.
- statsmodels'in sonuç vermediği a-priori vektör: K4-024, K4-025, K4-030.
- post-hoc: 12 vektörde en büyük |G*Power güç − statsmodels güç| = 4.797e-08 (K4-020).
- statsmodels uyarı/hata veren vektör: K4-024, K4-025, K4-030.
