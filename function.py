import curses
import time
import random
import requests

from theme import *

def read_settings(settings_file):
    try:
        # Open and read the settings file
        with open(settings_file, 'r') as file:
            settings = json.load(file)
            return settings

    except FileNotFoundError:
        print(f"Error: The file {settings_file} was not found.")
        return None

    except json.JSONDecodeError:
        print(f"Error: The file {settings_file} contains invalid JSON.")
        return None

# Load settings
settings = load_settings(settings_file)

if settings:
    # Accessing individual settings
    server = settings.get("server", {})
    status = settings.get("status", {})
    ptop_mode = settings.get("ptop_mode", {})
    
    # Use the settings in your application
    if debug_mode:
        print("Debug mode is enabled.")
    else:
        print("Debug mode is disabled.")

else:
    print("Failed to load settings.")

def fetch_json(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the JSON content
        data = response.json()

        # Save the JSON data to a file
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)

        #print(f"JSON data has been saved to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

    except json.JSONDecodeError:
        print("Error decoding JSON response")


def check_filedir(dir):
    # Check if the configured directory for the cached files exists. 
    h, w = stdscr.getmaxyx()

def draw_header(stdscr, y, x, label, width):
    stdscr.addstr(y, x, " " + f"{label}" + " " * ((width - len(label))-2), curses.color_pair(11))

def draw_footer(stdscr):
    h, w = stdscr.getmaxyx()
   
    stdscr.addstr(h-1, 1, f"F1", curses.color_pair(8))
    stdscr.addstr(h-1, 3, f"Alerts ", curses.color_pair(12))
    stdscr.addstr(h-1, (len("F1Alerts ")+1), f"F2", curses.color_pair(8))
    stdscr.addstr(h-1, (len("F1Alerts F2")+1), f"Warnings ", curses.color_pair(13))
    stdscr.addstr(h-1, (len("F1Alerts F2 Warings ")+1), f"F3", curses.color_pair(8))
    stdscr.addstr(h-1, (len("F1Alerts F2 Warings F3")+1), f"Ack ", curses.color_pair(10))
    stdscr.addstr(h-1, (len("F1Alerts F2 Warings F3Ack ")+1), f"F10", curses.color_pair(8))
    stdscr.addstr(h-1, (len("F1Alerts F2 Warings F3Ack F10")+1), f"Quit ", curses.color_pair(9))
    

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
