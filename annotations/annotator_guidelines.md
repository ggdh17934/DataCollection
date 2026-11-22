# Annotator Guidelines — Scene Change Detection Dataset (Subject 23)

## Overview

This document provides step-by-step instructions for annotating paired scene images in **Roboflow**. Each image pair consists of a "before" and "after" photograph of the same scene. Your task is to identify and annotate any **real object changes** between the two images.

---

## 1. Understanding the Task

### What is a "change"?
A **change** occurs when a physical object has been:
- **Added**: An object appears in the "after" image that was not in the "before" image
- **Removed**: An object present in the "before" image is absent in the "after" image
- **Moved**: An object has changed position between the two images

### What is NOT a change?
The following are **NOT** considered changes:
- Lighting/shadow differences (sun moved, clouds appeared, lights turned on/off)
- Slight camera position shifts
- Natural movement of non-target elements (curtain flutter, leaves)
- Color temperature differences due to white balance

---

## 2. Annotation Workflow in Roboflow

### Step 1: Open the "after" image
- Always annotate on the **"after" image** of a changed pair
- Keep the "before" image visible as reference (use a second screen or printed copy)

### Step 2: Identify the change
- Compare the "after" image with the "before" image
- Locate the exact region where the change occurred

### Step 3: Draw the annotation

#### For Changed Pairs:
1. Select the **polygon tool** (Smart Polygon recommended)
2. Draw a tight polygon around the **entire changed region**
   - For `object_added`: outline the newly added object
   - For `object_removed`: outline the area where the object used to be (now empty)
   - For `object_moved`: outline the object in its new position
3. Assign the correct class label:
   - `object_added`
   - `object_removed`
   - `object_moved`

#### For Unchanged Pairs:
- **Do NOT draw any annotations**
- The image should remain with zero annotations in Roboflow
- These pairs serve as negative control samples

### Step 4: Verify your annotation
- Check that the polygon tightly fits the changed region
- Ensure the class label is correct
- Save the annotation

---

## 3. Annotation Rules

### Rule 1: One change per pair
Each pair contains **exactly one** intentional change (or no change). Annotate only the primary change.

### Rule 2: Tight polygons
Draw polygons that **closely follow the object boundary**. Do not leave large gaps or include excessive background.

### Rule 3: Be consistent with classes
- `object_added` = object was NOT in "before", IS in "after"
- `object_removed` = object WAS in "before", is NOT in "after"  
- `object_moved` = same object in both images but at a **different position**

### Rule 4: Ignore lighting changes
If the only difference between "before" and "after" is lighting (shadows, brightness), this is a **no-change pair**. Do not annotate it.

### Rule 5: Handle edge cases
- **Partially visible objects**: Still annotate; add `partial_occlusion` quality flag
- **Very small changes**: Still annotate if the change is real and visible
- **Ambiguous changes**: Flag with a note; discuss with the team lead

---

## 4. Quality Checklist

Before marking an annotation as complete, verify:

- [ ] Correct "before"/"after" pair was compared
- [ ] Change type is correctly classified (added/removed/moved/no-change)
- [ ] Polygon tightly follows the changed region boundary
- [ ] Class label matches the actual change type
- [ ] No accidental annotations on no-change pairs
- [ ] Any quality issues noted in the metadata

---

## 5. Common Mistakes to Avoid

| Mistake | Why it's wrong | Correct approach |
|---------|---------------|------------------|
| Annotating shadows as changes | Shadows are lighting artifacts, not object changes | Only annotate physical object changes |
| Loose/sloppy polygons | Reduces mask quality and IoU scores | Draw tight polygons following object edges |
| Wrong class label | Corrupts the dataset semantics | Double-check: added? removed? moved? |
| Annotating "before" instead of "after" | We always annotate the after image | Always work on the "after" image |
| Missing annotation on a changed pair | Creates a false negative | Always compare with "before" image |
