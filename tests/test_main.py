"""Tests
"""
from __future__ import annotations

import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))


import catimage


def test_greyscale():
	assert catimage.generateGreyscale(f"{THISDIR}/data/test.png", 80).rstrip() == Path(f"{THISDIR}/data/test_greyscale.txt").read_text(encoding="utf-8").rstrip()


def test_hdcolour():
	assert catimage.generateHDColour(f"{THISDIR}/data/test.png", 80).rstrip() == Path(f"{THISDIR}/data/test_hd.txt").read_text(encoding="utf-8").rstrip()
