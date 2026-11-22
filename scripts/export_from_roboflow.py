"""
export_from_roboflow.py — Export Annotations from Roboflow
Subject 23: Paired Real-World Scene Change and No-Change Dataset

Downloads dataset versions in COCO JSON format into data/derived/roboflow_exports/
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

EXPORT_DIR = ROOT / "data" / "derived" / "roboflow_exports"

if not API_KEY or API_KEY == "your_roboflow_api_key_here":
    print("ERROR: ROBOFLOW_API_KEY not found in .env")
    sys.exit(1)

def export_version(version_num=1):
    rf = Roboflow(api_key=API_KEY)
    ws = rf.workspace(WORKSPACE_NAME)
    project = ws.project(PROJECT_NAME)
    
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    
    print(f"Exporting version {version_num} from {project.name}...")
    try:
        version = project.version(version_num)
        dataset = version.download("coco-segmentation", location=str(EXPORT_DIR))
        print(f"Successfully downloaded to: {EXPORT_DIR}")
    except Exception as e:
        print(f"Error downloading version {version_num}: {e}")

if __name__ == "__main__":
    v = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    export_version(v)
