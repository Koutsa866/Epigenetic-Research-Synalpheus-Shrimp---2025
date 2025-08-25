# Epigenetic•Research•Synalpheus•Shrimp•••2025
> A senior research project by **Philip Koutsaftis**  
> Advisor: Dr. Solomon Chak, Denison University

##  Project Summary

This project investigates the epigenetic basis of eusociality in Synalpheus chacei, a sponge•dwelling snapping shrimp that exhibits complex social behaviors, including reproductive division of labor and cooperative brood care—traits that have independently evolved multiple times within this genus.

Focusing on DNA methylation at CpG islands, we explore how epigenetic modifications may regulate gene expression patterns associated with eusocial traits. Using Oxford Nanopore sequencing data, we identify heavily methylated regions across the genome and assess their overlap with CpG islands and nearby genes. We hypothesize that methylated CpG islands located near regulatory regions influence the expression of genes critical to social structure and division of labor. This work aims to uncover novel molecular mechanisms underlying social evolution in marine invertebrates and broaden our understanding of epigenetic regulation beyond traditional model organisms.

---

## Methods (Section 1 - Summer 2024)

### 1. Nanopore Sequencing and Methylation Tag Extraction**
• Sequenced DNA with Oxford Nanopore MinION
• Used **Dorado** for basecalling and extraction of:
  • **MM tags** (locations of modified cytosines)
  • **ML tags** (corresponding probabilities of methylation)
• Filtered for methylation probabilities >95%

### 2. Methylation Quantification and BLAST Annotation (Summer 2024)
• Extracted MM and ML tags from basecalled Nanopore data to identify methylated cytosines
• Used R to calculate the proportion of methylated cytosines per read and to summarize methylation distributions across all reads
• Filtered for high•confidence methylation events by retaining only reads with ≥95% probability of methylation
• Identified the top 10 reads with the highest methylation levels (up to ~10%)
 Hypothesized that these highly methylated reads may overlap CpG islands or gene regulatory regions
• Annotated these sequences using BLASTn and BLASTx against the nr, tsa_nr, and core_nt databases
• Interpreted BLAST hits to evaluate possible gene functions and potential roles in eusocial traits

## Methods  (Section 2 - Summer 2025 - Present)

### 3. **CpG Island Detection and Methylation Overlay**

Developed a custom Python script to scan the Synalpheus chacei genome and detect CpG islands using the following criteria:
	•	GC content ≥ 50%
	•	Observed/Expected CpG ratio ≥ 0.6
	•	Minimum length ≥ 200 bp
	•	Extracted MM (modified base locations) and ML (methylation probabilities) tags from Nanopore reads and overlaid these data onto the CpG island coordinates.
	•	Used Python to quantify methylation levels within each CpG island:
	•	Percentage of methylated CpG cytosines per island — [insert final value or describe distribution]
	•	Percentage of total bases methylated across each island — [insert final value or describe distribution]
	•	Applied a methylation threshold of ≥70% methylated CpG sites to classify CpG islands as methylated or unmethylated for downstream regulatory analysis.
	•	Summary statistics:
	•	Total CpG islands detected: 5,427,765
	•	Methylated CpG islands (≥70%): 5,123,226
	•	Proportion of islands classified as methylated: 94.4%


  ### 4. **Genome Chunking and Gene Prediction**
• Split genome assembly into 2,800+ contigs
• Organized into 56 batches of 50 files each (`contigs_batch_1` to `contigs_batch_56`)
• Ran **AUGUSTUS** gene prediction (via bash in Google Colab) on all batches using:
  ```
  ••species=fly
  ••gff3=on
  ••UTR=on
  ••print_utr=on
  ••protein=on
  ```
• Output: ~2,800 `.gff` files stored in batch•labeled folders in `augustus_output/`

### 5. **Gene•CpG Island Association** *(Next Step)*
• Convert `.gff` predictions to `.bed` format
• Use **BEDTools** to identify genes overlapping or near methylated CpG islands
• Goal: Identify potential regulatory relationships

### 6. **Gene Annotation and Functional Insights** *(Upcoming)*
• Annotate predicted genes using **eggNOG•mapper** or **InterProScan**
• Perform **GO enrichment** to detect overrepresented functions
• Visualize results with **IGV** or **UCSC Genome Browser**

### 7. **Machine Learning Model (Exploratory)**
• Use **H2O AutoML** to predict gene methylation status from features:
  • CpG island features
  • Distance to gene TSS
  • Island length, GC content, etc.

---

##  Results Summary

• Median read length: 2,561 bp (range: 5–38,026 bp)
• 82% of reads contained ≥1 high•confidence methylated cytosine
• Median methylation proportion: 0.006
• Some sequences had >10% mC, possibly within CpG islands
• Top 10 methylated reads were annotated using BLAST and found to contain hits to genes with possible regulatory or functional roles
• Total CpG islands identified genome•wide: 5,423,765
• Methylated CpG islands (≥70% methylation threshold): 5,123,226
• Proportion of methylated CpG islands: 94.46%
• These CpG island metrics were derived after integrating methylation call data with CpG island locations, supporting the hypothesis that widespread methylation may influence gene regulation in Synalpheus chacei.

---

##  Completed Milestones

• [x] Nanopore methylation tag extraction
• [x] Genome chunking into 2,800+ contigs
• [x] Ran AUGUSTUS on all 56 contig batches
• [x] Saved all GFF outputs to Google Drive
• [x] Identified CpG islands with Python
• [x] Mapped methylation to CpG islands
• [x] Classified CpG islands by methylation status

---

##  In Progress / Upcoming

• [ ] Convert `.gff` to `.bed` for genes
• [ ] Use BEDTools to find CpG–gene overlaps
• [ ] Annotate genes with eggNOG or InterProScan
• [ ] Perform GO enrichment analysis
• [ ] Visualize gene/CpG/methylation data
• [ ] Train predictive ML models on CpG–gene associations

---

##  Folder Structure

```
/2025_SnrProj_Dir/
│
├── contigs/
│   ├── contigs_batch_1/ to contigs_batch_56/
│   └── each contains 50 FASTA files per contig
│
├── augustus_output/
│   ├── augustus_batch1/ to augustus_batch56/
│   └── each contains GFF files from AUGUSTUS
│
├── methylation_data/
│   ├── filtered_mm_ml_tags.csv
│   └── methylation_summary_per_island.csv
│
├── scripts/
│   ├── chunking_genome.py
│   ├── run_augustus.sh
│   ├── detect_cpg_islands.py
│   └── intersect_genes_with_cpg.py
│
└── results/
    ├── gene_annotation/
    ├── plots/
    └── GO_enrichment/
```

---

##  Research Significance

This is one of the first genome•wide studies of DNA methylation in a eusocial marine invertebrate. By integrating methylation data, CpG island detection, gene prediction, and functional annotation, this research sheds light on the epigenetic regulation of complex social behavior in a non•insect system.

---

##  References

• Dorado basecaller: Oxford Nanopore Technologies
• AUGUSTUS gene prediction: Stanke et al. (2004)
• BEDTools: Quinlan and Hall (2010)
• eggNOG•mapper: Huerta•Cepas et al. (2017)

---

*Updated: July 3, 2025*
