# Epigenetic-Research-Synalpheus-Shrimp---2025
> A senior research project by **Philip Koutsaftis**  
> Advisor: Dr. Solomon Chak, Denison University

## 🧠 Project Summary

This project explores the role of epigenetics — specifically cytosine methylation at CpG sites — in the evolution of eusociality in *Synalpheus chacei*, a marine sponge-dwelling snapping shrimp. Eusociality in these shrimp evolved independently across species and is characterized by reproductive division of labor and cooperative brood care, similar to ants or bees.

Using Oxford Nanopore sequencing, we identify heavily methylated DNA regions and test their overlap with CpG islands and nearby genes, with the hypothesis that epigenetic regulation may drive gene expression differences linked to eusocial behavior.

---

## 🔬 Methods

### 1. **Nanopore Sequencing & Basecalling**
- Data from a single MinION run (25,728 reads)
- Used **Dorado** to basecall DNA and extract methylation tags:
  - **MM tags:** Mark modified cytosines
  - **ML tags:** Indicate probability of modification

### 2. **Methylation Analysis**
- Filtered for cytosine bases with >95% probability of methylation
- Computed proportion of methylated cytosines per sequence
- Identified top 10 sequences with highest methylation levels

### 3. **BLAST Search for Sequence Annotation**
- Ran BLASTn and BLASTx against:
  - `nr`: non-redundant nucleotide
  - `tsa_nr`: protein-translated transcriptome database
  - `core_nt`: curated nucleotide dataset
- Annotated high-methylation sequences to infer gene function

### 4. **CpG Island Detection** *(In Progress)*
- Using Python to scan the genome for:
  - ≥50% GC content
  - CpG Observed/Expected ratio ≥ 0.6
  - Length ≥ 200 bp

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


## 🧩 Goals

- [x] Extract MM/ML tags from MinION BAM files
- [x] Calculate methylation percentage per read
- [x] Annotate top mC sequences via BLAST
- [ ] Detect CpG islands
- [ ] Identify genes near methylated CpG islands
- [ ] Compare methylation patterns to social vs. non-social shrimp species

---

## 📂 Folder Structure

```bash
data/
  ├── raw/               # BAM, FASTQ from MinION
  └── processed/         # Trimmed methylation data
scripts/
  ├── basecalling/       # Dorado setup
  ├── methylation/       # Analysis in R/Python
  └── blast_annotation.R
results/
  ├── figures/
  └── tables/
