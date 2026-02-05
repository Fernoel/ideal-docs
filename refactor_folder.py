import os
import shutil
from pathlib import Path

def move_to_folders():
    # Define paths
    docs_dir = Path("docs")
    en_dir = docs_dir / "en"
    es_dir = docs_dir / "es"
    
    # Create language dirs
    en_dir.mkdir(exist_ok=True)
    es_dir.mkdir(exist_ok=True)
    
    # Files to ignore (assets, and the language folders themselves)
    ignore = {".DS_Store", "en", "es", "assets"}
    
    # Walk through docs directory
    # We need to list files first to avoid walking into en/es as we create them
    # But os.walk is convenient. We can exclude en/es from dirs.
    
    for root, dirs, files in os.walk(docs_dir, topdown=True):
        # Modify dirs in-place to skip en/es and assets
        dirs[:] = [d for d in dirs if d not in ignore]
        
        rel_path = Path(root).relative_to(docs_dir)
        
        for file in files:
            if file in ignore: continue
            
            src = Path(root) / file
            
            if file.endswith(".es.md"):
                # Spanish file
                # Remove .es.md and move to es/
                new_name = file.replace(".es.md", ".md")
                dest = es_dir / rel_path / new_name
                dest.parent.mkdir(parents=True, exist_ok=True)
                print(f"Moving {src} to {dest}")
                shutil.move(str(src), str(dest))
                
            elif file.endswith(".md"):
                # English file (default)
                # Move to en/
                dest = en_dir / rel_path / file
                dest.parent.mkdir(parents=True, exist_ok=True)
                print(f"Moving {src} to {dest}")
                shutil.move(str(src), str(dest))
            else:
                # Other files (images in markdown folders? or assets?)
                # If it's not .md, leave it or move to en?
                # Usually better to leave common files, but if they are specific...
                # Let's assume non-md files in content folders are specific.
                # But assets/ is already ignored.
                print(f"Skipping non-md file: {src}")

def cleanup_empty_dirs():
    docs_dir = Path("docs")
    for root, dirs, files in os.walk(docs_dir, topdown=False):
        for name in dirs:
            if name in ["en", "es", "assets"]: continue
            path = Path(root) / name
            if not any(path.iterdir()):
                print(f"Removing empty dir: {path}")
                path.rmdir()

if __name__ == "__main__":
    move_to_folders()
    cleanup_empty_dirs()
