#!/usr/bin/env python3
"""
Author: Fredhappyface
Date: 2020/02/19

Cat an image to the console. Inspired by img2txt
https://github.com/hit9/img2txt.git by Chao Wang
"""
from __future__ import annotations

from typing import Any, Callable, Union
import urllib.request
import os
import argparse
from pathlib import Path
from PIL import Image
LAZY_PRINT = None
try:
	from cli2gui import Cli2Gui
	from metprint import LogType, LAZY_PRINT
except ImportError:

	def Cli2Gui(*args: Any, **kwargs: Any):
		def wrapper(callingFunction: Callable[..., None]):
			def inner(*args: Any, **kwargs: Any):
				return callingFunction(*args, **kwargs)

			inner.__name__ = callingFunction.__name__
			return inner
		return wrapper


THISDIR = str(Path(__file__).resolve().parent)


def openImageToPx(imageName: str, maxLen: int, hd: bool = False) -> tuple[Any,
int, int]:
	"""Get an array of pixels and the dimensions of these

	Args:
		imageName (str): path of the image on the filesystem (relative of
		absolute)
		maxLen (int): maximum of width and height in chars
		hd (bool, optional): get 'hd' array of pixels. Defaults to False.

	Returns:
		int[][], int, int: 2d array of pixels, and the dimensions of the image
	"""
	if not os.path.exists(imageName):
		if LAZY_PRINT is not None:
			LAZY_PRINT(imageName + " does not exist", LogType.ERROR)
		else:
			print("- Error: " + imageName + " does not exist")
		return Image.open(THISDIR + os.sep +
		"broken.png").convert("RGBA").load(), 16, 16
	image = Image.open(imageName).convert("RGBA")
	initW, initH = image.size
	scale = maxLen / max(initH, initW)
	width = int(scale * initW)
	height = int(scale * initH / (1 if hd else 2))
	image = image.resize((width, height))
	pixels = image.load()
	return pixels, width, height


def getANSIColour(rgb: tuple[int, ...]) -> int:
	"""Generate the ansi escape code based on the pixel value

	Args:
		rgb (tuple[int, ...]): int array with pixel rgb values: [r, g, b]

	Returns:
		int: ansi escape code for the colour
	"""
	websafeR = int(round((rgb[0] / 255.0) * 5))
	websafeG = int(round((rgb[1] / 255.0) * 5))
	websafeB = int(round((rgb[2] / 255.0) * 5))
	return int(((websafeR*36) + (websafeG*6) + websafeB) + 16)

def genANSIpx(beforeColour: Union[None, int, tuple[int, ...]], colour: Union[None, int, tuple[int, ...]], bg: bool=False,
trueColour: bool=True) -> str: # yapf: disable
	"""Generate the ansi escape string for a set of pixels with the same
	colour

	Args:
		beforeColour (Union[None, int, tuple[int, ...]]): previous colour
		colour (Union[None, int, tuple[int, ...]]): current colour
		bg (bool, optional): ansi background char. Defaults to False.
		trueColour (bool, optional): print in true colour. Defaults to True.

	Returns:
		str: string to represent char colour
	"""
	colourArr = []
	if not trueColour:
		if isinstance(beforeColour, tuple):
			beforeColour = getANSIColour(
			beforeColour) if beforeColour is not None else None
		if isinstance(colour, tuple):
			colour = getANSIColour(colour) if colour is not None else None

	if colour != beforeColour:
		if colour is None:
			colourArr.append("49" if bg else "39")
		elif not trueColour:
			colourArr += ["48" if bg else "38", "5", str(colour)]
		elif isinstance(colour, tuple):
			colourArr += [
			"48" if bg else "38", "2",
			str(colour[0]),
			str(colour[1]),
			str(colour[2])]
	return "\x1b[" + ";".join(colourArr) + "m" if len(colourArr) > 0 else ""


def generateHDColour(imageName: str, maxLen: int, trueColour: bool = True,
char: str = "\u2584") -> str:
	"""Iterate through image pixels to make a printable string

	Args:
		imageName (str): path of the image on the filesystem (relative of
		absolute)
		maxLen (int): maximum of width and height in chars
		trueColour (bool, optional): print in true colour. Defaults to True.
		char (str, optional): use this char for each pixel. Defaults to "\u2584".

	Returns:
		str: string to print
	"""
	char = "\u2584" if char in [None, ""] else char
	pixels, width, height = openImageToPx(imageName, maxLen, hd=True)
	result = ["\x1b[2K\x1b[0m"] # Clear line and reset
	beforeFgColour = None
	beforeBgColour = None
	for h in range(0, height, 2):
		for w in range(width):
			rgbaBg = pixels[w, h]
			try:
				rgbaFg = pixels[w, h + 1]
			except IndexError:
				rgbaFg = pixels[w, h]
			if rgbaBg[3] != 0:
				result.append(
				genANSIpx(beforeBgColour, rgbaBg[:3], True, trueColour=trueColour))
				beforeBgColour = rgbaBg[:3]
			else:
				result.append(genANSIpx(beforeBgColour, None, True, trueColour=trueColour))
				beforeBgColour = None
			if rgbaFg[3] != 0:
				result.append(
				genANSIpx(beforeFgColour, rgbaFg[:3], trueColour=trueColour) + char)
				beforeFgColour = rgbaFg[:3]
			else:
				result.append(genANSIpx(beforeFgColour, None, trueColour=trueColour) + " ")
				beforeFgColour = None
		if h + 1 != height:
			beforeFgColour = None
			beforeBgColour = None
			result.append("\x1b[39m\x1b[49m\n")

	return "".join(result)


def generateColour(imageName: str, maxLen: int, trueColour: bool = True,
char: str = "\u2588"):
	"""Iterate through all of the pixels in an image and construct a printable
	string

	Args:
		imageName (str): path of the image on the filesystem (relative of
		absolute)
		maxLen (int): maximum of width and height in chars
		trueColour (bool, optional): print in true colour. Defaults to True.
		char (str, optional): use this char for each pixel. Defaults to "\u2588".

	Returns:
		str: string to print
	"""
	char = "\u2588" if char in [None, ""] else char
	pixels, width, height = openImageToPx(imageName, maxLen)
	result = ["\x1b[2K\x1b[0m"] # Clear line and reset
	beforeFgColour = None
	for h in range(height):
		for w in range(width):
			rgba: tuple[int, ...] = pixels[w, h]
			if rgba[3] != 0:
				result.append(
				genANSIpx(beforeFgColour, rgba[:3], trueColour=trueColour) + char)
				beforeFgColour = rgba[:3]
			else:
				result.append(genANSIpx(beforeFgColour, None, trueColour=trueColour) + " ")
				beforeFgColour = None
		if h + 1 != height:
			beforeFgColour = None
			result.append("\x1b[39m\n")
	return result


def generateGreyscale(imageName: str, maxLen: int):
	"""Iterate through image pixels to make a printable string

	Args:
		imageName (str): path of the image on the filesystem (relative of
		absolute)
		maxLen (int): maximum of width and height in chars

	Returns:
		str: string to print
	"""
	pixels, width, height = openImageToPx(imageName, maxLen)
	result = [""]
	color = " .;-:!>7?CO$QHNM"
	for h in range(height):
		for w in range(width):
			rgba = pixels[w, h]
			rgb: tuple[int, ...] = rgba[:3]
			result.append(color[int(sum(rgb) / 3.0 / 256.0 * 16)])
		result.append("\n")
	return "".join(result)


def handleArgs(args: argparse.Namespace):
	"""Handle arguments from the cli/ gui

	Args:
		args (argparse.Namespace): arguments
	"""
	if args.url:
		urllib.request.urlretrieve(args.image, "dowloadedImage.jpg")
		args.image = "dowloadedImage.jpg"

	maxLen = 130 if args.big else 78
	if not args.greyscale and not args.regular:
		result = generateHDColour(args.image, maxLen, not args.disable_truecolour,
		args.char)
	elif not args.greyscale and args.regular:
		result = generateColour(args.image, maxLen, not args.disable_truecolour,
		args.char)
	else:
		result = generateGreyscale(args.image, maxLen)
	print(result)


@Cli2Gui(run_function=handleArgs, image=THISDIR + os.sep + "program_icon.png",
program_name="CatImage")
def cli(): # pragma: no cover
	""" CLI entry point """
	parser = argparse.ArgumentParser(description="cat an image to the terminal")
	parser.add_argument("image", type=str, help="image file or url")
	parser.add_argument("-u", "--url", action="store_true", help="image is a URL")
	parser.add_argument("-b", "--big", action="store_true", help="big image")
	parser.add_argument(
	"-c", "--char", action="store",
	help="char to use in colour print use $'chr' for escaped chars")
	parser.add_argument("-t", "--disable-truecolour", action="store_true",
	help="disable output in truecolour")

	group = parser.add_argument_group(
	"choose one of the following",
	"use the following arguments to change the look of the image")
	mxg = group.add_mutually_exclusive_group()
	mxg.add_argument(
	"-g", "--greyscale", action="store_true",
	help="output image in greyscale (best for terminals that cannot handle ANSI)")
	mxg.add_argument("-r", "--regular", action="store_true",
	help="output image in regular definition")

	args = parser.parse_args()
	handleArgs(args)


if __name__ == "__main__": # pragma: no cover
	cli()
