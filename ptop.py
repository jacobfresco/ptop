import curses
import time
import random

from function import *

# Constants to define the placeholder values
CPU_BARS = 10
MEM_BARS = 15
SWAP_BARS = 10
NUM_PROCESSES = 10

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Don't block waiting for user input
    stdscr.timeout(500) # Refresh every 500 ms

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        # Draw CPU, Memory, and Swap Usage
        draw_bars(stdscr, 1, 1, "CPU", CPU_BARS, 100, random.randint(0, 100))
        draw_bars(stdscr, 2, 1, "Mem", MEM_BARS, 16000, random.randint(0, 16000))
        draw_bars(stdscr, 3, 1, "Swp", SWAP_BARS, 8000, random.randint(0, 8000))

        # Draw Process List Header
        draw_processes(stdscr, 5, 1, NUM_PROCESSES)

        # Handle exit key (q)
        key = stdscr.getch()
        if key == ord('q'):
            break

        stdscr.refresh()
        time.sleep(0.1)

curses.wrapper(main)
