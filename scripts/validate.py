"""
validate.py — Dataset Validation Script
Subject 23: Paired Real-World Scene Change and No-Change Dataset

Validates:
1. All files in manifest.csv exist on disk
2. labels.jsonl conforms to annotation_schema.json
3. Changed pairs have masks; unchanged pairs have null masks
4. SHA-256 checksums match
5. No corrupted/unreadable images
6. No conflicting IDs
"""

import json
import csv
import hashlib
import os
import sys
from pathlib import Path

# Try to import PIL for image validation
try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("WARNING: Pillow not installed. Skipping image corruption checks.")

ROOT = Path(__file__).resolve().parent.parent
ERRORS = []
WARNINGS = []


def error(msg):
    ERRORS.append(msg)
    print(f"  ERROR: {msg}")


def warn(msg):
    WARNINGS.append(msg)
    print(f"  WARN:  {msg}")


def ok(msg):
    print(f"  OK:    {msg}")


def validate_manifest():
    """Check that all files referenced in manifest.csv exist."""
    print("\n=== Validating manifest.csv ===")
    manifest_path = ROOT / "metadata" / "manifest.csv"
    if not manifest_path.exists():
        error("metadata/manifest.csv not found")
        return

    with open(manifest_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if len(rows) == 0:
        warn("manifest.csv is empty (no data rows yet)")
        return

    pair_ids = set()
    for row in rows:
        pid = row.get("pair_id", "")
        if pid in pair_ids:
            error(f"Duplicate pair_id in manifest: {pid}")
        pair_ids.add(pid)

        for col in ["before_path", "after_path"]:
            path = row.get(col, "")
            if path and not (ROOT / path).exists():
                error(f"File not found for {pid}.{col}: {path}")

    ok(f"Manifest contains {len(rows)} pairs, {len(pair_ids)} unique IDs")


def validate_labels():
    """Check labels.jsonl against the annotation schema."""
    print("\n=== Validating labels.jsonl ===")
    labels_path = ROOT / "annotations" / "labels.jsonl"
    schema_path = ROOT / "annotations" / "annotation_schema.json"

    if not labels_path.exists():
        warn("annotations/labels.jsonl not found (not created yet)")
        return
    if not schema_path.exists():
        error("annotations/annotation_schema.json not found")
        return

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    required_fields = [
        k for k, v in schema["fields"].items()
        if isinstance(v, dict) and v.get("required", False)
    ]

    pair_ids = set()
    line_count = 0
    change_count = 0
    nochange_count = 0

    with open(labels_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as e:
                error(f"Invalid JSON on line {i}: {e}")
                continue

            line_count += 1
            pid = record.get("pair_id", f"UNKNOWN_LINE_{i}")

            # Check required fields
            for field in required_fields:
                if field not in record:
                    error(f"{pid}: missing required field '{field}'")

            # Check pair_id uniqueness
            if pid in pair_ids:
                error(f"Duplicate pair_id: {pid}")
            pair_ids.add(pid)

            # Check change/no-change consistency
            label = record.get("change_label")
            if label == "change":
                change_count += 1
                if not record.get("change_mask_path"):
                    warn(f"{pid}: changed pair missing change_mask_path")
                if not record.get("change_region_box"):
                    warn(f"{pid}: changed pair missing change_region_box")
                if not record.get("change_type"):
                    error(f"{pid}: changed pair missing change_type")
            elif label == "no_change":
                nochange_count += 1
                if record.get("change_mask_path"):
                    error(f"{pid}: no-change pair should not have a mask")
                if record.get("change_region_box"):
                    error(f"{pid}: no-change pair should not have a region box")
            else:
                error(f"{pid}: invalid change_label '{label}'")

            # Check image files exist
            for img_field in ["before_image", "after_image"]:
                img_path = record.get(img_field, "")
                if img_path and not (ROOT / img_path).exists():
                    error(f"{pid}: {img_field} file not found: {img_path}")

            # Check mask file exists (for changed pairs)
            mask_path = record.get("change_mask_path")
            if mask_path and not (ROOT / mask_path).exists():
                error(f"{pid}: mask file not found: {mask_path}")

    ok(f"Processed {line_count} records: {change_count} changed, {nochange_count} unchanged")


def validate_checksums():
    """Verify SHA-256 checksums."""
    print("\n=== Validating checksums ===")
    checksum_path = ROOT / "metadata" / "checksums.sha256"
    if not checksum_path.exists():
        warn("metadata/checksums.sha256 not found (not generated yet)")
        return

    mismatch = 0
    missing = 0
    verified = 0

    with open(checksum_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("  ", 1)
            if len(parts) != 2:
                warn(f"Malformed checksum line: {line}")
                continue
            expected_hash, filepath = parts
            full_path = ROOT / filepath
            if not full_path.exists():
                error(f"Checksum file not found: {filepath}")
                missing += 1
                continue
            sha256 = hashlib.sha256()
            with open(full_path, "rb") as fh:
                for chunk in iter(lambda: fh.read(8192), b""):
                    sha256.update(chunk)
            if sha256.hexdigest() != expected_hash:
                error(f"Checksum mismatch: {filepath}")
                mismatch += 1
            else:
                verified += 1

    ok(f"Checksums: {verified} verified, {mismatch} mismatches, {missing} missing files")


def validate_images():
    """Check for corrupted images."""
    print("\n=== Validating images ===")
    if not HAS_PIL:
        warn("Skipping image validation (Pillow not installed)")
        return

    img_dirs = [
        ROOT / "data" / "originals" / "changed",
        ROOT / "data" / "originals" / "unchanged",
    ]

    total = 0
    corrupted = 0
    for img_dir in img_dirs:
        if not img_dir.exists():
            continue
        for img_file in img_dir.glob("*.jpg"):
            total += 1
            try:
                with Image.open(img_file) as img:
                    img.verify()
            except Exception as e:
                error(f"Corrupted image: {img_file.name} — {e}")
                corrupted += 1

    ok(f"Checked {total} images, {corrupted} corrupted")


def main():
    print("=" * 60)
    print("Dataset Validation — Subject 23")
    print("=" * 60)

    validate_manifest()
    validate_labels()
    validate_checksums()
    validate_images()

    print("\n" + "=" * 60)
    print(f"SUMMARY: {len(ERRORS)} errors, {len(WARNINGS)} warnings")
    print("=" * 60)

    if ERRORS:
        print("\nFailed validation. Fix errors above.")
        sys.exit(1)
    else:
        print("\nAll checks passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()
