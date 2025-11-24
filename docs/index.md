# Welcome to Drug Response 23andMe

This package allows you to annotate your 23andMe raw data with drug response information from PharmGKB.

## Features

*   **Load 23andMe Data**: Easily parse your raw 23andMe text file.
*   **Load PharmGKB Data**: Import variant annotations from PharmGKB.
*   **Merge & Filter**: Combine datasets to find significant efficacy variants relevant to your genotype.
*   **Visualize**: Generate plots showing the distribution of drugs and SNPs per gene.

## Installation

```bash
pip install .
```

## Quick Start

```python
from drug_response_23andme import loader, processor, visualizer

# Load data
df_23 = loader.load_23andme("path/to/23andme.txt")
df_ann = loader.load_pharmgkb("path/to/var_drug_ann.tsv")

# Process
merged = processor.merge_data(df_23, df_ann)
filtered = processor.filter_significant_efficacy(merged)
summary = processor.summarize_data(filtered)

# Visualize
visualizer.plot_stats(filtered)
```
