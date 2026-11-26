import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
dry_run = "--dry-run" in sys.argv

count = 0
for f in root.rglob("*"):
    if f.is_file() and f.suffix.lower() == ".h5":
        print(("Would delete: " if dry_run else "Deleting: ") + str(f))
        if not dry_run:
            f.unlink()
        count += 1

print(f"{count} PNG file(s) {'found' if dry_run else 'deleted'}.")