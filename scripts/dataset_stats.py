"""
dataset_stats.py — Dataset Statistics Generator
Subject 23: Paired Real-World Scene Change and No-Change Dataset

Generates statistics and distribution charts for the LaTeX report.
"""

import json
import csv
import os
import sys
from pathlib import Path
from collections import Counter

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False

ROOT = Path(__file__).resolve().parent.parent
FIGURES_DIR = ROOT / "report" / "figures"


def load_labels():
    """Load labels from labels.jsonl."""
    labels_path = ROOT / "annotations" / "labels.jsonl"
    if not labels_path.exists():
        print("ERROR: annotations/labels.jsonl not found")
        return []

    records = []
    with open(labels_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def print_stats(records):
    """Print dataset statistics to console."""
    print("\n" + "=" * 60)
    print("DATASET STATISTICS — Subject 23")
    print("=" * 60)

    total = len(records)
    changed = sum(1 for r in records if r.get("change_label") == "change")
    unchanged = sum(1 for r in records if r.get("change_label") == "no_change")
    verified = sum(1 for r in records if r.get("verified", False))

    print(f"\nTotal pairs:       {total}")
    print(f"  Changed:         {changed}")
    print(f"  Unchanged:       {unchanged}")
    print(f"  Verified:        {verified} ({100*verified/max(total,1):.1f}%)")

    # Change type distribution
    print("\nChange Type Distribution:")
    change_types = Counter(r.get("change_type") for r in records if r.get("change_label") == "change")
    for ct, count in change_types.most_common():
        print(f"  {ct}: {count}")

    # Scene category distribution
    print("\nScene Category Distribution:")
    scenes = Counter(r.get("scene_category") for r in records)
    for sc, count in scenes.most_common():
        print(f"  {sc}: {count}")

    # Illumination distribution
    print("\nIllumination (before) Distribution:")
    illum = Counter(r.get("illumination_before") for r in records)
    for il, count in illum.most_common():
        print(f"  {il}: {count}")

    # Illumination changed
    illum_changed = sum(1 for r in records if r.get("illumination_changed", False))
    print(f"\nPairs with illumination change: {illum_changed} ({100*illum_changed/max(total,1):.1f}%)")

    # Viewpoint shift
    print("\nViewpoint Shift Distribution:")
    vp = Counter(r.get("viewpoint_shift") for r in records)
    for v, count in vp.most_common():
        print(f"  {v}: {count}")

    # Quality flags
    all_flags = []
    for r in records:
        all_flags.extend(r.get("quality_flags", []))
    if all_flags:
        print("\nQuality Flags:")
        for flag, count in Counter(all_flags).most_common():
            print(f"  {flag}: {count}")
    else:
        print("\nQuality Flags: none reported")

    # Missing annotation rate
    missing = sum(1 for r in records
                  if r.get("change_label") == "change" and not r.get("change_mask_path"))
    print(f"\nMissing masks (changed pairs): {missing}")

    # Capture dates
    dates = Counter(r.get("capture_date") for r in records)
    print(f"\nCapture dates: {len(dates)} unique dates")
    for d, count in sorted(dates.items()):
        print(f"  {d}: {count} pairs")

    return {
        "total": total, "changed": changed, "unchanged": unchanged,
        "change_types": change_types, "scenes": scenes,
        "illumination": illum, "viewpoint": vp,
    }


def generate_charts(stats):
    """Generate distribution charts as PNG files."""
    if not HAS_MPL:
        print("\nWARNING: matplotlib not installed. Skipping chart generation.")
        print("Install with: pip install matplotlib")
        return

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Change vs No-Change pie chart
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.pie([stats["changed"], stats["unchanged"]],
           labels=["Changed", "Unchanged"],
           colors=["#e74c3c", "#2ecc71"],
           autopct="%1.1f%%", startangle=90)
    ax.set_title("Change vs No-Change Distribution")
    fig.savefig(FIGURES_DIR / "change_distribution.png", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved: change_distribution.png")

    # 2. Change type bar chart
    if stats["change_types"]:
        fig, ax = plt.subplots(figsize=(6, 4))
        types = list(stats["change_types"].keys())
        counts = list(stats["change_types"].values())
        ax.bar(types, counts, color=["#3498db", "#e67e22", "#9b59b6"])
        ax.set_title("Change Type Distribution")
        ax.set_ylabel("Count")
        fig.savefig(FIGURES_DIR / "change_type_distribution.png", dpi=150, bbox_inches="tight")
        plt.close()
        print(f"  Saved: change_type_distribution.png")

    # 3. Scene category bar chart
    if stats["scenes"]:
        fig, ax = plt.subplots(figsize=(8, 4))
        scenes = list(stats["scenes"].keys())
        counts = list(stats["scenes"].values())
        ax.barh(scenes, counts, color="#1abc9c")
        ax.set_title("Scene Category Distribution")
        ax.set_xlabel("Count")
        fig.savefig(FIGURES_DIR / "scene_distribution.png", dpi=150, bbox_inches="tight")
        plt.close()
        print(f"  Saved: scene_distribution.png")

    # 4. Illumination distribution
    if stats["illumination"]:
        fig, ax = plt.subplots(figsize=(6, 4))
        illum = list(stats["illumination"].keys())
        counts = list(stats["illumination"].values())
        ax.bar(illum, counts, color="#f39c12")
        ax.set_title("Illumination Condition Distribution")
        ax.set_ylabel("Count")
        plt.xticks(rotation=30, ha="right")
        fig.savefig(FIGURES_DIR / "illumination_distribution.png", dpi=150, bbox_inches="tight")
        plt.close()
        print(f"  Saved: illumination_distribution.png")


def main():
    records = load_labels()
    if not records:
        print("No records found. Run this script after creating labels.jsonl.")
        sys.exit(0)

    stats = print_stats(records)

    print("\nGenerating charts...")
    generate_charts(stats)

    print("\nDone.")


if __name__ == "__main__":
    main()
