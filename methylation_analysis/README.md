# Methylation Analysis Pipeline

Complete bioinformatics pipeline for DNA methylation analysis in *Synalpheus chacei*.

## Directory Structure

### `/scripts/`
- **`gene_prediction/`** - AUGUSTUS gene calling
- **`feature_extraction/`** - BED file processing and genomic features
- **`functional_annotation/`** - DIAMOND, BLAST, and GO enrichment
- **`visualization/`** - All plotting and figure generation scripts
- **`utilities/`** - Helper scripts and data processing tools

### `/notebooks/`
- **`promoter_cpg_analysis.ipynb`** - Interactive CpG island analysis
- **`augustus_analysis.ipynb`** - Gene prediction workflow

### `/results/`
- **`figures/`** - Publication-ready analysis figures
- **`poster_figures/`** - PAG33 conference poster materials

### `/docs/`
- **`PAG33_final_poster.pdf`** - Conference presentation
- **`PAG33_poster_alt.pdf`** - Alternative poster version

## Key Results
- 6,848 genes predicted via AUGUSTUS
- 1,103 genes (16.1%) with methylated promoters  
- 77.4% of annotated methylated genes are transposable elements
- p = 3.9×10⁻¹³ for DNA binding enrichment

## Usage
1. Install requirements: `pip install -r requirements.txt`
2. Run setup: `bash setup_analysis.sh`
3. Execute pipeline scripts in order
4. Generate figures using visualization scripts
