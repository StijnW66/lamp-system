from gpiozero import PWMLED
from time import sleep
import sys
import threading

sys.path.append('.')

from pi.led_control.led_control import set_rgb
from database_connection.database_connection import DataBase
from pi.led_control.pattern_control import PatternThread

database = DataBase()
pattern = PatternThread()

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

	update_leds()
	sleep(1)

