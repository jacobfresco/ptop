import curses
import time
import random

def theme_set_colours():
    curses.start_color() # Use colours
    curses.use_default_colors() # Use default terminal colors

    # Black backgrounds
    curses.init_pair(1, COLOR_RED, COLOR_BLACK);
    curses.init_pair(2, COLOR_RED, COLOR_BLACK);
    curses.init_pair(3, COLOR_GREEN, COLOR_BLACK);
    curses.init_pair(4, COLOR_YELLOW, COLOR_BLACK);
    curses.init_pair(5, COLOR_BLUE, COLOR_BLACK);
    curses.init_pair(6, COLOR_MAGENTA, COLOR_BLACK);
    curses.init_pair(7, COLOR_CYAN, COLOR_BLACK);
    curses.init_pair(8, COLOR_WHITE, COLOR_BLACK);

    curses.init_pair(9, COLOR_BLACK, COLOR_GREEN);
    curses.init_pair(10, COLOR_BLACK, COLOR_BLUE);

