# Dataset Card — Paired Real-World Scene Change and No-Change Dataset

*Following the "Datasheets for Datasets" template (Gebru et al., 2021)*

## Motivation

### For what purpose was the dataset created?
To provide a ground-level, paired scene change detection benchmark with explicit change/no-change labels, change-type taxonomy, and controlled distractor conditions.

### Who created the dataset?
Master's student at the University of Echahid Hamma Lakhdar – El Oued, Algeria, under supervision of Dr. Mohammed Anouar Naoui.

### Who funded the creation of the dataset?
University academic project; no external funding.

---

## Composition

### What do the instances represent?
Each instance is a pair of photographs of the same scene taken at two different times. Some pairs contain a visible object change; others do not.

### How many instances are there?
Planning target: 150 image pairs (300 photographs). 75 changed + 75 unchanged.

### What data does each instance consist of?
- Two JPEG images (before and after)
- Binary change/no-change label
- Change type (added/removed/moved) for changed pairs
- Bounding box and polygon mask for the changed region
- Scene category, lighting conditions, time gap, and quality metadata

### Is there any missing data?
*To be completed after collection.*

### Does the dataset contain data that might be considered confidential?
No. All scenes are of non-sensitive everyday environments. No people, personal documents, or private information.

---

## Collection Process

### How was the data collected?
Smartphone photographs captured on a tripod or stable surface at permitted locations in El Oued, Algeria.

### Who was involved in the data collection process?
The student author captured all images. A second annotator independently verified a subset.

### Over what time frame was the data collected?
November–December 2026 (6-week project period).

### Were any ethical review processes conducted?
The collection follows the handbook's mandatory rules: no identifiable people, stripped EXIF metadata, permission-based site access, and no modification of public infrastructure.

---

## Annotation

### What annotations are provided?
- Change/no-change binary label
- Change type: `object_added`, `object_removed`, `object_moved`
- Bounding box around changed region
- Polygon segmentation mask (binary PNG)
- Scene category, illumination, viewpoint shift

### How were annotations collected?
Using Roboflow (Instance Segmentation project) with manual polygon annotation. Exported in COCO JSON format.

### Who performed the annotation?
Primary annotation by the student author. Independent verification of 20% of pairs by a second annotator.

---

## Uses

### What tasks is the dataset suitable for?
- Scene change detection
- Change localization (segmentation)
- Change classification
- Robustness testing against lighting/viewpoint distractors

### What tasks should it NOT be used for?
- Real-time surveillance or security applications
- Any task requiring identified individuals
- Claims of geographic representativeness beyond the collection setting

---

## Distribution

### How will the dataset be distributed?
Private GitHub repository accessible to the supervisor.

### License?
Restricted academic use. See LICENSE-or-ACCESS.md.

---

## Maintenance

### Who will maintain the dataset?
The student author during the project period. No long-term maintenance commitment.

### Will the dataset be updated?
Version 1.0 is frozen at submission. No updates planned.
