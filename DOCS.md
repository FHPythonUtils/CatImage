<a name=".catimage"></a>
## catimage

Cat an image to the terminal.

<a name=".catimage.catimage"></a>
## catimage.catimage

Author: Fredhappyface
Date: 2020/02/19

Cat an image to the console. Inspired by img2txt
https://github.com/hit9/img2txt.git by Chao Wang

<a name=".catimage.catimage.openImageToPx"></a>
#### openImageToPx

```python
openImageToPx(imageName, maxLen, hd=False)
```

Get an array of pixels and the dimensions of these

**Arguments**:

- `imageName` _str_ - path of the image on the filesystem (relative of
  absolute)
- `maxLen` _int_ - maximum of width and height in chars
- `hd` _bool, optional_ - get 'hd' array of pixels. Defaults to False.
  

**Returns**:

  int[][], int, int: 2d array of pixels, and the dimensions of the image

<a name=".catimage.catimage.getANSIColour"></a>
#### getANSIColour

```python
getANSIColour(rgb)
```

Generate the ansi escape code based on the pixel value

**Arguments**:

- `rgb` _int[]_ - int array with pixel rgb values: [r, g, b]
  

**Returns**:

- `int` - ansi escape code for the colour

<a name=".catimage.catimage.genANSIpx"></a>
#### genANSIpx

```python
genANSIpx(beforeColour, colour, bg=False, trueColour=True)
```

Generate the ansi escape string for a set of pixels with the same
colour

**Arguments**:

- `beforeColour` _int_ - previous colour
- `colour` _int_ - current colour
- `bg` _bool, optional_ - ansi background char. Defaults to False.
- `trueColour` _bool, optional_ - print in true colour. Defaults to True.
  

**Returns**:

- `str` - string to represent char colour

<a name=".catimage.catimage.generateHDColour"></a>
#### generateHDColour

```python
generateHDColour(imageName, maxLen, trueColour=True, char="\u2584")
```

Iterate through image pixels to make a printable string

**Arguments**:

- `imageName` _str_ - path of the image on the filesystem (relative of
  absolute)
- `maxLen` _int_ - maximum of width and height in chars
- `trueColour` _bool, optional_ - print in true colour. Defaults to True.
- `char` _str, optional_ - use this char for each pixel. Defaults to "\u2584".
  

**Returns**:

- `str` - string to print

<a name=".catimage.catimage.generateColour"></a>
#### generateColour

```python
generateColour(imageName, maxLen, trueColour=True, char="\u2588")
```

Iterate through all of the pixels in an image and construct a printable
string

**Arguments**:

- `imageName` _str_ - path of the image on the filesystem (relative of
  absolute)
- `maxLen` _int_ - maximum of width and height in chars
- `trueColour` _bool, optional_ - print in true colour. Defaults to True.
- `char` _str, optional_ - use this char for each pixel. Defaults to "\u2588".
  

**Returns**:

- `str` - string to print

<a name=".catimage.catimage.generateGreyscale"></a>
#### generateGreyscale

```python
generateGreyscale(imageName, maxLen)
```

Iterate through image pixels to make a printable string

**Arguments**:

- `imageName` _str_ - path of the image on the filesystem (relative of
  absolute)
- `maxLen` _int_ - maximum of width and height in chars
  

**Returns**:

- `str` - string to print

<a name=".catimage.catimage.handleArgs"></a>
#### handleArgs

```python
handleArgs(args)
```

Handle arguments from the cli/ gui

**Arguments**:

- `args` _argparse_ - arguments

<a name=".catimage.catimage.cli"></a>
#### cli

```python
@Cli2Gui(run_function=handleArgs, image=THISDIR + os.sep + "program_icon.png", program_name="CatImage")
cli()
```

CLI entry point

<a name=".catimage.__main__"></a>
## catimage.\_\_main\_\_

Cat an image to the terminal. Main entry point for cli

<a name=".make"></a>
## make

Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build

