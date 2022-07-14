from gpiozero import PWMLED
from time import sleep

# Initialize LED pins from file
f = open("pi/led_control/led_numbers.txt", "r")

red_led = PWMLED(int(f.readline())) #13-S 4-T
green_led = PWMLED(int(f.readline())) #19-S 17-T
blue_led = PWMLED(int(f.readline())) #26-S 27-T

leds = [red_led, green_led, blue_led]

f.close()

def set_value(led, value):
	if(value <= 1):
		led.value = value

def set_rgb(rgb):
	#print(rgb)
	for i in range(3):
		set_value(leds[i], rgb[i]/100)
