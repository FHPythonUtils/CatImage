#!/usr/bin/env python3
"""
Author: Fredhappyface
Date: 2020/02/19

Cat an image to the console. Inspired by img2txt
https://github.com/hit9/img2txt.git by Chao Wang
"""

import platform
import urllib.request
import os
import ctypes
import argparse
from pathlib import Path

from PIL import Image
from cli2gui import Cli2Gui

THISDIR = str(Path(__file__).resolve().parent)

def openImageToPx(imageName, maxLen, hd=False):
	"""Get an array of pixels and the dimensions of these

	Args:
		imageName (str): path of the image on the filesystem (relative of
		absolute)
		maxLen (int): maximum of width and height in chars
		hd (bool, optional): get 'hd' array of pixels. Defaults to False.

	Returns:
		int[][], int, int: 2d array of pixels, and the dimensions of the image
	"""
	image = Image.open(imageName).convert("RGBA")
	initW, initH = image.size
	scale = maxLen / max(initH, initW)
	width = int(scale * initW)
	height = int(scale * initH/ (1 if hd else 2))
	image = image.resize((width, height))
	pixels = image.load()
	return pixels, width, height


def getANSIColour(rgb):
	"""Generate the ansi escape code based on the pixel value

	Args:
		rgb (int[]): int array with pixel rgb values: [r, g, b]

	Returns:
		int: ansi escape code for the colour
	"""
	websafeR = int(round((rgb[0] / 255.0) * 5))
	websafeG = int(round((rgb[1] / 255.0) * 5))
	websafeB = int(round((rgb[2] / 255.0) * 5))
	return int(((websafeR * 36) + (websafeG * 6) + websafeB) + 16)

def genANSIpx(beforeColour, colour, bg=False, trueColour=True):
	"""Generate the ansi escape string for a set of pixels with the same
	colour

	Args:
		beforeColour (int): previous colour
		colour (int): current colour
		bg (bool, optional): ansi background char. Defaults to False.
		trueColour (bool, optional): print in true colour. Defaults to True.

	Returns:
		str: string to represent char colour
	"""
	colourArr = []

	if not trueColour:
		beforeColour = getANSIColour(beforeColour) if beforeColour is not None else None
		colour = getANSIColour(colour) if colour is not None else None

	if colour != beforeColour:
		if colour is None:
			colourArr.append("49" if bg else "39")
		elif not trueColour:
			colourArr += ["48" if bg else "38", "5", str(colour)]
		else:
			colourArr += ["48" if bg else "38", "2", str(colour[0]), str(colour[1]), str(colour[2])]
	return "\x1b[" + ";".join(colourArr) + "m" if len(colourArr) > 0 else ""


def generateHDColour(imageName, maxLen, trueColour=True, char="\u2584"):
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
	result = "\x1b[2K\x1b[0m" # Clear line and reset
	beforeFgColour = None
	beforeBgColour = None
	for h in range(0, height, 2):
		for w in range(width):
			rgbaBg = pixels[w, h]
			try:
				rgbaFg = pixels[w, h+1]
			except IndexError:
				rgbaFg = pixels[w, h]
			if rgbaBg[3] != 0:
				result += genANSIpx(beforeBgColour, rgbaBg[:3], True, trueColour=trueColour)
				beforeBgColour = rgbaBg[:3]
			else:
				result += genANSIpx(beforeBgColour, None, True, trueColour=trueColour)
				beforeBgColour = None
			if rgbaFg[3] != 0:
				result += genANSIpx(beforeFgColour, rgbaFg[:3], trueColour=trueColour) + char
				beforeFgColour = rgbaFg[:3]
			else:
				result += genANSIpx(beforeFgColour, None, trueColour=trueColour) + " "
				beforeFgColour = None
		if h+1 != height:
			beforeFgColour = None
			beforeBgColour = None
			result += "\x1b[39m\x1b[49m\n"

	return result

def generateColour(imageName, maxLen, trueColour=True, char="\u2588"):
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
	result = "\x1b[2K\x1b[0m" # Clear line and reset
	beforeFgColour = None
	for h in range(height):
		for w in range(width):
			rgba = pixels[w, h]
			if rgba[3] != 0:
				result += genANSIpx(beforeFgColour, rgba[:3], trueColour=trueColour) + char
				beforeFgColour = rgba[:3]
			else:
				result += genANSIpx(beforeFgColour, None, trueColour=trueColour) + " "
				beforeFgColour = None
		if h+1 != height:
			beforeFgColour = None
			result += "\x1b[39m\n"
	return result



def generateGreyscale(imageName, maxLen):
	"""Iterate through image pixels to make a printable string

	Args:
		imageName (str): path of the image on the filesystem (relative of
		absolute)
		maxLen (int): maximum of width and height in chars

	Returns:
		str: string to print
	"""
	pixels, width, height = openImageToPx(imageName, maxLen)
	result = ""
	color = " .;-:!>7?CO$QHNM"
	for h in range(height):
		for w in range(width):
			rgba = pixels[w, h]
			rgb = rgba[:3]
			result += color[int(sum(rgb) / 3.0 / 256.0 * 16)]
		result += "\n"
	return result



def handleArgs(args):
	"""Handle arguments from the cli/ gui

	Args:
		args (argparse): arguments
	"""
	if args.url:
		urllib.request.urlretrieve(args.image, "dowloadedImage.jpg")
		args.image = "dowloadedImage.jpg"

	if platform.system() == "Windows":
		kernel32 = ctypes.windll.kernel32
		kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

	os.path.exists(args.image)

	maxLen = 130 if args.big else 78
	if not args.greyscale and not args.regular:
		result = generateHDColour(args.image, maxLen, not args.disable_truecolour, args.char)
	elif not args.greyscale and args.regular:
		result = generateColour(args.image, maxLen, not args.disable_truecolour, args.char)
	else:
		result = generateGreyscale(args.image, maxLen)
	print(result)

@Cli2Gui(run_function=handleArgs, image=THISDIR + os.sep + "program_icon.png", program_name="CatImage")
def cli(): # pragma: no cover
	parser = argparse.ArgumentParser(description="cat an image to the terminal")
	parser.add_argument("image", type=str,
		help="image file or url")
	parser.add_argument("-u", "--url", action="store_true",
		help="image is a URL")
	parser.add_argument("-b", "--big", action="store_true",
		help="big image")
	parser.add_argument("-c", "--char", action="store",
		help="char to use in colour print use $'chr' for escaped chars")
	parser.add_argument("-t", "--disable-truecolour", action="store_true",
		help="disable output in truecolour")

	group = parser.add_argument_group("choose one of the following",
		"use the following arguments to change the look of the image")
	mxg = group.add_mutually_exclusive_group()
	mxg.add_argument("-g", "--greyscale", action="store_true",
		help="output image in greyscale (best for terminals that cannot handle ANSI)")
	mxg.add_argument("-r", "--regular", action="store_true",
		help="output image in regular definition")

	args = parser.parse_args()

	handleArgs(args)


if __name__ == "__main__": # pragma: no cover
	cli()
