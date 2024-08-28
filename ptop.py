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

if settings['ptop_mode']['debug'] == "true":
    import logging
    logging.basicConfig(
        level=logging.ERROR,
        filename="ptop_debug.log",
        encoding="utf-8",
        filemode="a",
        format="{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M",
    )
    
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

        
        try:
            uptime = probe['sensordata']['uptime'][:-1].split(',')
            downtime = probe['sensordata']['downtime'][:-1].split(',')

            draw_bars(stdscr, 3, 3, "Up", 32, 100, int(uptime[0]))
            draw_value(stdscr, 3, 41, uptime[0] + "%", 3)
            draw_bars(stdscr, 4, 3, "Int", 32, 100, int(probe['sensordata']['interval']))
            draw_value(stdscr, 4, 41, probe['sensordata']['interval'] + "s", 3)
            draw_bars(stdscr, 5, 3, "Dwn", 32, 100, int(downtime[0]))
            draw_value(stdscr, 5, 41, downtime[0] + "%", 3)
            
            draw_sensor(stdscr, 3, 50, "Name", probe['sensordata']['parentdevicename'] , 3)
            draw_sensor(stdscr, 4, 50, "PRTG Version", alerts['prtg-version'], 3)
            draw_sensor(stdscr, 5, 50, "Uptime", probe['sensordata']['uptimetime'], 3)

            draw_line(stdscr, 7, 1, f"* ID    DEVICE                MESSAGE ", w, 9)
        except Exception as e:
            logging.error("Error printing probe information: " + str(e))                
            pass

        l = 8
        
        try:
            for i in range(int(alerts['treesize'])):
                try:
                    draw_line(stdscr, l, 1, "", w, 12)
                    draw_value(stdscr, l, 1, "A", 12)
                    draw_value(stdscr, l, 3, alerts['sensors'][i]['objid'], 12)
                    draw_value(stdscr, l, 9, alerts['sensors'][i]['device_raw'][:21], 12)
                    draw_value(stdscr, l, 31, alerts['sensors'][i]['message_raw'][:(w-31)], 12)
                    l += 1
                except curses.error as e:
                    logging.debug("Error printing alerts: " + str(e))
                    pass
                    
        except AttributeError as e:
            logging.error("Empty JSON: " + str(e))
            pass

        
        try:    
            if settings['ptop_mode']['show_warnings'] == "true":
                try:
                    for i in range(int(warnings['treesize'])):
                        try:
                            draw_line(stdscr, l, 1, "", w, 4)
                            draw_value_nb(stdscr, l, 1, "W", 4)
                            draw_value_nb(stdscr, l, 3, warnings['sensors'][i]['objid'], 4)
                            draw_value_nb(stdscr, l, 9, warnings['sensors'][i]['device_raw'][:21], 4)
                            draw_value_nb(stdscr, l, 31, warnings['sensors'][i]['message_raw'][:(w-31)], 4)
                            l += 1
                        except curses.error as e:
                            logging.debug("Error printing warnings: " + str(e))
                            pass

                except AttributeError as e:
                    logging.error("Empty JSON: " + str(e))        
        except Exception as e:
            logging.error("Error: " + str(e))
            pass


        try:
            if settings['ptop_mode']['show_acks'] == "true":
                try:
                    for i in range(int(acks['treesize'])):
                        try:
                            draw_line(stdscr, l, 1, "", w, 7)
                            draw_value_nb(stdscr, l, 1, "a", 7)
                            draw_value_nb(stdscr, l, 3, acks['sensors'][i]['objid'], 7)
                            draw_value_nb(stdscr, l, 9, acks['sensors'][i]['device_raw'][:21], 7)
                            draw_value_nb(stdscr, l, 31, acks['sensors'][i]['message_raw'][:(w-31)], 7)
                            l += 1
                        except curses.error as e:
                            logging.debug("Error printing acks: " + str(e))
                            pass

                except AttributeError as e:
                    logging.error("Empty JSON: " + str(e)) 
        except Exception as e:
            logging.error("Error: " + str(e))
            pass

        try:
            draw_footer(stdscr, f"[Alerts " + str(alerts['treesize']) + "] [Warnings " + str(warnings['treesize']) +"] [Ackknowleded " + str(acks['treesize']) + "] [Q - Quit]")
        except Exception as e:
            logging.error("Error printing footer: " + str(e))
            pass

        key = stdscr.getch()
        if key == ord('q'):
            stdscr.clear()
            break

        stdscr.refresh()
        time.sleep(1)

curses.wrapper(main)
