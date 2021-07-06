from gpiozero import PWMLED
from time import sleep

def set_value(led, value):
	if(value <= 1):
		led.value = value
