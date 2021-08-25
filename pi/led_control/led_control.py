from gpiozero import PWMLED
from time import sleep

red_led = PWMLED(4) #13
green_led = PWMLED(17) #19
blue_led = PWMLED(27) #26

leds = [red_led, green_led, blue_led]

def set_value(led, value):
	if(value <= 1):
		led.value = value

def set_rgb(rgb):
	#print(rgb)
	for i in range(3):
		set_value(leds[i], rgb[i]/100)
