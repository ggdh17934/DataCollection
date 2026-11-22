# Collection Protocol — Paired Real-World Scene Change and No-Change Dataset

## 1. Equipment

- **Camera**: Smartphone camera (12+ MP recommended)
- **Stabilization**: Use a tripod, stack of books, or tape-marked floor position to maintain consistent framing
- **Reference markers** (optional): Small tape marks on the ground to reposition the camera if needed

## 2. Scene Selection

### Planned Sites

Select 20–30 permitted locations across these categories:

| # | Scene Category | Example Sites | Target Pairs |
|---|---------------|---------------|-------------|
| 1 | Indoor — Room/Bedroom | Your room, friend's room (with permission) | ~24 pairs |
| 2 | Indoor — Kitchen | Your kitchen, cafeteria corner | ~20 pairs |
| 3 | Indoor — Classroom/Office | University classroom (permitted), study room | ~20 pairs |
| 4 | Outdoor — Courtyard/Patio | University courtyard, home terrace | ~24 pairs |
| 5 | Outdoor — Garden/Park | Garden, park bench area | ~24 pairs |
| 6 | Outdoor — Street/Walkway | Permitted walkway, building entrance | ~20 pairs |
| 7 | Other | Garage, stairwell, balcony | ~18 pairs |

### Site Requirements
- You must have **permission** to photograph at the site
- No identifiable people should be visible
- No private/sensitive documents visible
- Safe and accessible location

## 3. Capture Protocol — Step by Step

### For Every Pair:

```
1. SETUP
   - Place camera on tripod/stable surface
   - Frame the scene — ensure interesting objects are visible
   - Note: site name, time, lighting condition, weather (outdoor)

2. CAPTURE "BEFORE"
   - Take the "before" photograph
   - File name: CV26_S23_PXXX_before.jpg

3. FOR CHANGED PAIRS (75 total):
   a. Make exactly ONE visible change:
      - ADD an object (place a cup, book, bag, plant pot, etc.)
      - REMOVE an object (take away something that was visible)
      - MOVE an object (slide it to a noticeably different position)
   b. DO NOT move the camera
   c. Capture the "after" photograph
   d. File name: CV26_S23_PXXX_after.jpg
   e. Record: what changed, change type, approximate change region

4. FOR UNCHANGED PAIRS (75 total):
   a. DO NOT touch any objects
   b. Wait 5–60 minutes, or return at a different time of day
   c. Natural changes are expected: shadows shift, lighting changes
   d. Capture the "after" photograph
   e. File name: CV26_S23_PXXX_after.jpg
   f. Record: time gap, lighting difference description

5. LOG the capture in acquisition_summary.csv
```

## 4. Change Types — What to Alter

### Object Added (~25 pairs)
Examples: Place a coffee mug on a table, put a backpack on a chair, add a book to a shelf, place a water bottle on a desk, put shoes near a door.

### Object Removed (~25 pairs)
Examples: Remove a lamp from a desk, take away a fruit bowl, remove a jacket from a hook, take a plant pot off a windowsill.

### Object Moved (~25 pairs)
Examples: Slide a chair from one side of a table to another, move a laptop from center to edge, relocate a stack of papers, shift a bin from left to right.

## 5. No-Change Distractors — Natural Variations

### Lighting Shift (~25 pairs)
Capture morning vs afternoon, or sunny vs cloudy — same objects, different shadows.

### Cloud/Weather (~15 pairs)
Outdoor scenes where cloud cover changes between captures.

### Minor Camera Re-alignment (~25 pairs)
Intentionally re-place the camera with a slight shift — same scene content.

### Natural Movement (~10 pairs)
Curtain flutter, leaf movement, water ripple — NOT an object change.

## 6. EXIF Metadata Removal

Before committing any image to the repository:

```bash
# Using exiftool (install: https://exiftool.org/)
exiftool -all= -overwrite_original data/originals/**/*.jpg

# Or using Python (Pillow):
# See scripts/strip_exif.py
```

## 7. File Naming Convention

```
CV26_S23_P001_before.jpg    # Pair 001, before image
CV26_S23_P001_after.jpg     # Pair 001, after image
CV26_S23_P001_mask.png      # Pair 001, change mask (changed pairs only)
```

- Pairs 001–075: Changed pairs (in `data/originals/changed/`)
- Pairs 076–150: Unchanged pairs (in `data/originals/unchanged/`)

## 8. Acquisition Summary Log

Maintain `metadata/acquisition_summary.csv` with these columns:

```
pair_id,capture_date,time_before,time_after,site_name,scene_category,change_label,change_type,change_description,illumination_before,illumination_after,weather,camera_device,notes
```
