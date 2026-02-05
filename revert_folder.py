import os
import shutil
from pathlib import Path

def flatten_folders():
    docs_dir = Path("docs")
    en_dir = docs_dir / "en"
    es_dir = docs_dir / "es"
    
    # Move en files to docs/
    if en_dir.exists():
        for root, dirs, files in os.walk(en_dir):
            rel_path = Path(root).relative_to(en_dir)
            dest_dir = docs_dir / rel_path
            dest_dir.mkdir(parents=True, exist_ok=True)
            
            for file in files:
                src = Path(root) / file
                dest = dest_dir / file
                print(f"Moving {src} to {dest}")
                shutil.move(str(src), str(dest))
    
    # Move es files to docs/ with .es.md suffix
    if es_dir.exists():
        for root, dirs, files in os.walk(es_dir):
            rel_path = Path(root).relative_to(es_dir)
            dest_dir = docs_dir / rel_path
            dest_dir.mkdir(parents=True, exist_ok=True)
            
            for file in files:
                if file.endswith(".md"):
                    new_name = file.replace(".md", ".es.md")
                    src = Path(root) / file
                    dest = dest_dir / new_name
                    print(f"Moving {src} to {dest}")
                    shutil.move(str(src), str(dest))
                else:
                    # Non-md files in es folder?
                    src = Path(root) / file
                    dest = dest_dir / file
                    print(f"Moving {src} to {dest}")
                    shutil.move(str(src), str(dest))

    # Cleanup
    if en_dir.exists():
        shutil.rmtree(en_dir)
    if es_dir.exists():
        shutil.rmtree(es_dir)

if __name__ == "__main__":
    flatten_folders()
