"""İkincil kâhin: statsmodels GofChisquarePower ile χ² uyum iyiliği güç vektörleri üretir (G*Power DEĞİLDİR).
a-priori ızgarada kesirli N'yi, post-hoc ızgarada gücü oracle/statsmodels_vectors.csv'ye tam double hassasiyetle yazar.
statsmodels'te df = n_bins - 1. Kullanım: .venv/Scripts/python oracle/make_statsmodels_vectors.py"""
import csv
import itertools
import os
import sys
import warnings

import statsmodels
from statsmodels.stats.power import GofChisquarePower

sys.stdout.reconfigure(encoding="utf-8")
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "statsmodels_vectors.csv")
KAYNAK = f"statsmodels {statsmodels.__version__}"

W = ["0.05", "0.1", "0.15", "0.2", "0.25", "0.3", "0.4", "0.5", "0.7", "1.0"]
DF = ["1", "2", "3", "4", "5", "6", "8", "10"]
ALPHA = ["0.01", "0.05", "0.10"]
POWER = ["0.80", "0.90", "0.95"]
N_TOTAL = ["20", "50", "100", "200", "500"]

cols = ["id", "kaynak", "mode", "w", "alpha", "power", "n_total", "df", "sm_n_fractional", "sm_power"]
gof = GofChisquarePower()
rows, problems = [], []

def call(fn, **kw):
    """statsmodels çağrısı; uyarı ya da hata olursa kaydeder, sonucu repr ile (tam double) döndürür."""
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            value = fn(**kw)
        except Exception as exc:
            problems.append((kw, f"hata: {exc}"))
            return ""
    if caught:
        problems.append((kw, "uyarı: " + "; ".join(str(c.message) for c in caught)))
    return repr(float(value))

for w, df, alpha, power in itertools.product(W, DF, ALPHA, POWER):
    n = call(gof.solve_power, effect_size=float(w), nobs=None, alpha=float(alpha), power=float(power), n_bins=int(df) + 1)
    rows.append({"mode": "a-priori", "w": w, "alpha": alpha, "power": power, "n_total": "", "df": df,
                 "sm_n_fractional": n, "sm_power": ""})

for w, df, alpha, n_total in itertools.product(W, DF, ALPHA, N_TOTAL):
    p = call(gof.power, effect_size=float(w), nobs=int(n_total), alpha=float(alpha), n_bins=int(df) + 1)
    rows.append({"mode": "post-hoc", "w": w, "alpha": alpha, "power": "", "n_total": n_total, "df": df,
                 "sm_n_fractional": "", "sm_power": p})

for i, r in enumerate(rows, 1):
    r["id"] = f"SM-{i:04d}"
    r["kaynak"] = KAYNAK

with open(out, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)

n_ap = sum(r["mode"] == "a-priori" for r in rows)
print(f"{KAYNAK} | vektör: {len(rows)} (a-priori {n_ap}, post-hoc {len(rows) - n_ap})")
print("boş sonuç:", sum(1 for r in rows if not (r["sm_n_fractional"] or r["sm_power"])))
print("uyarı/hata:", len(problems))
for kw, msg in problems[:20]:
    print("  ", kw, msg)
