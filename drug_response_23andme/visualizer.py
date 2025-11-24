import matplotlib.pyplot as plt
import pandas as pd

def plot_stats(df, output_prefix="plot"):
    """
    Generates histograms for drugs/gene and SNPs/gene.
    
    Args:
        df (pd.DataFrame): The filtered DataFrame.
        output_prefix (str): Prefix for saved plot files.
    """
    if df.empty:
        print("No data to plot.")
        return

    # 1. Number of drugs per gene
    if "GENE_SYMBOL" in df.columns and "DRUG_NAME" in df.columns:
        drugs_per_gene = df.groupby("GENE_SYMBOL")["DRUG_NAME"].nunique()
        
        plt.figure(figsize=(6,4))
        plt.hist(drugs_per_gene, bins=20, color='skyblue', edgecolor='black')
        plt.xlabel("# of drugs associated per gene")
        plt.ylabel("Number of genes")
        plt.title("Distribution of drugs per gene")
        plt.tight_layout()
        plt.savefig(f"{output_prefix}_drugs_per_gene.png")
        plt.close()
        print(f"Saved {output_prefix}_drugs_per_gene.png")

    # 2. Number of SNPs per gene
    if "GENE_SYMBOL" in df.columns and "dbSNP_ID" in df.columns:
        snps_per_gene = df.groupby("GENE_SYMBOL")["dbSNP_ID"].nunique()
        
        plt.figure(figsize=(6,4))
        plt.hist(snps_per_gene, bins=20, color='salmon', edgecolor='black')
        plt.xlabel("# of SNPs per gene")
        plt.ylabel("Number of genes")
        plt.title("Distribution of SNPs per gene")
        plt.tight_layout()
        plt.savefig(f"{output_prefix}_snps_per_gene.png")
        plt.close()
        print(f"Saved {output_prefix}_snps_per_gene.png")
