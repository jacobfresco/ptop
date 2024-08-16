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

settings = read_json("settings.json")
check_filedir(settings['ptop_mode']['file_dir'])

def main(stdscr):
    curses.curs_set(0)  
    stdscr.nodelay(1)   
    stdscr.timeout(500) 
    theme_set_colours()

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        draw_header(stdscr, 1, 1, "ptop - Monitor PRTG from your terminal", w)
        draw_footer(stdscr)

        alerts = read_json(settings['ptop_mode']['file_dir'] + settings['ptop_mode']['alert_file'])
        warnings = read_json(settings['ptop_mode']['file_dir'] + settings['ptop_mode']['warnings_file'])
        probe = read_json(settings['ptop_mode']['file_dir'] + settings['ptop_mode']['probe_file'])
        
        uptime = probe['sensordata']['uptime'][:-1].split(',')
        draw_bars(stdscr, 3, 3, "Up", 32, 100, int(uptime[0]))
        draw_value(stdscr, 3, 41, uptime[0] + "%", 3)
        draw_bars(stdscr, 4, 3, "Mem", 32, 16000, random.randint(0, 16000))
        draw_bars(stdscr, 5, 3, "Swp", 32, 8000, random.randint(0, 8000))
        
        draw_sensor(stdscr, 3, 50, "Name", probe['sensordata']['parentdevicename'], 3)
        draw_sensor(stdscr, 4, 50, "PRTG Version", alerts['prtg-version'], 3)
        draw_sensor(stdscr, 5, 50, "Alerts", alerts['treesize'], 3)

        for i in alerts['sensors']:
            
            draw_processes(stdscr, 7, 1, 10)

        key = stdscr.getch()
        if key == ord('q'):
            stdscr.clear()
            break

        stdscr.refresh()
        time.sleep(0.1)

curses.wrapper(main)
