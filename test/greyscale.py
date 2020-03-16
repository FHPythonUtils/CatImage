"""Print test image as greyscale
"""
import sys
import os
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))

import catimage

print(catimage.generateGreyscale(THISDIR + os.sep + "test.png", 80))
