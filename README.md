# color-ascii-art-py

Generate a color ASCII art picture. Designed for CLIs with access to background and foreground coloring.

Written and tested in Python version [3.12.7](https://www.python.org/downloads/release/python-3127/) on Windows 10/11. Scripts are not guaranteed to run as intended on other versions or operating systems!

## Installation

color-ascii-art-py scripts are *NOT* executable binaries. They are Python scripts, meant to be individually downloaded and run.

### Find a Suitable Script

There are multiple scripts in which color-ascii-art-py takes form.

1. Download `by-img.py` from [the latest release](https://github.com/9730886/color-ascii-art-py/releases) for generating art by individual image.
2. Download `by-dir.py` from [the latest release](https://github.com/9730886/color-ascii-art-py/releases) for generating art by images in directory.

> If you have a single directory of the images you want to generate art of, you may find it easier to place the script in that directory.

### Runtime Dependencies
 - os
 - [Pillow (Python Imaging Library Fork)](https://github.com/python-pillow/Pillow)

## Usage

### Runtime

Scripts have only been debugged and utilized in [Python IDLE](https://docs.python.org/3/library/idle.html). The scripts may or may not function as intended inside a console.

### Color-coding

By default, the script will use the following format to generate color codes:

`` `rG# ``

1. The first character is defined as the `COLOR_INDICATOR` constant in the script. It indicates that a foreground and background color is about to be defined.
2. The second character is the foreground color. It will always be in lowercase.
3. The third character is the background color. It will always be in uppercase.
4. The fourth character is the ASCII symbol. This is what you want to write to the standard output.

### Customization

It is possible to change some constants and add/remove colors in the script. The following is a list of what constants are currently configurable in the script.

- ASCII_CHARS: An array of symbols that will be used to generate the bare ASCII art, ordered from most to least dense. You **cannot** add or remove items to this array, only change the items currently in it.
  - Example: `['A', '#', '@', '%', '?', '*', '+', ';', ':', '.', ' ']`
- PIXEL_COLORS: A dictionary of color characters paired with their respective (R, G, B) values. Items can be added and removed to this constant.
  - Example: `{'R': (255, 0, 0), 'G': (0, 255, 0), 'B': (0, 0, 255)}`
- MAX_WIDTH: Sets the maximum width of generated art. Can be changed to any positive, nonzero integer.
  - Example: `32`
- COLOR_INDICATOR: The symbol to flag the beginning of a color code. Can be changed to any character.
  - Example: `+`
- NEWLINE_SYMBOL: The symbol to indicate a new line. This is used purely to preserve consistency between operating systems ([read more](https://en.wikipedia.org/wiki/Newline#Issues_with_different_newline_formats)). Can be changed to any character.
  - Example: `^`

> Please be sure constants do not conflict with each other (e.g. a character used as an ASCII character is also defined as the newline symbol)!

### Example

Source image:

<img src="https://github.com/9730886/color-ascii-art-py/blob/main/example/source.jpg?raw=true" width="300px" height="300px" alt="Example source image">

Generated color ASCII art (resized to 128x128):

<img src="https://github.com/9730886/color-ascii-art-py/blob/main/example/screenshot.png?raw=true" width="300px" height="300px" alt="Example source image">

## Contributing

If you find a bug, always report it [as an issue](https://github.com/9730886/color-ascii-art-py/issues). If an issue for your problem already exists, do not create a duplicate.

If you have a fix, you can open a pull request and reference the issue.

Feature and other additions are always welcome, as long as they fit the project as determined by a maintainer at the time of request.
