Module catimage.catimage
========================
Author: Fredhappyface
Date: 2020/02/19

Cat an image to the console. Inspired by img2txt
https://github.com/hit9/img2txt.git by Chao Wang

Functions
---------


`Cli2Gui(*args: Any, **kwargs: Any)`
:


`cli(*args: Any, **kwargs: Any)`
:


`genANSIpx(beforeColour: Union[None, int, tuple[int, ...]], colour: Union[None, int, tuple[int, ...]], bg: bool = False, trueColour: bool = True) ‑> str`
:   Generate the ansi escape string for a set of pixels with the same
    colour

    Args:
            beforeColour (Union[None, int, tuple[int, ...]]): previous colour
            colour (Union[None, int, tuple[int, ...]]): current colour
            bg (bool, optional): ansi background char. Defaults to False.
            trueColour (bool, optional): print in true colour. Defaults to True.

    Returns:
            str: string to represent char colour


`generateColour(imageName: str, maxLen: int, trueColour: bool = True, char: str = '█')`
:   Iterate through all of the pixels in an image and construct a printable
    string

    Args:
            imageName (str): path of the image on the filesystem (relative of
            absolute)
            maxLen (int): maximum of width and height in chars
            trueColour (bool, optional): print in true colour. Defaults to True.
            char (str, optional): use this char for each pixel. Defaults to "█".

    Returns:
            str: string to print


`generateGreyscale(imageName: str, maxLen: int)`
:   Iterate through image pixels to make a printable string

    Args:
            imageName (str): path of the image on the filesystem (relative of
            absolute)
            maxLen (int): maximum of width and height in chars

    Returns:
            str: string to print


`generateHDColour(imageName: str, maxLen: int, trueColour: bool = True, char: str = '▄') ‑> str`
:   Iterate through image pixels to make a printable string

    Args:
            imageName (str): path of the image on the filesystem (relative of
            absolute)
            maxLen (int): maximum of width and height in chars
            trueColour (bool, optional): print in true colour. Defaults to True.
            char (str, optional): use this char for each pixel. Defaults to "▄".

    Returns:
            str: string to print


`getANSIColour(rgb: tuple[int, ...]) ‑> int`
:   Generate the ansi escape code based on the pixel value

    Args:
            rgb (tuple[int, ...]): int array with pixel rgb values: [r, g, b]

    Returns:
            int: ansi escape code for the colour


`handleArgs(args: argparse.Namespace)`
:   Handle arguments from the cli/ gui

    Args:
            args (argparse.Namespace): arguments


`openImageToPx(imageName: str, maxLen: int, hd: bool = False) ‑> tuple`
:   Get an array of pixels and the dimensions of these

    Args:
            imageName (str): path of the image on the filesystem (relative of
            absolute)
            maxLen (int): maximum of width and height in chars
            hd (bool, optional): get 'hd' array of pixels. Defaults to False.

    Returns:
            int[][], int, int: 2d array of pixels, and the dimensions of the image
