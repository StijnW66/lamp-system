from gpiozero import PWMLED
from time import sleep

def set_value(led, value):
	led.value = value
