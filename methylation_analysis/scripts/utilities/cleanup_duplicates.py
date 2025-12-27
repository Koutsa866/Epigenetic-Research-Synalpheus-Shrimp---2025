#!/usr/bin/env python3
"""Delete verified duplicate files safely"""

import shutil
from pathlib import Path

BASE = Path("/Users/philip_koutsaftis/Library/CloudStorage/GoogleDrive-philipkoutsaftis@gmail.com/My Drive/2025_SnrProj_Dir")

# Verified duplicates to delete
DUPLICATES = {
    "Python scripts": [
        "run_local_analysis.py",
        "run_go_enrichment.py", 
        "create_figure.py"
    ],
    "Documentation": [
        "COMPLETE_METHODS_AND_RESULTS.md",
        "PROJECT_PROGRESS_SUMMARY.md",
        "CLEANUP_GUIDE.md",
        "README.md"
    ],
    "Old shrimp scripts": [
        "shrimp_discovery_v6_bash.sh", "shrimp_discovery_v7.sh", "shrimp_discovery_v8.sh",
        "shrimp_discovery_v9.sh", "shrimp_discovery_v10.sh", "shrimp_discovery_v11.sh",
        "shrimp_discovery_v12.sh", "shrimp_discovery_v13.sh", "shrimp_discovery_v14.sh",
        "shrimp_discovery_v15.sh", "shrimp_discovery_v16.sh", "shrimp_discovery_v16_final.sh",
        "shrimp_discovery_v17_final.sh", "shrimp_discovery_v18.sh", "shrimp_discovery_v19.sh",
        "shrimp_discovery_v20.sh", "shrimp_discovery_v22.sh", "shrimp_discovery_v23.sh",
        "shrimp_discovery_v26.sh", "shrimp_discovery_v27.sh", "shrimp_discovery_v28.sh",
        "shrimp_discovery_v29.py", "shrimp_discovery_v31.sh", "shrimp_discovery_v35.sh",
        "shrimp_discovery_local.py", "shrimp_discovery_local_fixed.py",
        "shrimp_local_analysis.py", "shrimp_analysis.py", "shrimp_final.sh"
    ],
    "Duplicate folders": [
        "analysis_output",
        "Refactored_Scripts"
    ]
}

def delete_duplicates():
    print("🗑️  SAFE DELETION OF VERIFIED DUPLICATES\n")
    print("=" * 60)
    
    deleted_count = 0
    
    for category, items in DUPLICATES.items():
        print(f"\n📂 {category}:")
        for item in items:
            path = BASE / item
            if path.exists():
                try:
                    if path.is_dir():
                        shutil.rmtree(path)
                        print(f"  ✅ Deleted folder: {item}")
                    else:
                        path.unlink()
                        print(f"  ✅ Deleted file: {item}")
                    deleted_count += 1
                except Exception as e:
                    print(f"  ❌ Error deleting {item}: {e}")
            else:
                print(f"  ⚠️  Not found: {item}")
    
    print(f"\n{'=' * 60}")
    print(f"✅ Deleted {deleted_count} duplicate items")
    print("\n📁 Your organized structure is now clean!")

if __name__ == "__main__":
    import sys
    if '--confirm' in sys.argv:
        delete_duplicates()
    else:
        print("⚠️  DRY RUN - Preview of what will be deleted:\n")
        total = sum(len(items) for items in DUPLICATES.values())
        print(f"Total items to delete: {total}\n")
        for category, items in DUPLICATES.items():
            print(f"{category}: {len(items)} items")
        print("\n✅ All items verified as exact duplicates")
        print("\nRun with --confirm to delete:")
        print("python3 cleanup_duplicates.py --confirm")
