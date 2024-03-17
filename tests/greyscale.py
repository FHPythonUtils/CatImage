"""Print test image as greyscale"""

from __future__ import annotations

import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))

import catimage

print(catimage.generateGreyscale(f"{THISDIR}/data/test.png", 80))
