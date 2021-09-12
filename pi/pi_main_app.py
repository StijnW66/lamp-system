from gpiozero import PWMLED
from time import sleep
import sys
import threading
from datetime import datetime

sys.path.append('.')

now = datetime.now()

print("time =", now.strftime("%d/%m/%Y %H:%M:%S"))
print("running")

from pi.led_control.led_control import set_rgb
from database_connection.database_connection import DataBase
from pi.led_control.pattern_control import PatternThread

# Start a pattern while not connected to the database.
rainbow = [[[100, 0, 0], 50], [[100, 100, 0], 50], [[0, 100, 0], 50], [[0, 100, 100], 50], [[0, 0, 100], 50], [[100, 0, 100], 50]]
fast_rainbow = [[[100, 0, 0], 10], [[100, 100, 0], 10], [[0, 100, 0], 10], [[0, 100, 100], 10], [[0, 0, 100], 10], [[100, 0, 100], 10]]
rgb_flash = [[[100, 0, 0], 10], [[100, 0, 0], 1], [[0, 100, 0], 10], [[0, 100, 0], 1], [[0, 0, 100], 10], [[0, 0, 100], 1]]
rgb_quick_flash = [[[100, 0, 0], 5], [[100, 0, 0], 1], [[0, 100, 0], 5], [[0, 100, 0], 1], [[0, 0, 100], 5], [[0, 0, 100], 1]]
rgb_super_quick_flash = [[[100, 0, 0], 2], [[100, 0, 0], 1], [[0, 100, 0], 2], [[0, 100, 0], 1], [[0, 0, 100], 2], [[0, 0, 100], 1]]


pat = rainbow + fast_rainbow + rgb_flash + rgb_quick_flash * 2 + rgb_super_quick_flash * 3

pattern = PatternThread()
pattern.start_pattern(pat)

# Try to connect to database. Timeout after 200 attempts.
database = None
attempt_counter = 0

while database is None:
	try:
		database = DataBase()
	except:
		if attempt_counter == 200:
			exit()
		database = None
		sleep(1)
		attempt_counter += 1

print("connected", attempt_counter)
sys.stdout.flush()


current_pattern = 0

def update_leds():
	global current_pattern
	rgb_info = database.get_rgb_values()
	rgb = rgb_info[0]
	pat = rgb_info[1]
	if not (pat == 0):
		if not (pat == current_pattern):
			pattern.stop_pattern()
			pattern.start_pattern(database.get_pattern(pat))
			current_pattern = pat
	else:
		pattern.stop_pattern()
		current_pattern = 0
		set_rgb(rgb)

while True:
# Continuously poll database state to update the LEDs
	update_leds()
	sleep(1)

