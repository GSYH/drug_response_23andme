# User Guide

## Prerequisites

You need two files:
1.  **23andMe Raw Data**: A text file containing your genotype data.
2.  **PharmGKB Variant Annotations**: A TSV file (`var_drug_ann.tsv`) from PharmGKB.

## Step-by-Step

1.  **Load the Data**: Use `loader.load_23andme()` and `loader.load_pharmgkb()` to read your files into pandas DataFrames.
2.  **Merge**: Use `processor.merge_data()` to join the two DataFrames on `dbSNP_ID`. This keeps only the variants present in both files.
3.  **Filter**: Use `processor.filter_significant_efficacy()` to keep only variants with "Significant" evidence and "Efficacy" phenotype category.
4.  **Summarize**: Use `processor.summarize_data()` to get a clean table of genes and drugs.
5.  **Plot**: Use `visualizer.plot_stats()` to see histograms of your results.
