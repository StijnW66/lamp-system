from gpiozero import PWMLED
from time import sleep
import sys

sys.path.append('.')

from pi.led_control.led_control import set_value
from database_connection.database_connection import get_rgb_values

red_led = PWMLED(4)
green_led = PWMLED(17)
#blue_led =

leds = [red_led, green_led]

def update_leds():
	rgb = get_rgb_values()
	print(rgb)
	for i in range(2):
		set_value(leds[i], rgb[i]/100)

while True:

	update_leds()
	sleep(1)

