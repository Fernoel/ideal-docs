import os
import shutil
from pathlib import Path

def move_en():
    base = Path("docs/en")
    if not base.exists():
        print("docs/en does not exist")
        return
    for root, dirs, files in os.walk(base):
        for file in files:
            src = Path(root) / file
            rel_path = src.relative_to(base)
            dest = Path("docs") / rel_path
            dest.parent.mkdir(parents=True, exist_ok=True)
            if dest.exists():
                print(f"Warning: {dest} already exists. Overwriting.")
            print(f"Moving {src} to {dest}")
            shutil.move(str(src), str(dest))
    shutil.rmtree(base)

def move_es():
    base = Path("docs/es")
    if not base.exists():
        print("docs/es does not exist")
        return
    for root, dirs, files in os.walk(base):
        for file in files:
            src = Path(root) / file
            rel_path = src.relative_to(base)
            
            if file.endswith(".md"):
                new_name = file[:-3] + ".es.md"
                dest = Path("docs") / rel_path.parent / new_name
            else:
                # Assets or other files
                dest = Path("docs") / rel_path
            
            dest.parent.mkdir(parents=True, exist_ok=True)
            print(f"Moving {src} to {dest}")
            shutil.move(str(src), str(dest))
    shutil.rmtree(base)

def fix_blog_en_suffix():
    base = Path("docs/blog/posts")
    if not base.exists(): return
    for file in base.glob("*.en.md"):
        new_name = file.name.replace(".en.md", ".md")
        print(f"Renaming {file} to {new_name}")
        file.rename(base / new_name)

if __name__ == "__main__":
    move_en()
    move_es()
    fix_blog_en_suffix()
