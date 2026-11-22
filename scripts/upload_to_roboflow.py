"""
upload_to_roboflow.py — Upload Captured Images to Roboflow
Subject 23: Paired Real-World Scene Change and No-Change Dataset

Uploads images from data/originals/ directly to your Roboflow project.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from roboflow import Roboflow

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

API_KEY = os.getenv("ROBOFLOW_API_KEY")
WORKSPACE_NAME = os.getenv("ROBOFLOW_WORKSPACE", "datacollections-workspace")
PROJECT_NAME = os.getenv("ROBOFLOW_PROJECT", "cv26-scene-change-s23")

if not API_KEY or API_KEY == "your_roboflow_api_key_here":
    print("ERROR: ROBOFLOW_API_KEY not found in .env")
    sys.exit(1)

def upload_images(batch_name="pilot"):
    rf = Roboflow(api_key=API_KEY)
    ws = rf.workspace(WORKSPACE_NAME)
    project = ws.project(PROJECT_NAME)
    
    print(f"Connected to Roboflow project: {project.name}")
    
    dirs_to_upload = [
        ROOT / "data" / "originals" / "changed",
        ROOT / "data" / "originals" / "unchanged",
    ]
    
    total_uploaded = 0
    for img_dir in dirs_to_upload:
        if not img_dir.exists():
            continue
        
        images = list(img_dir.glob("*.jpg")) + list(img_dir.glob("*.png"))
        if not images:
            continue
            
        print(f"\nUploading from {img_dir.name} ({len(images)} images)...")
        for img_path in sorted(images):
            try:
                print(f"  Uploading {img_path.name}...")
                project.upload(
                    image_path=str(img_path),
                    batch_name=batch_name,
                    num_retry_uploads=3
                )
                total_uploaded += 1
            except Exception as e:
                print(f"  Failed to upload {img_path.name}: {e}")
                
    print(f"\nDone! Uploaded {total_uploaded} images to Roboflow batch: '{batch_name}'.")

if __name__ == "__main__":
    batch = sys.argv[1] if len(sys.argv) > 1 else "pilot_batch"
    upload_images(batch_name=batch)
