# PRA2003 - Week 5: Python version of the plot from momentumDifference.R
#
# Reads the results that momentumDifference.R writes and draws the same
# figure with matplotlib: one panel per WT/mutant pair, the difference per
# event in each momentum bin with +- SD error bars, and the fitted constant
# with its +- 1 sigma band.
#
# HOW TO RUN:
#   Run momentumDifference.R first, then in the same folder:
#     python momentum_difference_plot.py
#   Needs pandas and matplotlib (pip install pandas matplotlib).
#
# Writes:
#   momentum_difference_py.png           (Sets 1-9, main result)
#   momentum_difference_all_sets_py.png  (all 10 sets, for comparison)

import os

import matplotlib.pyplot as plt
import pandas as pd

# Same order as pairName in the R script
pair_names = ["E. coli", "Bacillus subtilis", "Pseudomonas aeruginosa",
              "Streptococcus pneumoniae", "Mycobacterium tuberculosis",
              "Salmonella"]


def plot_sets(name_suffix, sets_text):
    results_file = f"momentum_difference_results{name_suffix}.csv"
    fit_file = f"momentum_difference_fit{name_suffix}.csv"

    if not (os.path.exists(results_file) and os.path.exists(fit_file)):
        print(f"Skipping '{name_suffix or 'main'}': cannot find {results_file} "
              f"or {fit_file}. Run momentumDifference.R first.")
        return

    results = pd.read_csv(results_file)
    fits = pd.read_csv(fit_file)

    fig, axes = plt.subplots(2, 3, figsize=(18, 11))

    for ax, name in zip(axes.flat, pair_names):
        rows = results[results["Strain"] == name].sort_values("MomentumBin")
        fit = fits[fits["Strain"] == name].iloc[0]

        x = rows["MomentumBin"].to_numpy()
        y = rows["Difference"].to_numpy()
        err = rows["Uncertainty"].to_numpy()
        n_bins = len(x)

        c = fit["Constant"]
        c_err = fit["ConstantUncertainty"]

        # fitted constant with its +- 1 sigma band
        ax.axhspan(c - c_err, c + c_err, color="red", alpha=0.15, lw=0)
        ax.axhline(c, color="red", lw=2)
        ax.axhline(0, color="grey", ls="--", lw=1)  # no difference

        # points with +- SD error bars
        ax.errorbar(x, y, yerr=err, fmt="o", color="darkblue",
                    ecolor="black", capsize=4, markersize=6)

        # make sure zero is always visible, like range(c(low, high, 0)) in R
        low = min((y - err).min(), 0)
        high = max((y + err).max(), 0)
        pad = 0.05 * (high - low)
        ax.set_ylim(low - pad, high + pad)
        ax.set_xlim(0.7, n_bins + 0.3)

        ax.set_xticks(x)
        ax.set_xticklabels(rows["MomentumRange"], fontsize=9)
        ax.set_xlabel(r"Momentum bin |p| ($10^{-20}$ kg m/s)", fontsize=10)
        ax.set_ylabel("Difference per event (WT - mutant)", fontsize=10)

        ax.set_title(name, fontstyle="italic", fontsize=13, pad=22)
        ax.text(0.5, 1.02,
                f"constant = {c:.3g} ± {c_err:.3g} ({fit['Significance']:.1f}σ), "
                f"χ²/ndf = {fit['Chi2']:.1f}/{int(fit['ndf'])}",
                transform=ax.transAxes, ha="center", va="bottom", fontsize=9)

    fig.suptitle(f"Difference per event vs momentum ({sets_text})",
                 fontweight="bold", fontsize=15)
    fig.tight_layout(rect=[0, 0, 1, 0.96])

    out_file = f"momentum_difference{name_suffix}_py.png"
    fig.savefig(out_file, dpi=140)
    plt.close(fig)
    print(f"Wrote {out_file}")


# Main result: Sets 1-9 (Set 10 excluded, as in the R script)
plot_sets("", "sets 1,2,3,4,5,6,7,8,9")

# Comparison: all 10 sets
plot_sets("_all_sets", "sets 1,2,3,4,5,6,7,8,9,10")
