# PRA2003 - Week 5: plot of the WT - mutant difference vs momentum (Python)

# For each of the 6 WT/mutant pairs it draws:
#   - the difference per event in each momentum bin, with +- SD error bars
#     (plt.errorbar, like the "graph w/ uncertainties" example)
#   - the fitted constant as a red line, with its +- 1 sigma uncertainty
#     as a shaded band (plt.fill_between)
#   - a dashed line at zero (= no difference between WT and mutant)
#
# HOW TO RUN:
#   1. Run Week5_momentum_Difference.R first. It writes the CSV files read here.
#   2. In the same folder: python momentum_difference_plot.py
#   Needs numpy, pandas and matplotlib (pip install numpy pandas matplotlib).
#
# Writes:
#   momentum_difference_py.png           (Sets 1-9, main result)
#   momentum_difference_all_sets_py.png  (all 10 sets, for comparison)

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read and save everything in the folder this script is in, so it works no
# matter which folder VS Code's terminal is in
folder = os.path.dirname(os.path.abspath(__file__))

# Same order as pairName in the R script
pairNames = ["E. coli", "Bacillus subtilis", "Pseudomonas aeruginosa",
             "Streptococcus pneumoniae", "Mycobacterium tuberculosis",
             "Salmonella"]

# The two versions written by the R script: (end of the file name, sets used)
versions = [("", "sets 1-9"),
            ("_all_sets", "sets 1-10")]

for nameSuffix, setsText in versions:

    # Read the results of the R script (pandas DataFrames)
    results = pd.read_csv(os.path.join(folder, "momentum_difference_results" + nameSuffix + ".csv"))
    fitResults = pd.read_csv(os.path.join(folder, "momentum_difference_fit" + nameSuffix + ".csv"))

    # Print the data that is plotted
    print("\n==== Using", setsText, "====")
    print(results)
    print(fitResults)

    # Create the plot: one panel per pair, 2 rows x 3 columns
    plt.figure(figsize=(18, 10))

    for i in range(len(pairNames)):
        pairRows = results[results["Strain"] == pairNames[i]]
        fit = fitResults[fitResults["Strain"] == pairNames[i]]

        x = np.array(pairRows["MomentumBin"])
        y = np.array(pairRows["Difference"])
        yErrors = np.array(pairRows["Uncertainty"])

        constant = fit["Constant"].iloc[0]
        constantError = fit["ConstantUncertainty"].iloc[0]
        significance = fit["Significance"].iloc[0]
        chi2 = fit["Chi2"].iloc[0]
        ndf = fit["ndf"].iloc[0]

        plt.subplot(2, 3, i + 1)

        # Fitted constant with its +- 1 sigma uncertainty as a shaded band
        xBand = np.array([0.5, len(x) + 0.5])
        plt.fill_between(xBand, constant - constantError, constant + constantError,
                         color='red', alpha=0.2)
        plt.plot(xBand, [constant, constant], color='red', linewidth=2,
                 label='Fitted constant')

        # Line at zero: no difference between WT and mutant
        plt.axhline(0, color='gray', linestyle='--')

        # Data points with their uncertainties (SD of the files)
        plt.errorbar(x, y, yerr=yErrors, fmt='o', color='darkblue', ecolor='black',
                     capsize=4, label='Data (mean +- SD)')

        # Add titles and labels
        plt.title(pairNames[i] + "\n" +
                  f"constant = {constant:.3g} +- {constantError:.3g} "
                  f"({significance:.1f} sigma), chi2/ndf = {chi2:.1f}/{ndf}",
                  fontsize=10)
        plt.xticks(x, pairRows["MomentumRange"])
        plt.xlim(0.5, len(x) + 0.5)
        plt.xlabel('Momentum bin |p| (10^-20 kg m/s)')
        plt.ylabel('Difference per event (WT - mutant)')

        # Add legend and grid
        plt.legend(fontsize=8)
        plt.grid(True)

    plt.suptitle("Difference per event vs momentum (" + setsText + ")",
                 fontsize=14, fontweight='bold')
    plt.tight_layout()

    # Save the plot to a file (before plt.show, otherwise the saved image is empty)
    outFile = os.path.join(folder, "momentum_difference" + nameSuffix + "_py.png")
    plt.savefig(outFile, dpi=150)
    print("Saved the plot to", outFile)

    # Display the plot
    plt.show()
