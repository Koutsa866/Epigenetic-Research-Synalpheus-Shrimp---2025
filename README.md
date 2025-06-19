# Epigenetic-Research-Synalpheus-Shrimp---2025
> A senior research project by **Philip Koutsaftis**  
> Advisor: Dr. Solomon Chak, Denison University

## 🧠 Project Summary

This project explores the role of epigenetics — specifically cytosine methylation at CpG sites — in the evolution of eusociality in *Synalpheus chacei*, a marine sponge-dwelling snapping shrimp. Eusociality in these shrimp evolved independently across species and is characterized by reproductive division of labor and cooperative brood care, similar to ants or bees.

Oxford Nanopore sequencing and computational analysis are used to:
- Detect highly methylated DNA regions
- Identify and annotate CpG islands
- Investigate the proximity of these islands to functionally relevant genes


---

## 🔬 Methods Overview

### 1. 🧪 Nanopore Sequencing & Basecalling
- Sequenced on Oxford Nanopore MinION (~25,700 reads)
- Used **Dorado** for basecalling and to extract methylation-related tags:
  - `MM`: modified base location
  - `ML`: probability of modification

### 2. 🧮 Methylation Processing
- Script: `Shrimp_Proj2025.py`
- Filters reads for high-confidence methylated cytosines (>95%)
- Computes per-read methylation percentages
- Extracts and outputs top 10 most-methylated sequences for BLAST analysis

### 3. 🔍 CpG Island Detection
- Script: `map_methylation_to_cpg.py`
- Custom Python script identifies CpG islands by:
  - %GC ≥ 50%
  - Obs/Exp CpG ratio ≥ 0.6
  - Length ≥ 200 bp
- Output stored as BED format

### 4. 🧬 Mapping CpG Islands to Methylation
- Script: `run_methylation_mapping.sh`
- Uses `bedtools map` to compute average methylation over CpG islands
- Preparing for downstream analysis of gene proximity

---

## 📊 Results Summary

- **Median read length:** 2,561 bp (range: 5–38,026 bp)
- **82%** of reads contained ≥1 high-confidence methylated cytosine
- **Median methylation proportion:** 0.006
- Some sequences had **>10%** mC, possibly within CpG islands

---

## 🔭 Current Research

Future work will expand this study in the following ways:
	•	Genome-Wide CpG Mapping: Identify and annotate CpG islands across the Synalpheus chacei genome and integrate methylation data to locate regulatory hotspots.
	•	Gene Association: Link highly methylated CpG islands to nearby genes, especially those related to reproduction, development, or behavior.
	•	Comparative Epigenetics: Compare methylation patterns between eusocial and non-eusocial Synalpheus species to identify epigenetic signatures of eusociality.
	•	Functional Insights: Analyze whether methylation may block transcription factor binding or regulate gene expression.
	•	Improved Data Resolution: Use additional MinION runs, align reads to a reference genome, and refine filtering for high-confidence calls.

---


## 🧩 Progress Checklist

- [x] Extracted MM/ML tags from MinION data
- [x] Calculated per-read methylation
- [x] BLASTed top methylated sequences
- [x] Identified CpG islands
- [x] Mapped methylation levels to CpG islands
- [ ] Link CpG islands to nearby genes (in progress)
- [ ] Functional annotation of associated genes
- [ ] Compare eusocial vs. non-eusocial methylation patterns (planned)

---

## 🔭 Future Work

- Map CpG islands to nearby genes using GFF annotations
- Analyze enrichment of functional categories (e.g., behavior, reproduction)
- Compare across *Synalpheus* species with differing social structures
- Add visualizations of methylation across genome

---

## 📈 Tools & Software Used

| Tool         | Purpose                          |
|--------------|----------------------------------|
| Dorado       | Basecalling + methylation calling |
| Python       | CpG scanning, filtering, analysis |
| R / Bash     | Data wrangling, visualization     |
| bedtools     | Genomic region mapping            |
| BLASTn/x     | Sequence annotation               |

---

## 📂 Folder Structure

```bash
2025_SnrProj_Synalpheus/
├── Scripts/
│   ├── Shrimp_Proj2025.py
│   ├── map_methylation_to_cpg.py
│   └── run_methylation_mapping.sh
├── data/
│   ├── raw/               # BAM, bedmethyl, readstats
│   └── processed/         # filtered_methylation.tsv, CpG island BED
├── results/
│   ├── tables/            # top10 BLAST hits, CpG-methylation mapping
│   └── figures/           # optional future visualizations
├── README.md
