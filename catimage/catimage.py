#!/usr/bin/env python3
"""
Author: Fredhappyface
Date: 2020/02/19.

Cat an image to the console. Inspired by img2txt
https://github.com/hit9/img2txt.git by Chao Wang
"""

from __future__ import annotations

import argparse
import urllib.request
from pathlib import Path
from sys import stdout
from typing import Any, Callable

from PIL import Image

try:
	from cli2gui import Cli2Gui
except ImportError:

	def Cli2Gui(*args: Any, **kwargs: Any):
		_ = args, kwargs

		def wrapper(callingFunction: Callable[..., None]):
			def inner(*args: Any, **kwargs: Any):
				return callingFunction(*args, **kwargs)

			inner.__name__ = callingFunction.__name__
			return inner

		return wrapper


stdout.reconfigure(encoding="utf-8")
THISDIR = str(Path(__file__).resolve().parent)


# pylint:disable=invalid-name


def openImageToPx(imageName: str, maxLen: int, *, hd: bool = False) -> tuple[Any, int, int]:
	"""Get an array of pixels and the dimensions of these.

	Args:
	----
		imageName (str): path of the image on the filesystem (relative of absolute)
		maxLen (int): maximum of width and height in chars
		hd (bool, optional): get 'hd' array of pixels. Defaults to False.

	Returns:
	-------
		tuple[Any, int, int]: 2D array of pixels, and the dimensions of the image

	"""
	imagePath = Path(imageName)
	if not imagePath.exists():
		print(f"- Error: {imageName} does not exist")
		return Image.open(THISDIR + "/broken.png").convert("RGBA").load(), 16, 16

	image = Image.open(imagePath).convert("RGBA")
	initW, initH = image.size
	scale = maxLen / max(initH, initW)
	width = int(scale * initW)
	height = int(scale * initH / (1 if hd else 2))
	image = image.resize((width, height))
	pixels = image.load()
	return pixels, width, height


def getANSIColour(rgb: tuple[int, ...]) -> int:
	"""Generate the ANSI escape code based on the pixel value.

	Args:
	----
		rgb (tuple[int, ...]): int array with pixel RGB values: [r, g, b]

	Returns:
	-------
		int: ANSI escape code for the color

	"""
	websafeR = int(round((rgb[0] / 255.0) * 5))
	websafeG = int(round((rgb[1] / 255.0) * 5))
	websafeB = int(round((rgb[2] / 255.0) * 5))
	return int(((websafeR * 36) + (websafeG * 6) + websafeB) + 16)


def genANSIpx(
	beforeColour: int | tuple[int, ...] | None,
	colour: int | tuple[int, ...] | None,
	*,
	bg: bool = False,
	trueColour: bool = True,
) -> str:
	"""Generate the ANSI escape string for a set of pixels with the same color.

	Args:
	----
		beforeColour (Optional[Union[int, tuple[int, ...]]]): previous color
		colour (Optional[Union[int, tuple[int, ...]]]): current color
		bg (bool, optional): ANSI background char. Defaults to False.
		trueColour (bool, optional): print in true color. Defaults to True.

	Returns:
	-------
		str: string to represent char color

	"""
	colourArr = []
	if not trueColour:
		if isinstance(beforeColour, tuple):
			beforeColour = getANSIColour(beforeColour) if beforeColour is not None else None
		if isinstance(colour, tuple):
			colour = getANSIColour(colour) if colour is not None else None

	if colour != beforeColour:
		if colour is None:
			colourArr.append("49" if bg else "39")
		elif not trueColour:
			colourArr += ["48" if bg else "38", "5", str(colour)]
		elif isinstance(colour, tuple):
			colourArr += ["48" if bg else "38", "2", str(colour[0]), str(colour[1]), str(colour[2])]

	return "\x1b[" + ";".join(colourArr) + "m" if len(colourArr) > 0 else ""


def generateHDColour(
	imageName: str, maxLen: int, *, trueColour: bool = True, char: str = "\u2584"
) -> str:
	"""Iterate through image pixels to make a printable string.

	Args:
	----
		imageName (str): path of the image on the filesystem (relative of absolute)
		maxLen (int): maximum of width and height in chars
		trueColour (bool, optional): print in true color. Defaults to True.
		char (str, optional): use this char for each pixel. Defaults to "\u2584".

	Returns:
	-------
		str: string to print

	"""
	char = "\u2584" if char in [None, ""] else char
	pixels, width, height = openImageToPx(imageName, maxLen, hd=True)
	result = ["\x1b[2K\x1b[0m"]  # Clear line and reset
	beforeBgColour = None
	beforeFgColour = None

	for h in range(0, height, 2):
		for w in range(width):
			rgbaBg = pixels[w, h]
			try:
				rgbaFg = pixels[w, h + 1]
			except IndexError:
				rgbaFg = pixels[w, h]

			if rgbaBg[3] != 0:
				result.append(genANSIpx(beforeBgColour, rgbaBg[:3], bg=True, trueColour=trueColour))
				beforeBgColour = rgbaBg[:3]
			else:
				result.append(genANSIpx(beforeBgColour, None, bg=True, trueColour=trueColour))
				beforeBgColour = None

			if rgbaFg[3] != 0:
				result.append(genANSIpx(beforeFgColour, rgbaFg[:3], trueColour=trueColour) + char)
				beforeFgColour = rgbaFg[:3]
			else:
				result.append(genANSIpx(beforeFgColour, None, trueColour=trueColour) + " ")
				beforeFgColour = None

		if h + 1 != height:
			beforeFgColour = None
			beforeBgColour = None
			result.append("\x1b[39m\x1b[49m\n")

	return "".join(result)


def generateColour(
	imageName: str, maxLen: int, *, trueColour: bool = True, char: str = "\u2588"
) -> str:
	"""Iterate through all of the pixels in an image and construct a printable string.

	Args:
	----
		imageName (str): path of the image on the filesystem (relative of absolute)
		maxLen (int): maximum of width and height in chars
		trueColour (bool, optional): print in true color. Defaults to True.
		char (str, optional): use this char for each pixel. Defaults to "\u2588".

	Returns:
	-------
		str: string to print

	"""
	char = "\u2588" if char in [None, ""] else char
	pixels, width, height = openImageToPx(imageName, maxLen)
	result = ["\x1b[2K\x1b[0m"]  # Clear line and reset
	beforeFgColour = None

	for h in range(height):
		for w in range(width):
			rgba = pixels[w, h]
			if rgba[3] != 0:
				result.append(genANSIpx(beforeFgColour, rgba[:3], trueColour=trueColour) + char)
				beforeFgColour = rgba[:3]
			else:
				result.append(genANSIpx(beforeFgColour, None, trueColour=trueColour) + " ")
				beforeFgColour = None

		if h + 1 != height:
			beforeFgColour = None
			result.append("\x1b[39m\n")

	return "".join(result)


def generateGreyscale(imageName: str, maxLen: int) -> str:
	"""Iterate through image pixels to make a printable string.

	Args:
	----
		imageName (str): path of the image on the filesystem (relative of absolute)
		maxLen (int): maximum of width and height in chars

	Returns:
	-------
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


def handleArgs(args: argparse.Namespace) -> None:  # pragma: no cover
	"""Handle arguments from the CLI / GUI.

	Args:
	----
		args (argparse.Namespace): arguments

	"""
	if args.url:
		urllib.request.urlretrieve(args.image, "downloadedImage.jpg")
		args.image = "downloadedImage.jpg"

	maxLen = 130 if args.big else 78
	if not args.greyscale and not args.regular:
		generateHDColour(args.image, maxLen, trueColour=not args.disable_truecolour, char=args.char)
	elif not args.greyscale and args.regular:
		generateColour(args.image, maxLen, trueColour=not args.disable_truecolour, char=args.char)
	else:
		generateGreyscale(args.image, maxLen)


@Cli2Gui(run_function=handleArgs, image=THISDIR + "/program_icon.png", program_name="CatImage")
def cli() -> None:  # pragma: no cover
	"""CLI entry point."""
	parser = argparse.ArgumentParser(description="cat an image to the terminal")
	parser.add_argument(
		"image",
		type=str,
		help="image file or URL",
	)
	parser.add_argument(
		"-u",
		"--url",
		action="store_true",
		help="image is a URL",
	)
	parser.add_argument(
		"-b",
		"--big",
		action="store_true",
		help="big image",
	)
	parser.add_argument(
		"-c",
		"--char",
		action="store",
		help="char to use in color print use $'chr' for escaped chars",
	)
	parser.add_argument(
		"-t",
		"--disable-truecolour",
		action="store_true",
		help="disable output in true color",
	)

	group = parser.add_argument_group(
		"choose one of the following", "use the following arguments to change the look of the image"
	)
	mxg = group.add_mutually_exclusive_group()
	mxg.add_argument(
		"-g",
		"--greyscale",
		action="store_true",
		help="output image in grayscale (best for terminals that cannot handle ANSI)",
	)
	mxg.add_argument(
		"-r",
		"--regular",
		action="store_true",
		help="output image in regular definition",
	)

	args = parser.parse_args()
	handleArgs(args)


if __name__ == "__main__":  # pragma: no cover
	cli()
