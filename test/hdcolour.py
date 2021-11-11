"""Print test image as hd colour
"""
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))

import catimage

print(catimage.generateHDColour(f"{THISDIR}/test.png", 80))
