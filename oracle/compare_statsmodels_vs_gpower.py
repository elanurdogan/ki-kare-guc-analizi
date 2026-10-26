"""K4_gui_results.csv'de g_tepki == "ok" olan G*Power GUI vektörlerinin aynı girdilerini statsmodels GofChisquarePower'a verir.
a-priori'de G*Power N'yi statsmodels kesirli N ve ceil'i ile, post-hoc'ta güçleri karşılaştırır; STATSMODELS_KARSILASTIRMA.md'ye yazar.
Yalnızca gözlem raporlar; yorum yapmaz. Kullanım: .venv/Scripts/python oracle/compare_statsmodels_vs_gpower.py"""
import csv
import math
import os
import sys
import warnings

import statsmodels
from statsmodels.stats.power import GofChisquarePower

sys.stdout.reconfigure(encoding="utf-8")
d = os.path.dirname(os.path.abspath(__file__))
gof = GofChisquarePower()

with open(os.path.join(d, "K4_gui_results.csv"), encoding="utf-8", newline="") as f:
    rows = [r for r in csv.DictReader(f) if r["g_tepki"] == "ok"]

def sm(fn, **kw):
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            value = float(fn(**kw))
        except Exception as exc:
            return None, "hata: " + " ".join(str(exc).split())
    note = ("uyarı: " + "; ".join(" ".join(str(c.message).split()) for c in caught)) if caught else ""
    if not math.isfinite(value):
        return None, f"sonuç {value}" + (f"; {note}" if note else "")
    return value, note

ap, ph = [], []
for r in rows:
    w, alpha, df = float(r["w"]), float(r["alpha"]), int(r["df"])
    if r["mode"] == "a-priori":
        n, note = sm(gof.solve_power, effect_size=w, nobs=None, alpha=alpha, power=float(r["power"]), n_bins=df + 1)
        c = math.ceil(n) if n is not None else None
        ap.append({"r": r, "n": n, "ceil": c, "eq": (c == int(r["g_n_total"])) if c is not None else None, "note": note})
    else:
        p, note = sm(gof.power, effect_size=w, nobs=int(r["n_total"]), alpha=alpha, n_bins=df + 1)
        ph.append({"r": r, "p": p, "diff": abs(p - float(r["g_power"])) if p is not None else None, "note": note})

def cell(text):
    return text.replace("|", "\\|")

def yn(v):
    return "—" if v is None else ("evet" if v else "**hayır**")

md = [
    "# statsmodels ↔ G*Power karşılaştırması (K4)",
    "",
    f"> İkincil kâhin: statsmodels {statsmodels.__version__} `GofChisquarePower` (`n_bins = df + 1`). Birincil kâhin: G*Power 3.1.9.7 GUI (`K4_gui_results.csv`).",
    "> Kapsam: `g_tepki` değeri tam olarak `ok` olan vektörler. Hata verenler ve \"ok (sözleşmeye göre geçersiz)\" olanlar dahil değil.",
    "> G*Power değerleri protokoldeki 7 ondalıklı metinden; statsmodels değerleri tam double.",
    "",
    f"## a-priori ({len(ap)} vektör)",
    "",
    "| id | w | α | power | df | G*Power N | statsmodels kesirli N | ceil(kesirli N) | G*Power N == ceil? | not |",
    "|---|---|---|---|---|---|---|---|---|---|",
]
for x in ap:
    r = x["r"]
    md.append(f"| {r['id']} | {r['w']} | {r['alpha']} | {r['power']} | {r['df']} | {r['g_n_total']} | "
              f"{'—' if x['n'] is None else repr(x['n'])} | {'—' if x['ceil'] is None else x['ceil']} | {yn(x['eq'])} | {cell(x['note'])} |")
md += [
    "",
    f"## post-hoc ({len(ph)} vektör)",
    "",
    "| id | w | α | n_total | df | G*Power güç | statsmodels güç | \\|fark\\| | not |",
    "|---|---|---|---|---|---|---|---|---|",
]
for x in ph:
    r = x["r"]
    p = "—" if x["p"] is None else repr(x["p"])
    diff = "—" if x["diff"] is None else f"{x['diff']:.3e}"
    md.append(f"| {r['id']} | {r['w']} | {r['alpha']} | {r['n_total']} | {r['df']} | {r['g_power']} | {p} | {diff} | {cell(x['note'])} |")

eq = [x for x in ap if x["eq"]]
neq = [x for x in ap if x["eq"] is False]
fail_ap = [x for x in ap if x["n"] is None]
diffs = [x for x in ph if x["diff"] is not None]
mx = max(diffs, key=lambda x: x["diff"]) if diffs else None
warned = [x["r"]["id"] for x in ap + ph if x["note"]]
neq_text = ", ".join(f"{x['r']['id']} (G*Power {x['r']['g_n_total']}, ceil {x['ceil']}, kesirli {x['n']!r})" for x in neq)
md += [
    "",
    "## Gözlem özeti",
    "",
    f"- a-priori: {len(ap)} vektörün {len(eq)} tanesinde G*Power N == ceil(statsmodels kesirli N).",
    f"- Tutmayan: {neq_text or 'yok'}.",
    f"- statsmodels'in sonuç vermediği a-priori vektör: {', '.join(x['r']['id'] for x in fail_ap) if fail_ap else 'yok'}.",
    f"- post-hoc: {len(ph)} vektörde en büyük |G*Power güç − statsmodels güç| = {mx['diff']:.3e} ({mx['r']['id']})." if mx else "- post-hoc: karşılaştırılabilir vektör yok.",
    f"- statsmodels uyarı/hata veren vektör: {', '.join(warned) if warned else 'yok'}.",
    "",
]
with open(os.path.join(d, "STATSMODELS_KARSILASTIRMA.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(md))
print("\n".join(md[-7:]))
