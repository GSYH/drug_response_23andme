# Drug Response 23andMe

![Python 3.6+](https://img.shields.io/badge/python-3.6%2B-blue)
![License MIT](https://img.shields.io/badge/license-MIT-green)
[![Documentation](https://img.shields.io/badge/docs-gh--pages-blue)](https://GSYH.github.io/drug_response_23andme/)

**Drug Response 23andMe** is a Python package for annotating 23andMe raw genotype data with drug response information from the PharmGKB database. It automates the parsing of genotype files, integrates variant annotations, and identifies significant efficacy variants relevant to the user.

**Website:** [https://GSYH.github.io/drug_response_23andme/](https://GSYH.github.io/drug_response_23andme/)

> [!NOTE]
> **Scope & Limitations:**
>
> *   **Input Data**: Designed for **23andMe raw data (v5)** text files.
> *   **Annotation Source**: Uses **PharmGKB variant annotations** (`var_drug_ann.tsv`).
> *   **Focus**: Primarily filters for **Significant Efficacy** variants to provide actionable insights.

This tool is designed for bioinformatics students and researchers who want to explore pharmacogenomics using personal genetic data.

## Installation

You can install `drug_response_23andme` directly from GitHub using `pip`.

### Option 1: Install from GitHub (Recommended)

To install the latest version of the package:

```bash
pip install git+https://github.com/GSYH/drug_response_23andme.git
```

### Option 2: Clone and Install

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
