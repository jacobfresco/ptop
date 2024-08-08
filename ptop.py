import curses
import time
import random

# Constants to define the placeholder values
CPU_BARS = 10
MEM_BARS = 15
SWAP_BARS = 10
NUM_PROCESSES = 10

def draw_bars(stdscr, y, x, label, width, max_value, current_value):
    bar_length = int((current_value / max_value) * width)
    stdscr.addstr(y, x, f"{label}: |" + "#" * bar_length + "-" * (width - bar_length) + "|")

def draw_processes(stdscr, y, x, num_processes):
    stdscr.addstr(y, x, "PID   USER     PRI  NI  VIRT   RES   SHR S %CPU %MEM   TIME+  COMMAND")
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

        stdscr.addstr(y + i + 1, x, f"{pid:<6}{user:<9}{priority:<4}{nice:<4}{virt:<7}{res:<6}{shr:<5}S {cpu:<5}{mem:<5}{time_plus:<8}{command:<10}")

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
