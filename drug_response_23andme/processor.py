import pandas as pd

def merge_data(df_23, df_ann):
    """
    Merges 23andMe data with PharmGKB annotations on dbSNP_ID.
    
    Args:
        df_23 (pd.DataFrame): 23andMe data.
        df_ann (pd.DataFrame): PharmGKB data.
        
    Returns:
        pd.DataFrame: Merged DataFrame.
    """
    # Merge with 23andMe
    df_merge = df_ann.merge(df_23[["dbSNP_ID", "ALLELE_23andme"]], on="dbSNP_ID", how="inner")
    
    # Reorder columns if they exist
    cols = [
        "dbSNP_ID", "GENE_SYMBOL", "DRUG_NAME", "PMID",
        "PHENOTYPE_CATEGORY", "SIGNIFICANCE", "NOTES", "SENTENCE",
        "ALLELE_PharmGKB", "ALLELE_23andme"
    ]
    existing_cols = [c for c in cols if c in df_merge.columns]
    
    return df_merge[existing_cols]

def filter_significant_efficacy(df):
    """
    Filters for significant efficacy variants.
    
    Args:
        df (pd.DataFrame): Merged DataFrame.
        
    Returns:
        pd.DataFrame: Filtered DataFrame.
    """
    if "SIGNIFICANCE" not in df.columns or "PHENOTYPE_CATEGORY" not in df.columns:
        return df
        
    df_sig_eff = df[
        (df["SIGNIFICANCE"].str.lower() == "yes") &
        (df["PHENOTYPE_CATEGORY"].str.lower() == "efficacy")
    ].copy()
    
    return df_sig_eff

def summarize_data(df):
    """
    Creates a summary of drugs per gene.
    
    Args:
        df (pd.DataFrame): Filtered DataFrame.
        
    Returns:
        pd.DataFrame: Summary DataFrame with columns [GENE_SYMBOL, DRUG_NAME, dbSNP_IDs]
    """
    if "GENE_SYMBOL" not in df.columns or "DRUG_NAME" not in df.columns:
        return pd.DataFrame()

    summary = (
        df.groupby(["GENE_SYMBOL", "DRUG_NAME"])["dbSNP_ID"]
        .apply(lambda s: ";".join(sorted(set(s))))
        .reset_index(name="dbSNP_IDs")
    )
    return summary
