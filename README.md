[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/CatImage.svg?style=for-the-badge&cacheSeconds=28800)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/CatImage.svg?style=for-the-badge&cacheSeconds=28800)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/CatImage.svg?style=for-the-badge&cacheSeconds=28800)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/CatImage.svg?style=for-the-badge&cacheSeconds=28800)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/CatImage.svg?style=for-the-badge&cacheSeconds=28800)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/catimage.svg?style=for-the-badge&cacheSeconds=28800)](https://pypistats.org/packages/catimage)
[![PyPI Total Downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=total%20downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi%2Epepy%2Etech%2Fapi%2Fv2%2Fprojects%2Fcatimage)](https://pepy.tech/project/catimage)
[![PyPI Version](https://img.shields.io/pypi/v/catimage.svg?style=for-the-badge&cacheSeconds=28800)](https://pypi.org/project/catimage)

<!-- omit in toc -->
# CatImage

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

Cat an image to the terminal.

- [Example](#example)
- [How To Use](#how-to-use)
- [Documentation](#documentation)
- [Install Single Script](#install-single-script)
	- [Wget](#wget)
	- [Curl](#curl)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Windows - Python.org](#windows---pythonorg)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
	- [Dnf](#dnf)
- [Install Python on MacOS](#install-python-on-macos)
	- [Homebrew](#homebrew)
	- [MacOS - Python.org](#macos---pythonorg)
- [How to run](#how-to-run)
	- [Windows](#windows)
	- [Linux/ MacOS](#linux-macos)
- [Building](#building)
- [Testing](#testing)
- [Download Project](#download-project)
	- [Clone](#clone)
		- [Using The Command Line](#using-the-command-line)
		- [Using GitHub Desktop](#using-github-desktop)
	- [Download Zip File](#download-zip-file)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)
	- [Support](#support)
	- [Rationale](#rationale)
- [Screenshots](#screenshots)
	- [Desktop](#desktop)

## Example

Original Image:

<img src="readme-assets/screenshots/desktop/example-0.png" alt="Screenshot 1" width="600">

Greyscale Image:

```python
./catimage.py readme-assets/screenshots/desktop/example-0.png -g
```

<img src="readme-assets/screenshots/desktop/example-1.png" alt="Screenshot 2" width="600">

Regular Definition Image:

```python
./catimage.py readme-assets/screenshots/desktop/example-0.png -r -t
```

<img src="readme-assets/screenshots/desktop/example-2.png" alt="Screenshot 3" width="600">

Regular Definition Image with '@':

```python
./catimage.py readme-assets/screenshots/desktop/example-0.png -r -c @ -t
```

<img src="readme-assets/screenshots/desktop/example-3.png" alt="Screenshot 4" width="600">

HD Image:

```python
./catimage.py readme-assets/screenshots/desktop/example-0.png -t
```

<img src="readme-assets/screenshots/desktop/example-4.png" alt="Screenshot 5" width="600">

HD Image with right half block:

```python
./catimage.py readme-assets/screenshots/desktop/example-0.png -c $'\u2590' -t
```

<img src="readme-assets/screenshots/desktop/example-5.png" alt="Screenshot 6" width="600">

HD Image True Colour:

```python
./catimage.py readme-assets/screenshots/desktop/example-0.png
```

<img src="readme-assets/screenshots/desktop/example-6.png" alt="Screenshot 7" width="600">

## How To Use

Use to cat an image to the terminal, see the help text below for more
information on using this tool from the command line:

```bash
usage: catimage [-h] [-u] [-b] [-c CHAR] [-t] [-g | -r] image

cat an image to the terminal

positional arguments:
  image                 image file or url

optional arguments:
  -h, --help            show this help message and exit
  -u, --url             image is a URL
  -b, --big             big image
  -c CHAR, --char CHAR  char to use in colour print use $'chr' for escaped chars
  -t, --disable-truecolour
                        disable output in truecolour

choose one of the following:
  use the following arguments to change the look of the image

  -g, --greyscale       output image in greyscale (best for terminals that cannot handle ANSI)
  -r, --regular         output image in regular definition
```

GUI

Use the --cli2gui flag to launch a GUI

<div>
<img src="readme-assets/screenshots/desktop/gui-0.png" alt="GUI 1" width="600">
<img src="readme-assets/screenshots/desktop/gui-1.png" alt="GUI 2" width="600">
</div>

Alternatively, import into your project and use:

```python
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

def generateGreyscale(imageName, maxLen):
	"""Iterate through image pixels to make a printable string

	Args:
		imageName (str): path of the image on the filesystem (relative of
		absolute)
		maxLen (int): maximum of width and height in chars

	Returns:
		str: string to print
	"""
```

## Documentation

A high-level overview of how the documentation is organized organized will help you know
where to look for certain things:

<!--
- [Tutorials](/documentation/tutorials) take you by the hand through a series of steps to get
  started using the software. Start here if you’re new.
-->
- The [Technical Reference](/documentation/reference) documents APIs and other aspects of the
  machinery. This documentation describes how to use the classes and functions at a lower level
  and assume that you have a good high-level understanding of the software.
<!--
- The [Help](/documentation/help) guide provides a starting point and outlines common issues that you
  may have.
-->

## Install Single Script

### Wget

```bash
wget -O /usr/bin/catimage https://raw.githubusercontent.com/FHPythonUtils/CatImage/master/catimage.py && sudo chmod 774 /usr/bin/catimage
```

### Curl

```bash
curl -o /usr/bin/catimage https://raw.githubusercontent.com/FHPythonUtils/CatImage/master/catimage.py && sudo chmod 774 /usr/bin/catimage
```

## Install With PIP

```python
pip install catimage
```

Head to https://pypi.org/project/catimage/ for more info

## Language information

### Built for

This program has been written for Python versions 3.8 - 3.11 and has been tested with both 3.8 and
3.11

## Install Python on Windows

### Chocolatey

```powershell
choco install python
```

### Windows - Python.org

To install Python, go to https://www.python.org/downloads/windows/ and download the latest
version.

## Install Python on Linux

### Apt

```bash
sudo apt install python3.x
```

### Dnf

```bash
sudo dnf install python3.x
```

## Install Python on MacOS

### Homebrew

```bash
brew install python@3.x
```

### MacOS - Python.org

To install Python, go to https://www.python.org/downloads/macos/ and download the latest
version.

## How to run

### Windows

- Module
	`py -3.x -m [module]` or `[module]` (if module installs a script)

- File
	`py -3.x [file]` or `./[file]`

### Linux/ MacOS

- Module
	`python3.x -m [module]` or `[module]` (if module installs a script)

- File
	`python3.x [file]` or `./[file]`

## Building

This project uses https://github.com/FHPythonUtils/FHMake to automate most of the building. This
command generates the documentation, updates the requirements.txt and builds the library artefacts

Note the functionality provided by fhmake can be approximated by the following

```sh
handsdown  --cleanup -o documentation/reference
poetry export -f requirements.txt --output requirements.txt
poetry export -f requirements.txt --with dev --output requirements_optional.txt
poetry build
```

`fhmake audit` can be run to perform additional checks

## Testing

For testing with the version of python used by poetry use

```sh
poetry run pytest
```

Alternatively use `tox` to run tests over python 3.8 - 3.11

```sh
tox
```

## Download Project

### Clone

#### Using The Command Line

1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2
	```bash
	git clone https://github.com/FHPythonUtils/CatImage
	```

More information can be found at
https://help.github.com/en/articles/cloning-a-repository

#### Using GitHub Desktop

1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Community Files

### Licence

MIT License
Copyright (c) FredHappyface
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog

See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct

Online communities include people from many backgrounds. The *Project*
contributors are committed to providing a friendly, safe and welcoming
environment for all. Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md)
 for more information.

### Contributing

Contributions are welcome, please see the
[Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md)
for more information.

### Security

Thank you for improving the security of the project, please see the
[Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md)
for more information.

### Support

Thank you for using this project, I hope it is of use to you. Please be aware that
those involved with the project often do so for fun along with other commitments
(such as work, family, etc). Please see the
[Support Policy](https://github.com/FHPythonUtils/.github/blob/master/SUPPORT.md)
for more information.

### Rationale

The rationale acts as a guide to various processes regarding projects such as
the versioning scheme and the programming styles used. Please see the
[Rationale](https://github.com/FHPythonUtils/.github/blob/master/RATIONALE.md)
for more information.

## Screenshots

### Desktop

<div>
<img src="readme-assets/screenshots/desktop/screenshot-0.png" alt="Screenshot 1" width="600">
<img src="readme-assets/screenshots/desktop/screenshot-1.png" alt="Screenshot 2" width="600">
<img src="readme-assets/screenshots/desktop/screenshot-2.png" alt="Screenshot 3" width="600">
</div>
