# Quality Control Report

## Subject 23: Paired Real-World Scene Change and No-Change Dataset

*This report will be completed during Week 5 (audit phase).*

---

## 1. Sample Counts

| Metric | Count |
|--------|-------|
| Total image pairs | — |
| Usable image pairs | — |
| Changed pairs | — |
| Unchanged pairs | — |
| Corrupted/removed files | — |

## 2. Class Distribution

### Change vs No-Change
| Label | Count | Percentage |
|-------|-------|------------|
| change | — | — |
| no_change | — | — |

### Change Type (changed pairs only)
| Type | Count | Percentage |
|------|-------|------------|
| object_added | — | — |
| object_removed | — | — |
| object_moved | — | — |

## 3. Scene Category Distribution

| Category | Count |
|----------|-------|
| indoor_room | — |
| indoor_kitchen | — |
| indoor_classroom | — |
| outdoor_courtyard | — |
| outdoor_garden | — |
| outdoor_street | — |
| other | — |

## 4. Missing Annotation Rate

| Metric | Count |
|--------|-------|
| Pairs without complete labels | — |
| Missing masks (changed pairs) | — |
| Missing metadata fields | — |

## 5. Duplicate Count

| Metric | Count |
|--------|-------|
| Perceptual hash duplicates found | — |
| Duplicates removed | — |

## 6. Independent Verification (20% audit)

### Audit Sample
- Pairs audited: — / — (—%)
- Second annotator: (pseudonym)

### Agreement Metrics

| Metric | Value |
|--------|-------|
| Cohen's κ (change/no-change label) | — |
| Mean IoU (change masks, changed pairs) | — |
| Mean IoU (bounding boxes, changed pairs) | — |
| Exact match (change_type) | — |

### Disagreement Resolution
- Disagreements found: —
- Resolution method: —
- Resolved by: — (without publishing annotator identities)

## 7. Privacy & Rights Audit

- [ ] No identifiable faces in any image
- [ ] No readable personal text/documents
- [ ] No license plates
- [ ] No precise location identifiers
- [ ] EXIF/GPS metadata stripped from all images
- [ ] All capture sites had permission

## 8. File Integrity

- [ ] All files in manifest.csv exist on disk
- [ ] SHA-256 checksums match
- [ ] No corrupted images (verified by validate.py)
- [ ] No conflicting pair IDs
