# Catimage

[Catimage Index](../README.md#catimage-index) /
[Catimage](./index.md#catimage) /
Catimage

> Auto-generated documentation for [catimage.catimage](../../../catimage/catimage.py) module.

- [Catimage](#catimage)
  - [Cli2Gui](#cli2gui)
  - [cli](#cli)
  - [genANSIpx](#genansipx)
  - [generateColour](#generatecolour)
  - [generateGreyscale](#generategreyscale)
  - [generateHDColour](#generatehdcolour)
  - [getANSIColour](#getansicolour)
  - [handleArgs](#handleargs)
  - [openImageToPx](#openimagetopx)

## Cli2Gui

[Show source in catimage.py:23](../../../catimage/catimage.py#L23)

#### Signature

```python
def Cli2Gui(*args: Any, **kwargs: Any):
    ...
```



## cli

[Show source in catimage.py:242](../../../catimage/catimage.py#L242)

CLI entry point

#### Signature

```python
@Cli2Gui(
    run_function=handleArgs, image=THISDIR + "/program_icon.png", program_name="CatImage"
)
def cli():
    ...
```



## genANSIpx

[Show source in catimage.py:82](../../../catimage/catimage.py#L82)

Generate the ansi escape string for a set of pixels with the same
colour

#### Arguments

beforeColour (Union[None, int, tuple[int, ...]]): previous colour
colour (Union[None, int, tuple[int, ...]]): current colour
- `bg` *bool, optional* - ansi background char. Defaults to False.
- `trueColour` *bool, optional* - print in true colour. Defaults to True.

#### Returns

- `str` - string to represent char colour

#### Signature

```python
def genANSIpx(
    beforeColour: None | int | tuple[int, ...],
    colour: None | int | tuple[int, ...],
    bg: bool = False,
    trueColour: bool = True,
) -> str:
    ...
```



## generateColour

[Show source in catimage.py:164](../../../catimage/catimage.py#L164)

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

#### Signature

```python
def generateColour(
    imageName: str, maxLen: int, trueColour: bool = True, char: str = "█"
) -> str:
    ...
```



## generateGreyscale

[Show source in catimage.py:199](../../../catimage/catimage.py#L199)

Iterate through image pixels to make a printable string

#### Arguments

- `imageName` *str* - path of the image on the filesystem (relative of
absolute)
- `maxLen` *int* - maximum of width and height in chars

#### Returns

- `str` - string to print

#### Signature

```python
def generateGreyscale(imageName: str, maxLen: int) -> str:
    ...
```



## generateHDColour

[Show source in catimage.py:117](../../../catimage/catimage.py#L117)

Iterate through image pixels to make a printable string

#### Arguments

- `imageName` *str* - path of the image on the filesystem (relative of
absolute)
- `maxLen` *int* - maximum of width and height in chars
- `trueColour` *bool, optional* - print in true colour. Defaults to True.
- `char` *str, optional* - use this char for each pixel. Defaults to "▄".

#### Returns

- `str` - string to print

#### Signature

```python
def generateHDColour(
    imageName: str, maxLen: int, trueColour: bool = True, char: str = "▄"
) -> str:
    ...
```



## getANSIColour

[Show source in catimage.py:67](../../../catimage/catimage.py#L67)

Generate the ansi escape code based on the pixel value

#### Arguments

rgb (tuple[int, ...]): int array with pixel rgb values: [r, g, b]

#### Returns

- `int` - ansi escape code for the colour

#### Signature

```python
def getANSIColour(rgb: tuple[int, ...]) -> int:
    ...
```



## handleArgs

[Show source in catimage.py:222](../../../catimage/catimage.py#L222)

Handle arguments from the cli/ gui

#### Arguments

- `args` *argparse.Namespace* - arguments

#### Signature

```python
def handleArgs(args: argparse.Namespace):
    ...
```



## openImageToPx

[Show source in catimage.py:42](../../../catimage/catimage.py#L42)

Get an array of pixels and the dimensions of these

#### Arguments

- `imageName` *str* - path of the image on the filesystem (relative of
absolute)
- `maxLen` *int* - maximum of width and height in chars
- `hd` *bool, optional* - get 'hd' array of pixels. Defaults to False.

#### Returns

int[][], int, int: 2d array of pixels, and the dimensions of the image

#### Signature

```python
def openImageToPx(imageName: str, maxLen: int, hd: bool = False) -> tuple[Any, int, int]:
    ...
```


