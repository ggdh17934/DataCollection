# CV26-Dataset-Subject-23: Paired Real-World Scene Change and No-Change Dataset

## Project Overview

**University:** University of Echahid Hamma Lakhdar – El Oued, Algeria  
**Department:** Computer Science  
**Academic Year:** 2026–2027  
**Subject:** 23 — Paired Real-World Scene Change and No-Change Dataset  
**Supervisor:** Dr. Mohammed Anouar Naoui  

## Description

A newly collected dataset of **150 paired scene images** (300 total captures) designed for **scene change detection**. Each pair consists of a "before" and "after" photograph of the same scene:

- **75 changed pairs**: An object was visibly added, removed, or moved between captures
- **75 unchanged pairs**: No object changes — only natural lighting/viewpoint differences (distractor controls)

Each changed pair is annotated with:
- Change/No-change binary label
- Change type (`object_added`, `object_removed`, `object_moved`)
- Bounding box around the changed region
- Binary segmentation mask of the changed region
- Scene category, lighting conditions, time gap, and quality metadata

## CV Task

Scene change detection against lighting and viewpoint distractors.

## Main Research Reference

> *Towards Generalizable Scene Change Detection* (Kim and Kim, CVPR 2025)

## Comparable Benchmarks

| Dataset | Type | Difference from ours |
|---------|------|---------------------|
| LEVIR-CD | Satellite bi-temporal change detection | Remote sensing only, no ground-level scenes |
| CDnet 2014 | Video change detection | Video-based, no paired stills, no object-level labels |
| Kim & Kim 2025 | Scene change detection method | Method paper, not a paired-capture dataset |

## Repository Structure

```
CV26-dataset-subject-23/
├── README.md                   # This file
├── LICENSE-or-ACCESS.md        # Access terms and rights
├── data/
│   ├── originals/              # Raw captured images
│   │   ├── changed/            # Changed scene pairs
│   │   └── unchanged/          # Unchanged scene pairs
│   └── derived/                # Masks and annotation exports
│       ├── masks/              # Binary PNG change masks
│       └── roboflow_exports/   # COCO JSON exports from Roboflow
├── annotations/
│   ├── labels.jsonl            # Per-pair annotations
│   ├── annotation_schema.json  # Schema definition
│   └── annotator_guidelines.md # Annotation instructions
├── metadata/
│   ├── manifest.csv            # Sample manifest
│   ├── checksums.sha256        # File integrity hashes
│   └── acquisition_summary.csv # Capture log
├── scripts/
│   ├── validate.py             # Validation script
│   ├── deduplicate.py          # Duplicate detection
│   └── dataset_stats.py        # Statistics generation
├── quality/
│   ├── qc_report.md            # Quality control report
│   └── reviewed_sample_ids.csv # Audited samples
├── documentation/
│   ├── dataset_card.md         # Dataset card (Gebru et al.)
│   ├── collection_protocol.md  # Capture protocol
│   ├── related_datasets.md     # 3-dataset comparison
│   └── rights_and_consent_policy.md
├── report/
│   ├── main.tex                # LaTeX report
│   ├── references.bib          # Bibliography
│   ├── figures/                # Report figures
│   └── report.pdf              # Compiled report
├── ai_prompts/
│   ├── prompt_history.md       # AI usage log
│   └── ai_usage_declaration.md # Declaration
└── presentation/
    └── final_slides.pdf        # Final presentation
```

## Planning Target

- 150 original image pairs (300 captures)
- 75 changed pairs + 75 unchanged pairs
- Annotation tool: Roboflow (Instance Segmentation)
- Export format: COCO JSON + PNG masks

## Collection Period

November–December 2026 (6 weeks)

## License & Access

This dataset is collected for academic purposes. See [LICENSE-or-ACCESS.md](LICENSE-or-ACCESS.md) for details.
