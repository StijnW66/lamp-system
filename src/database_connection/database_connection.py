import http.client
import json
import threading

HOST = 'cryptic-earth-79580.herokuapp.com'

class ServerConnection():

	def __init__(self):
		self.lock = threading.Lock()
		self.connection = http.client.HTTPSConnection(HOST)
		self.last_updated = None

	def get_rgb_values_http(self, rgb_id = 1):
		path = '/rgb_values/' + str(rgb_id)

		dict = self.execute_http_request("GET", path)

		self.last_updated = dict['lastUpdated']
		return [dict['rgb'], dict['patternId']]

	def get_rgb_values_update_http(self, rgb_id = 1):
		path = '/rgb_values/update/' + str(rgb_id)
		headers = {'Date': self.last_updated}
		dict = self.execute_http_request("GET", path, headers=headers)

		if dict is None:
			return None
		else:
			self.last_updated = dict['lastUpdated']
			return [dict['rgb'], dict['patternId']]

	def update_rgb_values_http(self, red=0, green=0, blue=0, pattern=0, rgb_id=1):
		path = '/rgb_values/' + str(rgb_id)
		headers = {'Content-type': 'application/json'}

		content = {'rgb' : [red, green, blue], 'patternId': pattern}
		json_data = json.dumps(content)

		dict = self.execute_http_request("PATCH", path, json_data, headers)

		self.last_updated = dict['lastUpdated']
		return [dict['rgb'], dict['patternId']]


	def get_pattern_http(self, pattern_id = 1):
		path = '/pattern/' + str(pattern_id)

		dict = self.execute_http_request("GET", path)

		return convert_pattern(dict['patternContents'])

	def get_total_patterns_http(self):
		path = '/pattern/count'
		dict = self.execute_http_request("GET",path)
		return dict # This is just a number


	def execute_http_request(self, method="GET", path="", json_data=None, headers=None):
		self.lock.acquire()
		print('executing: ' + method + " " + path)

		if headers is None:
			self.connection.request(method, path)
		elif json_data is None:
			self.connection.request(method, path, headers=headers)
		else:
			self.connection.request(method, path, json_data, headers)

		response = self.connection.getresponse()

		response = response.read()

		if len(response) == 0:
			self.lock.release()
			return None

		dict = json.loads(response)
		self.lock.release()
		print(dict)
		return dict

def convert_pattern(pattern):
	conv_pattern = []

	for color in pattern:
		conv_pattern.append([[color[0], color[1], color[2]], color[3]])
	print(conv_pattern)
	return conv_pattern
