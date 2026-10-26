"""K4 (chi2-contingency) kâhin planını üretir: K4_plan.csv, K4_gui_results.csv ve K4_GIRIS_LISTESI.md.
Hiçbir güç hesabı yapmaz; yalnızca G*Power 3.1.9.7 arayüzüne elle girilecek değerleri tek kaynaktan listeler.
Kullanım: python oracle/make_k4_plan.py  (dosyalar bu betiğin yanına yazılır; K4_gui_results.csv varsa korunur)."""
import collections
import csv
import os

out = os.path.dirname(os.path.abspath(__file__))
A, P = "a-priori", "post-hoc"
COHEN_N = "N, Cohen tablolarındaki yaklaşık değerden seçildi"
TABAN_A = "taban a-priori (w=0.3, α=0.05, power=0.80, df=1); yalnızca"
TABAN_P = "taban post-hoc (w=0.3, α=0.05, n_total=100, df=1); yalnızca"

# (mode, w, alpha, power, n_total, df, kategori, amac) — değerler metin olarak, yazıldığı gibi
V = [
    # a) Kalibrasyon
    (A, "0.3", "0.05", "0.95", "", "5", "kalibrasyon", "CONTRACT.md Bölüm 9 chi2-contingency/a-priori; elle girişin doğruluğunu kanıtlar"),
    (P, "0.3", "0.05", "", "100", "5", "kalibrasyon", "CONTRACT.md Bölüm 9 chi2-contingency/post-hoc; elle girişin doğruluğunu kanıtlar"),
    # b) Tipik a-priori
    (A, "0.1", "0.05", "0.80", "", "1", "tipik-a-priori", "küçük etki, df=1, klasik α/güç"),
    (A, "0.3", "0.05", "0.80", "", "1", "tipik-a-priori", "orta etki, df=1, klasik α/güç (sınır satırlarının a-priori tabanı)"),
    (A, "0.5", "0.05", "0.80", "", "1", "tipik-a-priori", "büyük etki, df=1, klasik α/güç"),
    (A, "0.3", "0.01", "0.90", "", "2", "tipik-a-priori", "orta etki, sıkı α, df=2"),
    (A, "0.1", "0.05", "0.95", "", "3", "tipik-a-priori", "küçük etki, yüksek güç, df=3 (büyük N)"),
    (A, "0.5", "0.10", "0.90", "", "4", "tipik-a-priori", "büyük etki, gevşek α, df=4 (küçük N; yuvarlama)"),
    (A, "0.3", "0.10", "0.80", "", "6", "tipik-a-priori", "orta etki, gevşek α, df=6"),
    (A, "0.1", "0.01", "0.80", "", "10", "tipik-a-priori", "küçük etki, sıkı α, df=10 (çok büyük N)"),
    (A, "0.5", "0.01", "0.95", "", "10", "tipik-a-priori", "büyük etki, sıkı α, yüksek güç, df=10"),
    (A, "0.3", "0.05", "0.90", "", "3", "tipik-a-priori", "orta etki, df=3, güç 0.90"),
    # c) Tipik post-hoc
    (P, "0.3", "0.05", "", "88", "1", "tipik-post-hoc", f"orta etki, df=1 a-priori satırıyla aynı ayar; güç ≈0.80 olmalı; {COHEN_N}"),
    (P, "0.5", "0.05", "", "32", "1", "tipik-post-hoc", f"büyük etki, df=1 a-priori satırıyla aynı ayar; güç ≈0.80 olmalı; {COHEN_N}"),
    (P, "0.1", "0.05", "", "785", "1", "tipik-post-hoc", f"küçük etki, df=1 a-priori satırıyla aynı ayar; güç ≈0.80 olmalı; {COHEN_N}"),
    (P, "0.1", "0.01", "", "1000", "10", "tipik-post-hoc", "küçük etki, sıkı α, df=10, üst N sınırı"),
    (P, "0.5", "0.10", "", "20", "4", "tipik-post-hoc", "büyük etki, gevşek α, alt N sınırı"),
    (P, "0.3", "0.01", "", "150", "2", "tipik-post-hoc", "orta etki, sıkı α, df=2"),
    (P, "0.5", "0.05", "", "50", "6", "tipik-post-hoc", "büyük etki, df=6"),
    (P, "0.3", "0.10", "", "300", "3", "tipik-post-hoc", "orta etki, gevşek α, df=3"),
    # d) Sınır değerler (geçerli olması beklenen) — her satırda tabandan yalnızca TEK değer sınırda
    (A, "0.01", "0.05", "0.80", "", "1", "sinir", f"{TABAN_A} w=0.01 (çok küçük; çok büyük N, taşma/üst sınır var mı?)"),
    (P, "0.02", "0.05", "", "100", "1", "sinir", f"{TABAN_P} w=0.02 (çok küçük; güç α'ya çok yakın)"),
    (A, "1.0", "0.05", "0.80", "", "1", "sinir", f"{TABAN_A} w=1.0 (büyük; çok küçük N)"),
    (A, "2.0", "0.05", "0.80", "", "1", "sinir", f"{TABAN_A} w=2.0 (çok büyük; N alt sınıra dayanır mı?)"),
    (A, "5.0", "0.05", "0.80", "", "1", "sinir", f"{TABAN_A} w=5.0 (aşırı büyük; alan kabul ediyor mu?)"),
    (A, "0.3", "0.05", "0.80", "", "50", "sinir", f"{TABAN_A} df=50 (büyük)"),
    (P, "0.3", "0.05", "", "100", "100", "sinir", f"{TABAN_P} df=100 (çok büyük)"),
    (A, "0.3", "0.05", "0.99", "", "1", "sinir", f"{TABAN_A} power=0.99"),
    (A, "0.3", "0.001", "0.80", "", "1", "sinir", f"{TABAN_A} α=0.001 (çok küçük)"),
    (A, "0.3", "0.05", "0.05", "", "1", "sinir", f"{TABAN_A} power=0.05 = α (çözüm var mı, N kaç?)"),
    (A, "0.3", "0.05", "0.03", "", "1", "sinir", f"{TABAN_A} power=0.03 < α (hata mı, sonuç mu?)"),
    (P, "0.3", "0.05", "", "2", "1", "sinir", f"{TABAN_P} n_total=2 (sözleşmedeki alt sınır)"),
    # e) Geçersiz girdiler
    (A, "0", "0.05", "0.95", "", "5", "gecersiz", "w=0: alan reddediyor mu, mesaj ne?"),
    (A, "-0.3", "0.05", "0.95", "", "5", "gecersiz", "w negatif: alan reddediyor mu, mesaj ne?"),
    (A, "0.3", "0.05", "0.95", "", "0", "gecersiz", "df=0: alan reddediyor mu, mesaj ne?"),
    (A, "0.3", "0.05", "0.95", "", "2.5", "gecersiz", "df ondalık: yuvarlıyor mu, reddediyor mu?"),
    (A, "0.3", "0.05", "1", "", "5", "gecersiz", "power=1: alan reddediyor mu, mesaj ne?"),
    (P, "0.3", "0", "", "100", "5", "gecersiz", "alpha=0: alan reddediyor mu, mesaj ne?"),
]

cols = ["id", "mode", "w", "alpha", "power", "n_total", "df", "kategori", "amac"]
rows = [dict(zip(cols, (f"K4-{i:03d}",) + v)) for i, v in enumerate(V, 1)]
res_cols = ["g_ncp", "g_critical_chi2", "g_n_total", "g_actual_power", "g_power", "g_tepki", "screenshot"]

keys = [tuple(r[c] for c in cols[1:7]) for r in rows]
assert len(set(keys)) == len(keys), "aynı girdi iki kez var"
assert all(r["n_total"] == "" for r in rows if r["mode"] == A)
assert all(r["power"] == "" for r in rows if r["mode"] == P)

def write_csv(path, header, data):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header, lineterminator="\n")
        w.writeheader()
        w.writerows(data)

write_csv(os.path.join(out, "K4_plan.csv"), cols, rows)
# Sonuç dosyası elle doldurulur; varsa asla üzerine yazılmaz
results_path = os.path.join(out, "K4_gui_results.csv")
if os.path.exists(results_path):
    print("K4_gui_results.csv zaten var, korunuyor")
else:
    write_csv(results_path, cols + res_cols, [{**r, **{c: "" for c in res_cols}} for r in rows])

# Kalibrasyon beklenenleri: CONTRACT.md Bölüm 9'dan birebir
EXPECTED = {
    ("kalibrasyon", A): "Noncentrality parameter λ = 19.8000000 · Critical χ² = 11.0704977 · Total sample size = 220 · Actual power = 0.9502155",
    ("kalibrasyon", P): "Noncentrality parameter λ = 9.0000000 · Critical χ² = 11.0704977 · Power (1-β err prob) = 0.6235846",
}
MODE_LABEL = {A: "A priori", P: "Post hoc"}
counts = collections.Counter(r["kategori"] for r in rows)
SECTIONS = [
    ("kalibrasyon", "A. Kalibrasyon ({}) — önce bunlar; tutmazsa DUR"),
    ("tipik-a-priori", "B. Tipik a-priori ({})"),
    ("tipik-post-hoc", "C. Tipik post-hoc ({})"),
    ("sinir", "D. Sınır değerler ({}) — tabandan yalnızca **kalın** değer farklı"),
    ("gecersiz", "E. Geçersiz girdiler ({}) — tepkiyi birebir yaz"),
]
BASE = {A: {"w": "0.3", "alpha": "0.05", "power": "0.80", "df": "1"},
        P: {"w": "0.3", "alpha": "0.05", "n_total": "100", "df": "1"}}

def inputs(r):
    fields = [("w", "Effect size w"), ("alpha", "α err prob")]
    fields.append(("power", "Power (1-β err prob)") if r["mode"] == A else ("n_total", "Total sample size"))
    fields.append(("df", "Df"))
    parts = []
    for key, label in fields:
        val = r[key]
        if r["kategori"] == "sinir" and val != BASE[r["mode"]][key]:
            val = f"**{val}**"
        parts.append(f"{label} = {val}")
    return " · ".join(parts)

md = [
    "# K4 Elle Giriş Listesi — chi2-contingency",
    "",
    "**G*Power 3.1.9.7:** Test family = **χ² tests** · Statistical test = **Goodness-of-fit tests: Contingency tables**",
    "**Mod:** Type of power analysis = **A priori: Compute required sample size** ya da **Post hoc: Compute achieved power**",
    "",
    "Her satırda: değerleri gir → *Calculate* → sonuçları `K4_gui_results.csv`'ye yaz → ekran görüntüsünü `oracle/screenshots/<id>.png` olarak kaydet.",
    "Hata çıkarsa mesajı **birebir** `g_tepki` sütununa yaz; alan değeri kabul etmiyorsa bunu da not et.",
    "",
    f"Toplam: **{len(rows)} vektör**. Sınır satırlarının tabanı: a-priori w=0.3 · α=0.05 · power=0.80 · Df=1; post-hoc w=0.3 · α=0.05 · N=100 · Df=1.",
    "",
]
for key, title in SECTIONS:
    md += [f"## {title.format(counts[key])}", "", "| id | Mod | Girilecek değerler | Beklenen | ☐ |", "|---|---|---|---|---|"]
    for r in rows:
        if r["kategori"] == key:
            md.append(f"| {r['id']} | {MODE_LABEL[r['mode']]} | {inputs(r)} | {EXPECTED.get((key, r['mode']), '—')} | ☐ |")
    md.append("")
with open(os.path.join(out, "K4_GIRIS_LISTESI.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(md))
print("vektör:", len(rows), dict(counts))
