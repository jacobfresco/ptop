import curses
import random

def draw_borders(win):
    win.border(0)
    height, width = win.getmaxyx()
    win.hline(1, 1, curses.ACS_HLINE, width-2)
    win.vline(2, width//2, curses.ACS_VLINE, height-3)
    win.addch(1, width//2, curses.ACS_TTEE)
    win.addch(height-1, width//2, curses.ACS_BTEE)

def display_header(win, width):
    win.addstr(0, 1, "htop-like Placebo Script", curses.color_pair(1))
    win.addstr(0, width-25, "Load average: 0.00 0.00 0.00", curses.color_pair(1))

def display_left_panel(win):
    win.addstr(2, 2, "Tasks: 0 total, 0 running, 0 sleeping, 0 stopped, 0 zombie", curses.color_pair(2))
    win.addstr(3, 2, "CPU: 0.0%us, 0.0%sy, 0.0%ni, 100.0%id, 0.0%wa, 0.0%hi, 0.0%si, 0.0%st", curses.color_pair(2))
    win.addstr(4, 2, "Mem: 0K total, 0K used, 0K free, 0K buffers", curses.color_pair(2))
    win.addstr(5, 2, "Swap: 0K total, 0K used, 0K free, 0K cached", curses.color_pair(2))

def display_right_panel(win):
    height, width = win.getmaxyx()
    for i in range(2, height-1):
        win.addstr(i, width//2 + 1, f"{random.randint(1, 100)}%", curses.color_pair(random.randint(3, 7)))

def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    
    # Define color pairs
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    # Get terminal dimensions
    height, width = stdscr.getmaxyx()

    # Draw the borders and static components
    draw_borders(stdscr)
    display_header(stdscr, width)
    display_left_panel(stdscr)
    display_right_panel(stdscr)

    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
