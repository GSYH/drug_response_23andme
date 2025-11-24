# Drug Response 23andMe

[![Documentation](https://img.shields.io/badge/docs-live-blue)](https://GSYH.github.io/drug_response_23andme/)

A Python package to annotate 23andMe raw data with PharmGKB drug response information.

**[📚 Read the Documentation](https://GSYH.github.io/drug_response_23andme/)**

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

## Data Sources & Credits

This package relies on data from the following sources:

*   **23andMe Data**: Raw genotype data from 23andMe.
    *   *Note*: If you need to convert 23andMe data to VCF, you might find [23andme2vcf](https://github.com/arrogantrobot/23andme2vcf) useful.
    *   **File Format**: The expected input is a tab-separated text file with columns: `CHR`, `POS`, `dbSNP_ID`, `ALLELE`.
*   **PharmGKB Data**: Variant annotations from the [PharmGKB Downloads page](https://www.pharmgkb.org/downloads).
    *   Specifically, the `var_drug_ann.tsv` file found within the `variantAnnotations.zip` archive.
    *   **File Format**: A tab-separated file containing columns such as `Variant/Haplotypes`, `Gene`, `Drug(s)`, `PMID`, `Phenotype Category`, `Significance`, `Notes`, `Sentence`, and `Alleles`.
    *   *Note*: The loader handles a known formatting issue in some versions of this file (an unclosed quote on a specific line).

## Acknowledgements

Special thanks to **Professor Cristina Mitrea** for guidance and support in the development of this project for the BIOINF575 Programming Laboratory in Bioinformatics course.
