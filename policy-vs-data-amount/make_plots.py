"""Plot policy performance against data amount from the compiled reference data.

Reads the CSV files in data/ and writes to figures/:
  policy_vs_data_amount.{pdf,png}        one figure, panels (a) to (e)   [used in the paper]
  policy_vs_hours.{pdf,png}              panels (a) to (c) alone
  diversity_and_collection_time.{pdf,png} panels (d) and (e) alone
  fits.json                              fitted parameters

Run from anywhere:  python make_plots.py
"""
import csv
import json
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.ticker import FixedLocator, FuncFormatter, NullFormatter  # noqa: E402

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)

# Palette: validated categorical slots 1 to 3 (dataviz reference palette, light surface).
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, GRID = "#0b0b0b", "#52514e", "#e6e5e1"

plt.rcParams.update({
    "font.size": 8, "axes.titlesize": 8.5, "axes.labelsize": 8,
    "xtick.labelsize": 7.5, "ytick.labelsize": 7.5, "legend.fontsize": 7,
    "pdf.fonttype": 42, "ps.fonttype": 42, "savefig.dpi": 200,
    "text.color": INK, "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2,
})

fits = {}


def read(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def style(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(INK2)
        ax.spines[s].set_linewidth(0.6)
    ax.grid(axis="y", color=GRID, linewidth=0.5)
    ax.set_axisbelow(True)
    ax.tick_params(length=2.5, width=0.6)


def loglin_fit(x, y):
    """Fit y = a + b ln(x); return a, b, R^2."""
    X = np.log(np.asarray(x, float))
    y = np.asarray(y, float)
    b, a = np.polyfit(X, y, 1)
    yhat = a + b * X
    r2 = 1 - ((y - yhat) ** 2).sum() / ((y - y.mean()) ** 2).sum()
    return a, b, r2


def series(ax, x, y, color, label, ls="-", marker="o"):
    ax.plot(x, y, ls, color=color, lw=1.5, marker=marker, ms=5,
            mec="white", mew=0.8, label=label, zorder=3)


def end_label(ax, x, y, text, dy=0):
    ax.annotate(text, (x, y), xytext=(4, dy), textcoords="offset points",
                color=INK2, fontsize=7, va="center", ha="left", zorder=5,
                bbox=dict(boxstyle="square,pad=0.15", fc="white", ec="none"))


def k_formatter(v, _):
    return f"{int(v / 1000)}k"


# ------------------------------------------------------------------ panels

def panel_egoscale(ax, tag):
    rows = read("egoscale_task_completion.csv")
    h = [float(r["human_pretraining_hours"]) for r in rows]
    s = [float(r["avg_task_completion_score"]) for r in rows]
    a, b, r2 = loglin_fit(h, s)
    fits["egoscale_score_vs_ln_hours"] = {"a": a, "b": b, "r2": r2}
    hh = np.logspace(np.log10(900), np.log10(23000), 50)
    ax.plot(hh, a + b * np.log(hh), "--", color=BLUE, lw=1, alpha=0.7, zorder=2)
    series(ax, h, s, BLUE, "EgoScale")
    ax.set_xscale("log")
    ax.xaxis.set_major_locator(FixedLocator([1000, 2000, 4000, 10000, 20000]))
    ax.xaxis.set_major_formatter(FuncFormatter(k_formatter))
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.set_xlim(850, 26000)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Human pretraining data (hours)")
    ax.set_ylabel("Avg. task completion score")
    ax.set_title(f"({tag}) EgoScale, human video", loc="left")
    ax.text(0.03, 0.95, f"fit: {a:.2f} + {b:.3f} ln(h)\nR² = {r2:.2f}",
            transform=ax.transAxes, va="top", fontsize=7, color=INK2)
    style(ax)


def panel_lingbot(ax, tag):
    rows = read("lingbot_scaling_fig5_readoff.csv")
    h = [float(r["pretraining_hours"]) for r in rows]
    sr = [float(r["success_rate_pct_avg"]) / 100 for r in rows]
    ps = [float(r["progress_rate_pct_avg"]) / 100 for r in rows]
    a, b, r2 = loglin_fit(h, sr)
    fits["lingbot_success_vs_ln_hours_readoff"] = {"a": a, "b": b, "r2": r2}
    hh = np.logspace(np.log10(2700), np.log10(23000), 50)
    ax.plot(hh, a + b * np.log(hh), "--", color=BLUE, lw=1, alpha=0.7, zorder=2)
    series(ax, h, sr, BLUE, "Success rate")
    series(ax, h, ps, ORANGE, "Progress rate")
    end_label(ax, h[-1], sr[-1], "success")
    end_label(ax, h[-1], ps[-1], "progress")
    ax.set_xscale("log")
    ax.xaxis.set_major_locator(FixedLocator([3000, 6000, 13000, 20000]))
    ax.xaxis.set_major_formatter(FuncFormatter(k_formatter))
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.set_xlim(2500, 36000)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Robot pretraining data (hours)")
    ax.set_ylabel("Rate (fraction), 25 tasks")
    ax.set_title(f"({tag}) LingBot-VLA, robot data", loc="left")
    ax.text(0.03, 0.95, f"fit (success): {a:.2f} + {b:.3f} ln(h)\nR² = {r2:.2f}; read off Fig. 5",
            transform=ax.transAxes, va="top", fontsize=6.5, color=INK2)
    ax.legend(loc="lower right", frameon=False, handlelength=1.6)
    style(ax)


def panel_pi0(ax, tag):
    rows = read("pi0_finetune_hours_fig11_readoff.csv")
    h = [float(r["finetuning_hours"]) for r in rows]
    p = [float(r["pi0_pretrained_avg_task_progress"]) for r in rows]
    q = [float(r["pi0_scratch_avg_task_progress"]) for r in rows]
    d = [float(r["diffusion_policy_avg_task_progress"]) for r in rows]
    series(ax, h, p, BLUE, "π₀ pretrained")
    series(ax, h, q, ORANGE, "π₀ from scratch")
    series(ax, h, d, AQUA, "Diffusion Policy")
    ax.set_xscale("log")
    ax.xaxis.set_major_locator(FixedLocator([1, 5, 10]))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{int(v)}"))
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.set_xlim(0.85, 14)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Fine-tuning data (hours)")
    ax.set_ylabel("Avg. task progress, 6 tasks")
    ax.set_title(f"({tag}) π₀, fine-tuning data", loc="left")
    ax.text(0.03, 0.95, "values read off Fig. 11", transform=ax.transAxes, va="top",
            fontsize=6.5, color=INK2)
    ax.legend(loc="lower left", frameon=False, handlelength=1.6, bbox_to_anchor=(0.0, -0.02))
    style(ax)


def panel_lin(ax, tag):
    rows = [r for r in read("lin2025_powerlaw_fits.csv") if r["task"] == "Mouse Arrangement"]
    x = np.array([1, 2, 4, 8, 16, 32], float)
    xx = np.logspace(0, np.log10(32), 60)
    colors = {"training environments": BLUE, "training objects": ORANGE,
              "environment-object pairs": AQUA}
    short = {"training environments": "environments", "training objects": "objects",
             "environment-object pairs": "env-object pairs"}
    ends = {}
    for r in rows:
        beta, alpha = float(r["beta"]), float(r["alpha"])
        c = colors[r["x_variable"]]
        yy = 1 - beta * xx ** alpha
        keep = yy >= 0
        ax.plot(xx[keep], yy[keep], "-", color=c, lw=1.5, zorder=3,
                label=f"{short[r['x_variable']]}: $1 - {beta:.3f}\\,x^{{{alpha:.3f}}}$")
        ax.plot(x, 1 - beta * x ** alpha, "o", color=c, ms=5, mec="white", mew=0.8, zorder=4)
        ends[r["x_variable"]] = 1 - beta * 32 ** alpha
        key = short[r["x_variable"]].replace(" ", "_").replace("-", "_")
        fits[f"lin_mouse_{key}_score_at_32"] = ends[r["x_variable"]]
    ax.axhline(0.9, color=INK2, lw=0.6, ls=":", zorder=1)
    ax.text(1.05, 0.915, "0.9", fontsize=6.5, color=INK2)
    end_label(ax, 32, ends["training objects"], "objects", dy=6)
    end_label(ax, 32, ends["environment-object pairs"], "env-object pairs", dy=0)
    end_label(ax, 32, ends["training environments"], "environments", dy=-6)
    ax.set_xscale("log", base=2)
    ax.xaxis.set_major_locator(FixedLocator([1, 2, 4, 8, 16, 32]))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{int(v)}"))
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.set_xlim(0.9, 75)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Number of training environments / objects / pairs")
    ax.set_ylabel("Normalized score (1 - optimality gap)")
    ax.set_title(f"({tag}) Lin et al. 2025, published power-law fits", loc="left")
    ax.legend(loc="lower right", frameon=False, handlelength=1.6, fontsize=6.3)
    style(ax)


def panel_fieldgen(ax, tag):
    rows = read("fieldgen_equal_time_table1.csv")
    for policy, ls in (("DP", "-"), ("RDT-small", "--")):
        for method, c in (("FieldGen", BLUE), ("Teleoperation", ORANGE)):
            rr = [r for r in rows if r["policy"] == policy and r["collection_method"] == method]
            m = [float(r["collection_minutes"]) for r in rr]
            v = [float(r["success_rate_pct_avg_4_tasks"]) / 100 for r in rr]
            series(ax, m, v, c, f"{method}, {policy}", ls=ls,
                   marker="o" if policy == "DP" else "s")
            fits[f"fieldgen_{method}_{policy}_at_20min"] = v[-1]
    end_label(ax, 20, 0.979, "FieldGen", dy=3)
    end_label(ax, 20, 0.646, "Teleoperation", dy=3)
    ax.set_xticks([4, 8, 12, 16, 20])
    ax.set_xlim(3, 26)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Collection time (minutes)")
    ax.set_ylabel("Success rate, mean of 4 tasks")
    ax.set_title(f"({tag}) FieldGen, equal collection time", loc="left")
    ax.legend(loc="lower right", frameon=False, handlelength=2.2, fontsize=6.3, ncol=1)
    style(ax)


# ------------------------------------------------------------------ figures

def save(fig, stem):
    fig.savefig(OUT / f"{stem}.pdf")
    fig.savefig(OUT / f"{stem}.png")
    plt.close(fig)


# Combined figure, panels (a) to (e): three on top, two below.
fig = plt.figure(figsize=(6.6, 4.9), constrained_layout=True)
fig.set_constrained_layout_pads(w_pad=0.04, h_pad=0.06, wspace=0.08, hspace=0.12)
gs = fig.add_gridspec(2, 6, height_ratios=[1, 1.05])
panel_egoscale(fig.add_subplot(gs[0, 0:2]), "a")
panel_lingbot(fig.add_subplot(gs[0, 2:4]), "b")
panel_pi0(fig.add_subplot(gs[0, 4:6]), "c")
panel_lin(fig.add_subplot(gs[1, 0:3]), "d")
panel_fieldgen(fig.add_subplot(gs[1, 3:6]), "e")
save(fig, "policy_vs_data_amount")

# The two separate figures, kept for slides and the README.
fig, axes = plt.subplots(1, 3, figsize=(6.6, 2.35))
panel_egoscale(axes[0], "a")
panel_lingbot(axes[1], "b")
panel_pi0(axes[2], "c")
fig.tight_layout(w_pad=1.2)
save(fig, "policy_vs_hours")

fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.45))
panel_lin(axes[0], "a")
panel_fieldgen(axes[1], "b")
fig.tight_layout(w_pad=1.2)
save(fig, "diversity_and_collection_time")

with open(OUT / "fits.json", "w", encoding="utf-8") as f:
    json.dump(fits, f, indent=2)
print(json.dumps(fits, indent=2))
