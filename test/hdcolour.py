"""Print test image as hd colour
"""
import sys
import os
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))

import catimage

print(catimage.generateHDColour(THISDIR + os.sep + "test.png", 80))
