import threading
import sys
from time import sleep
import math
from operator import add

sys.path.append('.')

from pi.led_control.led_control import set_rgb

#rainbow = [[100, 0, 0], [100, 100, 0], [0, 100, 0], [0, 100, 100], [0, 0, 100], [100, 0, 100]]
rainbow = [[[100, 0, 0], 50], [[100, 100, 0], 50], [[0, 100, 0], 50], [[0, 100, 100], 50], [[0, 0, 100], 50], [[100, 0, 100], 50]]
fast_rainbow = [[[100, 0, 0], 10], [[100, 100, 0], 10], [[0, 100, 0], 10], [[0, 100, 100], 10], [[0, 0, 100], 10], [[100, 0, 100], 10]]
rgb_flash = [[[100, 0, 0], 10], [[100, 0, 0], 1], [[0, 100, 0], 10], [[0, 100, 0], 1], [[0, 0, 100], 10], [[0, 0, 100], 1]]
rgb_quick_flash = [[[100, 0, 0], 5], [[100, 0, 0], 1], [[0, 100, 0], 5], [[0, 100, 0], 1], [[0, 0, 100], 5], [[0, 0, 100], 1]]
rgb_super_quick_flash = [[[100, 0, 0], 2], [[100, 0, 0], 1], [[0, 100, 0], 2], [[0, 100, 0], 1], [[0, 0, 100], 2], [[0, 0, 100], 1]]


pattern = rainbow + fast_rainbow + rgb_flash + rgb_quick_flash * 2 + rgb_super_quick_flash * 3

class PatternThread:

	def __init__(self):
		self.thread = None
		self.stop_flag = False

	def start_pattern(self, pattern_num=0):
		self.stop_flag = False

		self.thread = threading.Thread(target=lambda: self.advance_pattern(pattern_num), daemon=True)
		self.thread.start()
		print("new thread started")

	def stop_pattern(self):
		if self.thread is not None:
			self.stop_flag = True
			self.thread.join()
			self.thread = None
			print("new thread stopped")

	def advance_pattern(self, pattern_num=0):
		pattern_counter = 0
		interpolation_counter = 0
		interpolate_duration = rainbow[pattern_counter][1]

		while not self.stop_flag:
			progress = interpolation_counter * (100/interpolate_duration)

			rgb = interpolate_color(pattern[pattern_counter][0], pattern[(pattern_counter + 1) % len(pattern)][0], progress)
			print(rgb)
			set_rgb(rgb)


			interpolation_counter = (interpolation_counter + 1) % interpolate_duration
			if interpolation_counter == 0:
				pattern_counter = (pattern_counter + 1) % len(pattern)
				interpolate_duration = pattern[pattern_counter][1]
			sleep(0.1)


def interpolate_color(rgb_start, rgb_target, progress):
	rgb_start = [x * ((100 - progress)/100) for x in rgb_start]
	rgb_target = [x * (progress/100) for x in rgb_target]
	rgb = list( map(add, rgb_start, rgb_target))
	rgb = [int(x) for x in rgb]
	return rgb
