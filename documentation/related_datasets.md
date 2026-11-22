# Related Datasets — Comparison Worksheet

## Mandatory 3-Dataset Comparison (Required by handbook Section 4.1)

| Field | LEVIR-CD | CDnet 2014 | Our Collection (CV26-S23) |
|-------|----------|------------|---------------------------|
| **Full name** | LEVIR-CD: A New Change Detection Dataset for Building Change Detection | CDnet 2014: An Expanded Change Detection Benchmark Dataset | Paired Real-World Scene Change and No-Change Dataset |
| **Authors / Source** | Chen & Shi, 2020 | Goyette, Jodoin et al., 2014 | Student — Univ. El Oued, 2026–2027 |
| **Collection year** | 2017–2019 | 2012–2014 | 2026–2027 |
| **Geography** | Texas, USA & Chinese cities (satellite) | Global outdoor scenes (CCTV) | El Oued, Algeria (indoor + outdoor) |
| **Modality** | Satellite RGB images, 1024×1024 crops | Fixed-camera video frames (RGB) | Smartphone still photographs, paired captures |
| **Capture conditions** | Aerial / satellite; different dates | Fixed CCTV; continuous video | Ground-level; controlled tripod/hand-held |
| **Task** | Binary pixel-level building change detection | Frame-level foreground/background segmentation | Pair-level change/no-change classification + change region mask + change type |
| **Annotation unit** | Pixel-level binary mask (changed/unchanged building) | Per-frame foreground mask | Per-pair: binary label, change type, region box, polygon mask |
| **Object categories** | Buildings only (construction/demolition) | Generic foreground blobs (people, cars, animals) | Specific everyday objects (cups, books, furniture, bags, plants) |
| **Language** | English | English | English (annotations) |
| **Sample count** | 637 image pairs | 53 video sequences (~160k frames) | 150 pairs / 300 images (planning target) |
| **Ground-truth verification** | Manual mask labeling by researchers | Manual frame labeling | Human Roboflow annotation + 20% independent audit |
| **Access terms** | Open access (academic license) | Open access | Private / restricted (academic project) |
| **Known limitations** | Satellite-only; no ground-level; buildings-only; no change type taxonomy; no no-change controls | Video-only; no paired stills; no object-level description; foreground blobs not object identities | Smaller scale; single geographic region; phone camera only |
| **Precise gap our dataset fills** | — | — | ✅ Ground-level paired still images with explicit change/no-change labels, 3-category change-type taxonomy (added/removed/moved), controlled distractor no-change pairs, in an underrepresented North African setting |

## Gap Summary

Existing scene change detection datasets are either:
1. **Satellite-based** (LEVIR-CD) — detecting building-level changes from aerial views, with no ground-level everyday-object changes
2. **Video-based** (CDnet) — detecting foreground motion in continuous video, without paired still-image captures or object-level change descriptions

Our dataset provides **ground-level, paired still photographs** with:
- Explicit **change/no-change** binary labels
- A **change-type taxonomy** (added, removed, moved)
- **Controlled no-change distractor pairs** (lighting-only differences)
- **Object-level descriptions** of what changed
- Collection in an **underrepresented Algerian setting**

## References

1. Chen, H., & Shi, Z. (2020). "A Spatial-Temporal Attention-Based Method and a New Dataset for Remote Sensing Image Change Detection." *Remote Sensing*, 12(10), 1662.
2. Goyette, N., Jodoin, P.-M., Porikli, F., Konrad, J., & Ishwar, P. (2014). "A Novel Video Dataset for Change Detection Benchmarking." *IEEE Trans. Image Processing*.
3. Kim, C., & Kim, J. (2025). "Towards Generalizable Scene Change Detection." *CVPR 2025*.
