#!/usr/bin/env python3
"""Reorganize project directory structure"""

import shutil
from pathlib import Path

BASE = Path("/Users/philip_koutsaftis/Library/CloudStorage/GoogleDrive-philipkoutsaftis@gmail.com/My Drive/2025_SnrProj_Dir")

# Define new structure
NEW_STRUCTURE = {
    "data/genome": ["Data/assembly.fasta", "Data/contig_sizes.txt", "Data/Contig_Lengths_Sheets2.csv"],
    "data/methylation": ["Data/bedmethyl_50p_mC_cov30.bed", "Data/methylation_sorted.bed"],
    "data/cpg_islands": ["Data/cpg_islands_sorted.bed"],
    "data/databases": ["uniprot_sprot.fasta", "Refactored_Scripts/uniprot_sprot.fasta"],
    
    "scripts/01_gene_prediction": ["Refactored_Scripts/augustus_run_s2.py"],
    "scripts/02_feature_extraction": ["Refactored_Scripts/bed_files_processing.py"],
    "scripts/03_functional_annotation": ["run_local_analysis.py", "run_go_enrichment.py", 
                                         "Refactored_Scripts/blastp_analysis.py",
                                         "Refactored_Scripts/functional_annotation_prep.py"],
    "scripts/04_visualization": ["create_figure.py"],
    "scripts/utilities": ["Refactored_Scripts/ContigStats_refactored.py", 
                         "Refactored_Scripts/auto_github_sync.py"],
    
    "scripts_hpc": ["shrimp_final.sh", "shrimp_discovery_v31.sh", "shrimp_analysis.py"],
    
    "notebooks": ["Scripts/promoter_cpgIsland_file_processing.ipynb", 
                  "Scripts/S_elizabithae_AUGUSTUS.ipynb"],
    
    "results/01_gene_prediction/augustus_output": ["Results/augustus_output"],
    "results/01_gene_prediction/bed_files": ["Results/augustus_gene_bed_files"],
    "results/02_genomic_features": ["Results/strand_aware_bed"],
    "results/03_methylation_analysis": [
        "Results/genes_with_high_methylated_promoters.tsv",
        "Results/genes_without_methylated_promoters.tsv",
        "Results/high_methylated_cpg_islands.bed",
        "Results/promoter_high_methyl_cpg_overlap.bed",
        "Results/promoter_high_methyl_cpg_overlap.tsv",
        "Results/filtered_bedmethyl_50p_cov30.csv"
    ],
    "results/04_functional_annotation": [
        "analysis_output/gene_uniprot_mapping.csv",
        "analysis_output/go_enrichment_results.csv",
        "analysis_output/diamond_results.tsv"
    ],
    "results/05_figures": ["analysis_output/go_enrichment_chart.png"],
    
    "docs": ["COMPLETE_METHODS_AND_RESULTS.md", "PROJECT_PROGRESS_SUMMARY.md", 
             "README.md", "CLEANUP_GUIDE.md"],
    
    "archive/old_scripts": [f"shrimp_discovery_v{i}.sh" for i in [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,26,27,28,29,35]] + 
                           ["shrimp_discovery_v16_final.sh", "shrimp_discovery_v17_final.sh",
                            "shrimp_discovery_local.py", "shrimp_discovery_local_fixed.py",
                            "shrimp_local_analysis.py", "shrimp_discovery_v29.py"],
    "archive/old_results": ["results (1)", "contig_trim_v1"],
    "archive/old_folders": ["2025_SnrProj_Synalpheus", "bam2hints", "synalpheus_epigenetics",
                           "Transcriptome_Alignments", "PreogressRepos", "Scripts/ContigScripts_refactored"]
}

def reorganize():
    print("🔄 Starting reorganization...\n")
    
    # Create new directories
    for new_dir in NEW_STRUCTURE.keys():
        (BASE / new_dir).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created: {new_dir}/")
    
    # Move files
    moved = 0
    for dest_dir, sources in NEW_STRUCTURE.items():
        for src in sources:
            src_path = BASE / src
            if src_path.exists():
                dest_path = BASE / dest_dir / src_path.name
                try:
                    if src_path.is_dir():
                        if not dest_path.exists():
                            shutil.move(str(src_path), str(dest_path))
                            print(f"  📁 {src} → {dest_dir}/")
                            moved += 1
                    else:
                        shutil.copy2(str(src_path), str(dest_path))
                        print(f"  📄 {src} → {dest_dir}/")
                        moved += 1
                except Exception as e:
                    print(f"  ⚠️  Error moving {src}: {e}")
    
    print(f"\n✅ Reorganization complete! Moved {moved} items.")
    print("\n⚠️  IMPORTANT: Original files still exist. Review new structure, then manually delete old files.")
    
    # Print new structure
    print("\n📂 NEW STRUCTURE:")
    print("="*60)
    for root, dirs, files in sorted(Path(BASE).walk()):
        level = len(root.relative_to(BASE).parts)
        if level <= 2 and not any(x in str(root) for x in ['archive', '.git', '__pycache__']):
            indent = '  ' * level
            print(f"{indent}{root.name}/")
            if level == 2:
                file_count = len([f for f in files if not f.startswith('.')])
                if file_count > 0:
                    print(f"{indent}  ({file_count} files)")

if __name__ == "__main__":
    import sys
    if '--confirm' in sys.argv:
        reorganize()
    else:
        print("⚠️  DRY RUN - No files will be moved")
        print("\nThis will reorganize:")
        total = sum(len(sources) for sources in NEW_STRUCTURE.values())
        print(f"  • {total} files/folders")
        print(f"  • Into {len(NEW_STRUCTURE)} new directories")
        print("\nRun with --confirm to execute")
        print("Example: python3 reorganize_project.py --confirm")
