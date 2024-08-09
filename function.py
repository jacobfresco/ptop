import curses
import time
import random

from theme import *
def draw_header(stdscr, y, x, label, width):
    stdscr.addstr(y, x, " " + f"{label}" + " " * ((width - len(label))-2), curses.color_pair(11))

def draw_bars(stdscr, y, x, label, width, max_value, current_value):
    bar_length = int((current_value / max_value) * width)
    stdscr.addstr(y, x, f"{label}", curses.color_pair(7))
    stdscr.addstr(y, x+3, f"[", curses.color_pair(8))
    stdscr.addstr(y, x+4, "|" * bar_length + "-" * (width - bar_length),curses.color_pair(3))
    stdscr.addstr(y, x+4+width, f"]", curses.color_pair(8))

def draw_sensor(stdscr, y, x, label, value, vcolorpair):
    stdscr.addstr(y, x, f"{label}" + ": ", curses.color_pair(7))
    stdscr.addstr(y, x + (len(label)+2), f"{value}", curses.color_pair(int(vcolorpair)) | curses.A_BOLD)

def draw_processes(stdscr, y, x, num_processes):
    stdscr.addstr(y, x, "PID   USER     PRI  NI  VIRT   RES   SHR S %CPU %MEM   TIME+  COMMAND", curses.color_pair(9))
    for i in range(num_processes):
        pid = random.randint(1000, 9999)
        user = "user" + str(random.randint(1, 5))
        priority = random.randint(20, 40)
        nice = random.randint(-20, 19)
        virt = random.randint(100000, 500000)
        res = random.randint(10000, 30000)
        shr = random.randint(1000, 5000)
        cpu = round(random.uniform(0, 100), 1)
        mem = round(random.uniform(0, 10), 1)
        time_plus = f"{random.randint(0, 99)}:{random.randint(0, 59):02d}.{random.randint(0, 99):02d}"
        command = f"command_{i+1}"
        #stdscr.addstr(y + i + 1, x, f"{pid:<6}{user:<9}{priority:<4}{nice:<4}{virt:<7}{res:<6}{shr:<5}S {cpu:<5}{mem:<5}{time_plus:<8}{command:<10}")