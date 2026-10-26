"""K4_gui_protokol*.txt kayıtlarını GİRDİLERİNE göre K4 vektörleriyle eşleştirir ve K4_gui_results.csv'yi doldurur.
Hiçbir güç hesabı yapmaz: sayılar protokol metninden birebir kopyalanır; hata metinleri ekran görüntülerinden alınmış SCREEN_TEXT'tir.
Post-hoc'ta λ / w² girilen N'den farklıysa n_kullanilan'a yazılır. Kayıt ya da ekran metni olmayan satırlara dokunmaz."""
import csv
import glob
import os
import re
import sys
from decimal import Decimal

sys.stdout.reconfigure(encoding="utf-8")
d = os.path.dirname(os.path.abspath(__file__))

# Hata diyaloğu metinleri, ekran görüntülerinden birebir (kanıt olarak esas alınan: ekran metni)
SCREEN_TEXT = {
    "K4-031": "Power must be greater than or equal to alpha.",
    "K4-033": "Effect size w must be greater 1e-06.",
    "K4-034": "Effect size w must be greater 1e-06.",
    "K4-035": "Degrees of Freedom must be greater or equal one.",
    "K4-037": "Power is outside the admissible range (1e-07, 1).",
    "K4-038": "Alpha is outside the admissible range (1e-07, 1).",
    "K4-042": "Effect size w must be non-negative.",
}

MODE = {"A priori": "a-priori", "Post hoc": "post-hoc"}
records = []
for path in sorted(glob.glob(os.path.join(d, "K4_gui_protokol*.txt"))):
    tag = re.match(r"K4_gui_protokol_?(.*)\.txt", os.path.basename(path)).group(1)
    text = open(path, encoding="utf-8").read()
    for block in re.split(r"\n(?=\[\d+\] -- )", text.strip()):
        head = re.match(r"\[(\d+)\] -- (.*)", block)
        mode = re.search(r"Analysis:\s*(A priori|Post hoc)", block).group(1)
        fields = dict(re.findall(r"^\s*(?:Input:|Output:)?\s*([^\t=\n][^\t=\n]*?)\s*\t=\t(\S+)\s*$", block, re.M))
        records.append({"ref": f"{tag}[{head.group(1)}]", "ts": head.group(2).strip(),
                        "mode": MODE[mode], "f": fields})

def key_plan(r):
    second = r["power"] if r["mode"] == "a-priori" else r["n_total"]
    return (r["mode"], float(r["w"]), float(r["alpha"]), float(second), float(r["df"]))

def key_rec(rec):
    f = rec["f"]
    second = f["Power (1-β err prob)"] if rec["mode"] == "a-priori" else f["Total sample size"]
    return (rec["mode"], float(f["Effect size w"]), float(f["α err prob"]), float(second), float(f["Df"]))

def n_used(f):
    """Post-hoc: λ / w², protokol metninden tam ondalıkla; girilen N'den farklıysa döndürür."""
    w = Decimal(f["Effect size w"])
    if w == 0:
        return ""
    n = (Decimal(f["Noncentrality parameter λ"]) / (w * w)).normalize()
    return "" if n == Decimal(f["Total sample size"]) else format(n, "f")

path = os.path.join(d, "K4_gui_results.csv")
with open(path, encoding="utf-8", newline="") as fh:
    reader = csv.DictReader(fh)
    header = list(reader.fieldnames)
    rows = list(reader)
if "n_kullanilan" not in header:
    header.insert(header.index("g_power") + 1, "n_kullanilan")
    for r in rows:
        r["n_kullanilan"] = ""

by_key = {}
for rec in records:
    by_key.setdefault(key_rec(rec), []).append(rec)

used, matched, multi, errors = set(), {}, [], []
for r in rows:
    hits = by_key.get(key_plan(r), [])
    if len(hits) > 1:
        multi.append((r["id"], [h["ref"] for h in hits]))
    if hits:
        rec = hits[0]
        used.add(rec["ref"])
        f = rec["f"]
        r["g_ncp"] = f["Noncentrality parameter λ"]
        r["g_critical_chi2"] = f["Critical χ²"]
        if r["mode"] == "a-priori":
            r["g_n_total"] = f["Total sample size"]
            r["g_actual_power"] = f["Actual power"]
        else:
            r["g_power"] = f["Power (1-β err prob)"]
            r["n_kullanilan"] = n_used(f)
        r["g_tepki"] = "ok (sözleşmeye göre geçersiz)" if r["kategori"].startswith("gecersiz") else "ok"
        r["screenshot"] = f"{r['id']}.png"
        matched[r["id"]] = rec["ref"]
    elif r["id"] in SCREEN_TEXT:
        r["g_tepki"] = SCREEN_TEXT[r["id"]]
        r["screenshot"] = f"{r['id']}.png"
        errors.append(r["id"])

with open(path, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=header, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

untouched = [r["id"] for r in rows if r["id"] not in matched and r["id"] not in errors]
print("protokol kaydı:", len(records), "| eşleşen:", len(matched), "| ekran metniyle hata:", len(errors))
print("eşleşmeler:", ", ".join(f"{k}={v}" for k, v in matched.items()))
print("çoklu eşleşme:", multi or "yok")
print("dokunulmayan (kayıt/ekran metni yok):", untouched or "yok")
print("n_kullanilan dolu:", [(r["id"], r["n_total"], r["n_kullanilan"]) for r in rows if r["n_kullanilan"]] or "yok")
for rec in records:
    if rec["ref"] not in used:
        print(f"eşleşmeyen kayıt {rec['ref']} {rec['ts']} {rec['mode']} {rec['f']}")
