import curses
import time
import random

from function import *
from theme import *

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Don't block waiting for user input
    stdscr.timeout(500) # Refresh every 500 ms
    theme_set_colours()

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        draw_header(stdscr, 1, 1, "ptop - Monitor PRTG from your terminal", w)
        draw_footer(stdscr)
        # Draw standard information
        draw_bars(stdscr, 3, 3, "1", 32, 100, 100)
        draw_bars(stdscr, 4, 3, "Mem", 32, 16000, random.randint(0, 16000))
        draw_bars(stdscr, 5, 3, "Swp", 32, 8000, random.randint(0, 8000))

        draw_sensor(stdscr, 3, 50, "Alerts", "6", 3)
       

        # Draw Process List Header
        draw_processes(stdscr, 7, 1, 30)

        # Handle exit key (q)
        key = stdscr.getch()
        if key == ord('q'):
            break

        stdscr.refresh()
        time.sleep(0.1)

curses.wrapper(main)
