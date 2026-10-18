"""Masked color-difference (leakage) metric.

For each frame t: dE(t,x) = CIE76 distance between original and generated in CIELAB.
Report mean dE inside the mask (region the model was meant to change) and outside it
(region meant to be preserved), per frame and overall. Also a hue-only variant.
"""
import sys, os, csv
import numpy as np, cv2

orig_p, gen_p, mask_p, out_dir = sys.argv[1:5]
os.makedirs(out_dir, exist_ok=True)

def frames(p):
    cap = cv2.VideoCapture(p)
    while True:
        ok, f = cap.read()
        if not ok: break
        yield f
    cap.release()

def to_lab(bgr):
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2Lab).astype(np.float32)
    lab[..., 0] *= 100.0 / 255.0
    lab[..., 1] -= 128.0
    lab[..., 2] -= 128.0
    return lab

rows = []
heat_saved = False
acc_in = acc_out = 0.0; n_in = n_out = 0
for t, (o, g, m) in enumerate(zip(frames(orig_p), frames(gen_p), frames(mask_p))):
    if g.shape != o.shape: g = cv2.resize(g, (o.shape[1], o.shape[0]))
    if m.shape[:2] != o.shape[:2]: m = cv2.resize(m, (o.shape[1], o.shape[0]), interpolation=cv2.INTER_NEAREST)
    mask = cv2.cvtColor(m, cv2.COLOR_BGR2GRAY) > 127
    lo, lg = to_lab(o), to_lab(g)
    dE = np.linalg.norm(lo - lg, axis=2)
    dC = np.linalg.norm(lo[..., 1:] - lg[..., 1:], axis=2)  # chroma-only (a,b), ignores lightness
    inside, outside = dE[mask], dE[~mask]
    rows.append(dict(frame=t, mask_frac=float(mask.mean()),
                     dE_in=float(inside.mean()), dE_out=float(outside.mean()),
                     dC_in=float(dC[mask].mean()), dC_out=float(dC[~mask].mean()),
                     frac_out_gt10=float((outside > 10).mean()),
                     frac_out_gt20=float((outside > 20).mean())))
    acc_in += inside.sum(); n_in += inside.size
    acc_out += outside.sum(); n_out += outside.size
    if t in (0, 30, 59):
        # heatmap: dE clipped to [0,60] -> color map; draw mask contour
        hm = cv2.applyColorMap(np.clip(dE / 60.0 * 255, 0, 255).astype(np.uint8), cv2.COLORMAP_INFERNO)
        cnts, _ = cv2.findContours(mask.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(hm, cnts, -1, (255, 255, 255), 2)
        cv2.imwrite(os.path.join(out_dir, f"dE_heatmap_f{t:02d}.png"), hm)
        cv2.imwrite(os.path.join(out_dir, f"orig_f{t:02d}.png"), o)
        cv2.imwrite(os.path.join(out_dir, f"gen_f{t:02d}.png"), g)
        cv2.imwrite(os.path.join(out_dir, f"mask_f{t:02d}.png"), (mask * 255).astype(np.uint8))

with open(os.path.join(out_dir, "leakage_per_frame.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

a = {k: np.array([r[k] for r in rows]) for k in rows[0]}
summary = {
    "frames": len(rows),
    "mask_frac_mean": a["mask_frac"].mean(),
    "dE_in_mean": acc_in / n_in, "dE_in_std_over_frames": a["dE_in"].std(),
    "dE_out_mean": acc_out / n_out, "dE_out_std_over_frames": a["dE_out"].std(),
    "dC_in_mean": a["dC_in"].mean(), "dC_out_mean": a["dC_out"].mean(),
    "ratio_out_over_in": (acc_out / n_out) / (acc_in / n_in),
    "frac_outside_pixels_dE_gt10": a["frac_out_gt10"].mean(),
    "frac_outside_pixels_dE_gt20": a["frac_out_gt20"].mean(),
}
with open(os.path.join(out_dir, "leakage_summary.txt"), "w") as f:
    for k, v in summary.items():
        line = f"{k}: {v:.4f}" if isinstance(v, float) else f"{k}: {v}"
        print(line); f.write(line + "\n")

try:
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(a["frame"], a["dE_in"], label="inside mask (target)")
    ax.plot(a["frame"], a["dE_out"], label="outside mask (protected)")
    ax.set_xlabel("frame (4 fps)"); ax.set_ylabel("mean CIE76 $\\Delta E$"); ax.legend(frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(os.path.join(out_dir, "leakage_per_frame.pdf")); fig.savefig(os.path.join(out_dir, "leakage_per_frame.png"), dpi=200)
    print("plot saved")
except Exception as e:
    print("no plot:", e)
