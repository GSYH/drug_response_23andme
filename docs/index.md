# Drug Response 23andMe

![Python 3.6+](https://img.shields.io/badge/python-3.6%2B-blue)
![License MIT](https://img.shields.io/badge/license-MIT-green)
[![Documentation](https://img.shields.io/badge/docs-gh--pages-blue)](https://GSYH.github.io/drug_response_23andme/)

**Drug Response 23andMe** is a Python package for annotating 23andMe raw genotype data with drug response information from the PharmGKB database. It automates the parsing of genotype files, integrates variant annotations, and identifies significant efficacy variants relevant to the user.

!!! note "Scope & Limitations"
    *   **Input Data**: Designed for **23andMe raw data (v5)** text files.
    *   **Annotation Source**: Uses **PharmGKB variant annotations** (`var_drug_ann.tsv`).
    *   **Focus**: Primarily filters for **Significant Efficacy** variants to provide actionable insights.

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

## Features

*   **Load 23andMe Data**: Easily parse your raw 23andMe text file.
*   **Load PharmGKB Data**: Import variant annotations from PharmGKB.
*   **Merge & Filter**: Combine datasets to find significant efficacy variants relevant to your genotype.
*   **Visualize**: Generate plots showing the distribution of drugs and SNPs per gene.
