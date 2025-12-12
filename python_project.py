


import argparse
import os
import sys
from collections import defaultdict, Counter


def load_paths(path):
    """
    Load the list of file paths from a text file (one path per line).
    Ignores empty lines and comments starting with '#'.
    """
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
    """
    Group paths by their file extension. Returns:
      - counts: Counter mapping extension -> count
      - groups: dict mapping extension -> list of files
      - unknowns: list of files with no extension
    """
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






