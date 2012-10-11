from __future__ import print_function
import random
import os


# System color name constants.
(
    BLACK,
    RED,
    GREEN,
    YELLOW,
    BLUE,
    MAGENTA,
    CYAN,
    LIGHT_GRAY,
    DARK_GRAY,
    BRIGHT_RED,
    BRIGHT_GREEN,
    BRIGHT_YELLOW,
    BRIGHT_BLUE,
    BRIGHT_MAGENTA,
    BRIGHT_CYAN,
    WHITE,
) = range(16)

def rgb(red, green, blue):
    """
    Calculate the palette index of a color in the 6x6x6 color cube.

    The red, green and blue arguments may range from 0 to 5.
    """
    return 16 + (red * 36) + (green * 6) + blue

def gray(value):
    """
    Calculate the palette index of a color in the grayscale ramp.

    The value argument may range from 0 to 23.
    """
    return 232 + value

def set_color(fg=None, bg=None):
    """
    Print escape codes to set the terminal color.

    fg and bg are indices into the color palette for the foreground and
    background colors.
    """
    print(_set_color(fg, bg), end='')

def _set_color(fg=None, bg=None):
    result = ''
    if fg:
        result += '\x1b[38;5;%dm' % fg
    if bg:
        result += '\x1b[48;5;%dm' % bg
    return result

def reset_color():
    """
    Reset terminal color to default.
    """
    print(_reset_color(), end='')

def _reset_color():
    return '\x1b[0m'

def print_color(*args, **kwargs):
    """
    Print function, with extra arguments fg and bg to set colors.
    """
    fg = kwargs.pop('fg', None)
    bg = kwargs.pop('bg', None)
    set_color(fg, bg)
    print(*args, **kwargs)
    reset_color()

def format_color(string, fg=None, bg=None):
    return _set_color(fg, bg) + string + _reset_color()

def get_random_color():
    def get_random():
        return random.choice(range(6))
    c1 = rgb(get_random(), get_random(), get_random())
    c2 = random.choice(range(1,15))
    return random.choice([c1,c2])
    
quote_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'quotes.txt')
f = open(quote_file, 'r')
txt = f.read()
lines = txt.split('\n.\n')

print_color(random.choice(lines), fg=get_random_color())
