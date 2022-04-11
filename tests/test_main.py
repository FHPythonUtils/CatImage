"""Tests
"""
from __future__ import annotations

import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))


import catimage


def aux_readansi(path: str):
	return Path(f"{THISDIR}/data/{path}").read_text(encoding="utf-8").rstrip()


def test_greyscale():
	assert catimage.generateGreyscale(f"{THISDIR}/data/test.png", 80).rstrip() == aux_readansi(
		"test_greyscale.txt"
	)


def test_hdcolour():
	assert catimage.generateHDColour(f"{THISDIR}/data/test.png", 80).rstrip() == aux_readansi(
		"test_hd.txt"
	)


def test_colour():
	assert catimage.generateColour(f"{THISDIR}/data/test.png", 80).rstrip() == aux_readansi(
		"test_colour.txt"
	)


def test_notexists():
	assert catimage.generateHDColour(f"{THISDIR}/data/notexists.png", 80).rstrip() == aux_readansi(
		"test_broken.txt"
	)
