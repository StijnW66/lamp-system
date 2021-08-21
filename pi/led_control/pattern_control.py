import threading
import sys
from time import sleep
import math
from operator import add

sys.path.append('.')

from pi.led_control.led_control import set_rgb

rainbow = [[100, 0, 0], [100, 100, 0], [0, 100, 0], [0, 100, 100], [0, 0, 100], [100, 0, 100]]

class PatternThread:

	def __init__(self):
		self.thread = None
		self.stop_flag = False

	def start_pattern(self, pattern=0):
		self.stop_flag = False

		self.thread = threading.Thread(target=lambda: self.advance_pattern(pattern), daemon=True)
		self.thread.start()
		print("new thread started")

	def stop_pattern(self):
		if self.thread is not None:
			self.stop_flag = True
			self.thread.join()
			print("new thread stopped")

	def advance_pattern(self, pattern=0, interpolate_duration=10):
		counter = 0
		while not self.stop_flag:
			index = math.floor(counter / interpolate_duration)
			next_index = (index + 1) % len(rainbow)
			progress = (counter % interpolate_duration) * interpolate_duration

			rgb = interpolate_color(rainbow[index], rainbow[next_index], progress)
			set_rgb(rgb)

			counter = (counter + 1) % (interpolate_duration *len(rainbow))
			sleep(0.1)


def interpolate_color(rgb_start, rgb_target, progress):
	rgb_start = [x * ((100 - progress)/100) for x in rgb_start]
	rgb_target = [x * (progress/100) for x in rgb_target]
	rgb = list( map(add, rgb_start, rgb_target))
	return rgb
