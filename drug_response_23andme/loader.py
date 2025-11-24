import pandas as pd
from io import StringIO

def load_23andme(file_path):
    """
    Loads and cleans 23andMe raw data file.
    
    Args:
        file_path (str): Path to the 23andMe txt file.
        
    Returns:
        pd.DataFrame: Cleaned DataFrame with columns [CHR, POS, dbSNP_ID, ALLELE_23andme]
    """
    # Read file, skipping comments
    df = pd.read_csv(
        file_path,
        sep="\t",
        comment='#',
        header=None,
        names=["CHR", "POS", "dbSNP_ID", "ALLELE_23andme"],
        dtype=str
    )
    
    # Drop rows missing rsIDs (some entries have i###### codes)
    df = df[df["dbSNP_ID"].str.startswith("rs", na=False)].copy()
    
    return df

def load_pharmgkb(file_path):
    """
    Loads and cleans PharmGKB variant annotation file.
    
    Args:
        file_path (str): Path to the PharmGKB tsv file.
        
    Returns:
        pd.DataFrame: Cleaned DataFrame with standardized columns.
    """
    # Skip the single bad line containing “The 15-year cumulative” if it exists
    # This is specific to the user's notebook logic
    lines_clean = []
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            if "The 15-year cumulative" in line:
                continue
            lines_clean.append(line)

    df = pd.read_csv(StringIO("".join(lines_clean)), sep="\t", dtype=str, low_memory=False)

    # Select & rename relevant columns
    col_map = {
        "Variant/Haplotypes": "dbSNP_ID",
        "Gene": "GENE_SYMBOL",
        "Drug(s)": "DRUG_NAME",
        "PMID": "PMID",
        "Phenotype Category": "PHENOTYPE_CATEGORY",
        "Significance": "SIGNIFICANCE",
        "Notes": "NOTES",
        "Sentence": "SENTENCE",
        "Alleles": "ALLELE_PharmGKB",
    }

    # Check if columns exist before selecting
    available_cols = [c for c in col_map.keys() if c in df.columns]
    df = df[available_cols].rename(columns=col_map)

    # Keep only rows with valid rsIDs
    if "dbSNP_ID" in df.columns:
        df = df[df["dbSNP_ID"].str.fullmatch(r"rs\d+", na=False)].copy()

    return df
