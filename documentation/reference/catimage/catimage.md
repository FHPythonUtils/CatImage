# Catimage

> Auto-generated documentation for [catimage.catimage](../../../catimage/catimage.py) module.

Author: Fredhappyface
Date: 2020/02/19

- [Catimage](../README.md#catimage-index) / [Modules](../MODULES.md#catimage-modules) / [Catimage](index.md#catimage) / Catimage
    - [Cli2Gui](#cli2gui)
    - [cli](#cli)
    - [genANSIpx](#genansipx)
    - [generateColour](#generatecolour)
    - [generateGreyscale](#generategreyscale)
    - [generateHDColour](#generatehdcolour)
    - [getANSIColour](#getansicolour)
    - [handleArgs](#handleargs)
    - [openImageToPx](#openimagetopx)

Cat an image to the console. Inspired by img2txt
https://github.com/hit9/img2txt.git by Chao Wang

## Cli2Gui

[[find in source code]](../../../catimage/catimage.py#L26)

```python
def Cli2Gui(*args: Any, **kwargs: Any):
```

## cli

[[find in source code]](../../../catimage/catimage.py#L246)

```python
@Cli2Gui(
    run_function=handleArgs,
    image=THISDIR + '/program_icon.png',
    program_name='CatImage',
)
def cli():
```

CLI entry point

## genANSIpx

[[find in source code]](../../../catimage/catimage.py#L88)

```python
def genANSIpx(
    beforeColour: None | int | tuple[int, ...],
    colour: None | int | tuple[int, ...],
    bg: bool = False,
    trueColour: bool = True,
) -> str:
```

Generate the ansi escape string for a set of pixels with the same
colour

#### Arguments

beforeColour (Union[None, int, tuple[int, ...]]): previous colour
colour (Union[None, int, tuple[int, ...]]): current colour
- `bg` *bool, optional* - ansi background char. Defaults to False.
- `trueColour` *bool, optional* - print in true colour. Defaults to True.

#### Returns

- `str` - string to represent char colour

## generateColour

[[find in source code]](../../../catimage/catimage.py#L170)

```python
def generateColour(
    imageName: str,
    maxLen: int,
    trueColour: bool = True,
    char: str = '█',
):
```

Iterate through all of the pixels in an image and construct a printable
string

#### Arguments

- `imageName` *str* - path of the image on the filesystem (relative of
absolute)
- `maxLen` *int* - maximum of width and height in chars
- `trueColour` *bool, optional* - print in true colour. Defaults to True.
- `char` *str, optional* - use this char for each pixel. Defaults to "█".

#### Returns

- `str` - string to print

## generateGreyscale

[[find in source code]](../../../catimage/catimage.py#L203)

```python
def generateGreyscale(imageName: str, maxLen: int):
```

Iterate through image pixels to make a printable string

#### Arguments

- `imageName` *str* - path of the image on the filesystem (relative of
absolute)
- `maxLen` *int* - maximum of width and height in chars

#### Returns

- `str` - string to print

## generateHDColour

[[find in source code]](../../../catimage/catimage.py#L123)

```python
def generateHDColour(
    imageName: str,
    maxLen: int,
    trueColour: bool = True,
    char: str = '▄',
) -> str:
```

Iterate through image pixels to make a printable string

#### Arguments

- `imageName` *str* - path of the image on the filesystem (relative of
absolute)
- `maxLen` *int* - maximum of width and height in chars
- `trueColour` *bool, optional* - print in true colour. Defaults to True.
- `char` *str, optional* - use this char for each pixel. Defaults to "▄".

#### Returns

- `str` - string to print

## getANSIColour

[[find in source code]](../../../catimage/catimage.py#L73)

```python
def getANSIColour(rgb: tuple[int, ...]) -> int:
```

Generate the ansi escape code based on the pixel value

#### Arguments

rgb (tuple[int, ...]): int array with pixel rgb values: [r, g, b]

#### Returns

- `int` - ansi escape code for the colour

## handleArgs

[[find in source code]](../../../catimage/catimage.py#L226)

```python
def handleArgs(args: argparse.Namespace):
```

Handle arguments from the cli/ gui

#### Arguments

- `args` *argparse.Namespace* - arguments

## openImageToPx

[[find in source code]](../../../catimage/catimage.py#L45)

```python
def openImageToPx(
    imageName: str,
    maxLen: int,
    hd: bool = False,
) -> tuple[Any, int, int]:
```

Get an array of pixels and the dimensions of these

#### Arguments

- `imageName` *str* - path of the image on the filesystem (relative of
absolute)
- `maxLen` *int* - maximum of width and height in chars
- `hd` *bool, optional* - get 'hd' array of pixels. Defaults to False.

#### Returns

int[][], int, int: 2d array of pixels, and the dimensions of the image
