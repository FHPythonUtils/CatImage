#!/usr/bin/env python3
"""
Author: Fredhappyface
Date: 2020/02/19

Cat an image to the console. Inspired by img2txt
https://github.com/hit9/img2txt.git by Chao Wang
"""

import argparse
from PIL import Image
import platform
import urllib.request
import os


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

def genANSIpx(beforeFgColour, colour):
	"""Generate the ansi escape string for a set of pixels with the same
	colour

	Args:
		beforeFgColour (int): previous colour
		colour (int): current colour

	Returns:
		str: string to represent char colour
	"""
	colourArr = []

	if colour != beforeFgColour:
		if colour is None:
			colourArr.append("39")
		else:
			colourArr += ["38", "5", str(colour)]
	if len(colourArr) > 0:
		return "\x1b[" + ";".join(colourArr) + "m"
	else:
		return ""

def generateColour(pixels, width, height, char="\u2588"):
	"""Iterate through all of the pixels in an image and construct a printable
	string

	Args:
		pixels (int[][]): 2d array of pixels these are int[]
		width (int): image width
		height (int): image height
		char (str, optional): use this char for each pixel. Defaults to "\u2588".

	Returns:
		str: string to print
	"""
	result = "\x1b[0m"
	beforeFgColour = None
	for h in range(height):
		for w in range(width):
			rgba = pixels[w, h]
			if rgba[3] != 0:
				rgb = rgba[:3]
				colour = getANSIColour(rgb)
				result += genANSIpx(beforeFgColour, colour) + char
				beforeFgColour = colour
			else:
				result += genANSIpx(beforeFgColour, None) + " "
				beforeFgColour = "\x1b[49m"
		if h+1 != height:
			beforeFgColour = "\x1b[49m"
			result += "\n"
	return result



def generateGreyscale(pixels, width, height):
	"""Iterate through image pixels to make a printable string

	Args:
		pixels (int[][]): 2d array of pixels these are int[]
		width (int): image width
		height (int): image height

	Returns:
		str: string to print
	"""
	result = ""
	color = " .;-:!>7?CO$QHNM"
	for h in range(height):
		for w in range(width):
			rgba = pixels[w, h]
			rgb = rgba[:3]
			result += color[int(sum(rgb) / 3.0 / 256.0 * 16)]
		result += "\n"
	return result


def catImage(imageName, maxLen, colour, char):
	image = Image.open(imageName)
	image = image.convert("RGBA")
	initW, initH = image.size
	columns, rows = os.get_terminal_size(0)
	scale = maxLen / max(initH, initW)
	width = int(scale * initW)*2
	height = int(scale * initH)
	image = image.resize((width, height))
	pixels = image.load()
	if colour:
		result = "\x1b[49m\x1b[K" + generateColour(pixels, width, height, char)
	else:
		result = generateGreyscale(pixels, width, height)

	print(result)

if __name__ == "__main__": # pragma: no cover
	parser = argparse.ArgumentParser(description="cat an image")
	parser.add_argument("image", type=str, nargs=1, help="image file or url")
	parser.add_argument("-g", "--greyscale", help="image in greyscale (as opposed to colour?)", action="store_true")
	parser.add_argument("-u", "--url", help="image is url (as opposed to file?)", action="store_true")
	parser.add_argument("-c", "--char", help="char to use in colour print", action="store")
	parser.add_argument("-b", "--big", help="big image?", action="store_true")

	args = parser.parse_args()
	args.image = args.image[0]

	if args.char is None:
		args.char = "\u2588"


	if args.url:
		urllib.request.urlretrieve(args.image, "dowloadedImage.jpg")
		args.image = "dowloadedImage.jpg"

	os.path.exists(args.image)
	catImage(args.image, 50 if args.big else 35, not args.greyscale, args.char)
