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
pattern = PatternThread()
pattern.start_pattern()

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
		attempt_counter += 1

print("connected", attempt_counter)
sys.stdout.flush()


def update_leds():
	rgb = database.get_rgb_values()
	#print("values from database:", rgb)
	if (rgb == [0, 0, 0]):
		if threading.active_count() < 2:
			pattern.start_pattern()
	else:
		pattern.stop_pattern()
		set_rgb(rgb)

while True:
# Continuously poll database state to update the LEDs
	update_leds()
	sleep(1)

