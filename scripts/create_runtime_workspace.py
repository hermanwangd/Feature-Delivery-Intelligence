#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path(sys.argv[1] if len(sys.argv)>1 else ".fdi-work")
for d in ["clones","worktrees","grafel","observations","proposals","evidence","logs"]:
    (root/d).mkdir(parents=True, exist_ok=True)
print(root.resolve())
