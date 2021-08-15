from gpiozero import PWMLED
from time import sleep
import sys

sys.path.append('.')

from pi.led_control.led_control import set_value
from database_connection.database_connection import DataBase

database = DataBase()

red_led = PWMLED(4)
green_led = PWMLED(17)
blue_led = PWMLED(27)

leds = [red_led, green_led, blue_led]

def update_leds():
	rgb = database.get_rgb_values()
	print(rgb)
	for i in range(3):
		set_value(leds[i], rgb[i]/100)

while True:

	update_leds()
	sleep(1)

