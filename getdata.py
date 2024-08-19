import curses
import time
import random
import requests
import json
import os

from function import *
from theme import *

settings = read_json("settings.json")

check_filedir(settings['ptop_mode']['file_dir'])

url = settings['server']['prtg_host'] + ":" + settings['server']['prtg_port'] + settings['server']['fetch_url']
url = url.replace("$user", settings['server']['api_user'])
url = url.replace("$pwd", settings['server']['api_password'])

probe_url = settings['server']['prtg_host'] + ":" + settings['server']['prtg_port'] + settings['server']['probe_url']
probe_url = probe_url.replace("$user", settings['server']['api_user'])
probe_url = probe_url.replace("$pwd", settings['server']['api_password'])
probe_url = probe_url.replace("$probe_id", settings['server']['probe_id'])

alert_url = url.replace("$status_code", settings['prtg_status']['alert'])
warning_url = url.replace("$status_code", settings['prtg_status']['warning'])
ack_url = url.replace("$status_code", settings['prtg_status']['ack'])

fetch_json(alert_url, settings['ptop_mode']['file_dir'] + settings['ptop_mode']['alert_file'])
fetch_json(warning_url, settings['ptop_mode']['file_dir'] + settings['ptop_mode']['warnings_file'])
fetch_json(ack_url, settings['ptop_mode']['file_dir'] + settings['ptop_mode']['ack_file'])
fetch_json(probe_url, settings['ptop_mode']['file_dir'] + settings['ptop_mode']['probe_file'])

# End of script
