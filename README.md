# Drug Response 23andMe

A Python package to annotate 23andMe raw data with PharmGKB drug response information.

## Overview

This tool allows users to:
1.  Parse raw 23andMe genotype files.
2.  Integrate variant annotations from PharmGKB.
3.  Identify significant efficacy variants relevant to the user's genotype.
4.  Visualize the distribution of drug responses and SNPs per gene.

## Installation

You can install the package directly from the source:

```bash
git clone https://github.com/GSYH/drug_response_23andme.git
cd drug_response_23andme
pip install .
```

## Usage

### Python API

```python
from drug_response_23andme import loader, processor, visualizer

# 1. Load Data
# Replace with your actual file paths
df_23 = loader.load_23andme("path/to/23andme_v5_hg19_ref.txt")
df_ann = loader.load_pharmgkb("path/to/var_drug_ann.tsv")

# 2. Process Data
# Merge datasets on dbSNP_ID
merged_df = processor.merge_data(df_23, df_ann)

# Filter for significant efficacy variants
filtered_df = processor.filter_significant_efficacy(merged_df)

# Create a summary table
summary_df = processor.summarize_data(filtered_df)
print(summary_df.head())

# 3. Visualize
# Generate plots for drugs/gene and SNPs/gene
visualizer.plot_stats(filtered_df, output_prefix="my_analysis")
```

## Data Sources

*   **23andMe**: Your raw genotype data (txt file).
*   **PharmGKB**: Variant annotations (`var_drug_ann.tsv`) available from [PharmGKB](https://www.pharmgkb.org/).

## License

This project is licensed under the MIT License.
