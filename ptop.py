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
       

        alerts = read_json(settings['ptop_mode']['file_dir'] + settings['ptop_mode']['alert_file'])
        warnings = read_json(settings['ptop_mode']['file_dir'] + settings['ptop_mode']['warnings_file'])
        acks = read_json(settings['ptop_mode']['file_dir'] + settings['ptop_mode']['ack_file'])
        probe = read_json(settings['ptop_mode']['file_dir'] + settings['ptop_mode']['probe_file'])
        
        uptime = probe['sensordata']['uptime'][:-1].split(',')
        draw_bars(stdscr, 3, 3, "Up", 32, 100, int(uptime[0]))
        draw_value(stdscr, 3, 41, uptime[0] + "%", 3)
        draw_bars(stdscr, 4, 3, "Int", 32, 100, int(probe['sensordata']['interval']))
        draw_bars(stdscr, 5, 3, "Swp", 32, 8000, random.randint(0, 8000))
        
        draw_sensor(stdscr, 3, 50, "Name", probe['sensordata']['parentdevicename'], 3)
        draw_sensor(stdscr, 4, 50, "PRTG Version", alerts['prtg-version'], 3)
        draw_sensor(stdscr, 5, 50, "Uptime", probe['sensordata']['uptimetime'], 3)

        draw_line(stdscr, 7, 1, f"ID    DEVICE                MESSAGE ", w, 11)
        
        l = 8
        
        for i in range(int(alerts['treesize'])):
            try:
                draw_line(stdscr, l, 1, "", w, 12)
                draw_value(stdscr, l, 1, alerts['sensors'][i]['objid'], 12)
                draw_value(stdscr, l, 7, alerts['sensors'][i]['device_raw'][:21], 12)
                draw_value(stdscr, l, 29, alerts['sensors'][i]['message_raw'][:(w-29)], 12)
                l += 1
            except curses.error:
                pass

        for i in range(int(warnings['treesize'])):
            try:
                draw_line(stdscr, l, 1, "", w, 8)
                draw_value_nb(stdscr, l, 1, warnings['sensors'][i]['objid'], 8)
                draw_value_nb(stdscr, l, 7, warnings['sensors'][i]['device_raw'][:21], 8)
                draw_value_nb(stdscr, l, 29, warnings['sensors'][i]['message_raw'][:(w-29)], 8)
                l += 1
            except curses.error:
                pass
        
        # draw_footer(stdscr)
        draw_footer2(stdscr, f"[Alerts " + str(alerts['treesize']) + "] [Warnings " + str(warnings['treesize']) +"] [Ackknowleded " + str(acks['treesize']) + "] [Q - Quit]")

        key = stdscr.getch()
        if key == ord('q'):
            stdscr.clear()
            break

        stdscr.refresh()
        time.sleep(1)

curses.wrapper(main)
