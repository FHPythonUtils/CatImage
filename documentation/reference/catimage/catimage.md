# Catimage

[Catimage Index](../README.md#catimage-index) / [Catimage](./index.md#catimage) / Catimage

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

[Show source in catimage.py:24](../../../catimage/catimage.py#L24)

#### Signature

```python
def Cli2Gui(*args: Any, **kwargs: Any): ...
```



## cli

[Show source in catimage.py:270](../../../catimage/catimage.py#L270)

CLI entry point.

#### Signature

```python
@Cli2Gui(
    run_function=handleArgs, image=THISDIR + "/program_icon.png", program_name="CatImage"
)
def cli() -> None: ...
```



## genANSIpx

[Show source in catimage.py:91](../../../catimage/catimage.py#L91)

Generate the ANSI escape string for a set of pixels with the same color.

#### Arguments

----
 beforeColour (Optional[Union[int, tuple[int, ...]]]): previous color
 colour (Optional[Union[int, tuple[int, ...]]]): current color
 - `bg` *bool, optional* - ANSI background char. Defaults to False.
 - `trueColour` *bool, optional* - print in true color. Defaults to True.

#### Returns

-------
 - `str` - string to represent char color

#### Signature

```python
def genANSIpx(
    beforeColour: int | tuple[int, ...] | None,
    colour: int | tuple[int, ...] | None,
    bg: bool = False,
    trueColour: bool = True,
) -> str: ...
```



## generateColour

[Show source in catimage.py:183](../../../catimage/catimage.py#L183)

Iterate through all of the pixels in an image and construct a printable string.

#### Arguments

----
 - `imageName` *str* - path of the image on the filesystem (relative of absolute)
 - `maxLen` *int* - maximum of width and height in chars
 - `trueColour` *bool, optional* - print in true color. Defaults to True.
 - `char` *str, optional* - use this char for each pixel. Defaults to "█".

#### Returns

-------
 - `str` - string to print

#### Signature

```python
def generateColour(
    imageName: str, maxLen: int, trueColour: bool = True, char: str = "█"
) -> str: ...
```



## generateGreyscale

[Show source in catimage.py:222](../../../catimage/catimage.py#L222)

Iterate through image pixels to make a printable string.

#### Arguments

----
 - `imageName` *str* - path of the image on the filesystem (relative of absolute)
 - `maxLen` *int* - maximum of width and height in chars

#### Returns

-------
 - `str` - string to print

#### Signature

```python
def generateGreyscale(imageName: str, maxLen: int) -> str: ...
```



## generateHDColour

[Show source in catimage.py:130](../../../catimage/catimage.py#L130)

Iterate through image pixels to make a printable string.

#### Arguments

----
 - `imageName` *str* - path of the image on the filesystem (relative of absolute)
 - `maxLen` *int* - maximum of width and height in chars
 - `trueColour` *bool, optional* - print in true color. Defaults to True.
 - `char` *str, optional* - use this char for each pixel. Defaults to "▄".

#### Returns

-------
 - `str` - string to print

#### Signature

```python
def generateHDColour(
    imageName: str, maxLen: int, trueColour: bool = True, char: str = "▄"
) -> str: ...
```



## getANSIColour

[Show source in catimage.py:73](../../../catimage/catimage.py#L73)

Generate the ANSI escape code based on the pixel value.

#### Arguments

----
 rgb (tuple[int, ...]): int array with pixel RGB values: [r, g, b]

#### Returns

-------
 - `int` - ANSI escape code for the color

#### Signature

```python
def getANSIColour(rgb: tuple[int, ...]) -> int: ...
```



## handleArgs

[Show source in catimage.py:249](../../../catimage/catimage.py#L249)

Handle arguments from the CLI / GUI.

#### Arguments

----
 - `args` *argparse.Namespace* - arguments

#### Signature

```python
def handleArgs(args: argparse.Namespace) -> None: ...
```



## openImageToPx

[Show source in catimage.py:44](../../../catimage/catimage.py#L44)

Get an array of pixels and the dimensions of these.

#### Arguments

----
 - `imageName` *str* - path of the image on the filesystem (relative of absolute)
 - `maxLen` *int* - maximum of width and height in chars
 - `hd` *bool, optional* - get 'hd' array of pixels. Defaults to False.

#### Returns

-------
 tuple[Any, int, int]: 2D array of pixels, and the dimensions of the image

#### Signature

```python
def openImageToPx(
    imageName: str, maxLen: int, hd: bool = False
) -> tuple[Any, int, int]: ...
```