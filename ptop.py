import curses
import time
import random
import requests
import json
import os

from function import *
from theme import *

global prtg_url 
global prtg_url 
global prtg_url 

global file_dir 
global alert_file 
global warning_file
global ack_file

settings = read_settings("settings.json")
check_filedir(settings['ptop_mode']['file_dir'])

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
        draw_processes(stdscr, 7, 1, 10)

        # Handle exit key (q)
        key = stdscr.getch()
        if key == ord('^[[21~'):
            break

        stdscr.refresh()
        time.sleep(0.1)

curses.wrapper(main)
