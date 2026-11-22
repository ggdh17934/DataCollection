"""
deduplicate.py — Duplicate Detection Script
Subject 23: Paired Real-World Scene Change and No-Change Dataset

Uses perceptual hashing (pHash) to find near-duplicate images.
"""

import os
import sys
from pathlib import Path
from collections import defaultdict

try:
    from PIL import Image
    import imagehash
    HAS_DEPS = True
except ImportError:
    HAS_DEPS = False

ROOT = Path(__file__).resolve().parent.parent


def compute_phash(image_path, hash_size=8):
    """Compute perceptual hash for an image."""
    with Image.open(image_path) as img:
        return imagehash.phash(img, hash_size=hash_size)


def find_duplicates(threshold=10):
    """Find near-duplicate images using perceptual hashing."""
    img_dirs = [
        ROOT / "data" / "originals" / "changed",
        ROOT / "data" / "originals" / "unchanged",
    ]

    hashes = {}
    print("Computing perceptual hashes...")

    for img_dir in img_dirs:
        if not img_dir.exists():
            print(f"  Directory not found: {img_dir}")
            continue
        for img_file in sorted(img_dir.glob("*.jpg")):
            try:
                h = compute_phash(img_file)
                hashes[img_file] = h
            except Exception as e:
                print(f"  ERROR hashing {img_file.name}: {e}")

    if not hashes:
        print("No images found to check.")
        return []

    print(f"Computed hashes for {len(hashes)} images.")

    # Find pairs with hamming distance below threshold
    files = list(hashes.keys())
    duplicates = []

    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            dist = hashes[files[i]] - hashes[files[j]]
            if dist < threshold:
                # Skip before/after pairs from the same pair_id (they're supposed to be similar)
                name_i = files[i].stem
                name_j = files[j].stem
                base_i = name_i.rsplit("_", 1)[0]  # e.g., CV26_S23_P001
                base_j = name_j.rsplit("_", 1)[0]
                if base_i == base_j:
                    continue  # Same pair, skip

                duplicates.append((files[i].name, files[j].name, dist))

    return duplicates


def main():
    print("=" * 60)
    print("Duplicate Detection — Subject 23")
    print("=" * 60)

    if not HAS_DEPS:
        print("\nERROR: Required packages not installed.")
        print("Install with: pip install Pillow imagehash")
        sys.exit(1)

    duplicates = find_duplicates(threshold=10)

    if duplicates:
        print(f"\nFound {len(duplicates)} potential duplicate pairs:\n")
        print(f"{'Image A':<35} {'Image B':<35} {'Distance':>8}")
        print("-" * 80)
        for img_a, img_b, dist in sorted(duplicates, key=lambda x: x[2]):
            print(f"{img_a:<35} {img_b:<35} {dist:>8}")

        # Save report
        report_path = ROOT / "quality" / "duplicate_report.csv"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("image_a,image_b,hamming_distance\n")
            for img_a, img_b, dist in duplicates:
                f.write(f"{img_a},{img_b},{dist}\n")
        print(f"\nReport saved to: {report_path}")
    else:
        print("\nNo duplicates found.")

    print("\nDone.")


if __name__ == "__main__":
    main()
