


import argparse
import os
import sys
from collections import defaultdict, Counter


def load_paths(path):
    
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Input file not found: {path}")
    items = []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            items.append(line)
    return items


def group_by_extension(paths):
   
    groups = defaultdict(list)
    unknowns = []
    for p in paths:
        ext = extract_extension(p)
        if ext == "":
            unknowns.append(p)
        else:
            groups[ext].append(p)
    counts = Counter({ext: len(files) for ext, files in groups.items()})
    return counts, groups, unknowns






