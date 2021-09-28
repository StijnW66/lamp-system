import http.client
import json

HOST = 'cryptic-earth-79580.herokuapp.com'

class ServerConnection():

	def __init__(self):

		self.connection = http.client.HTTPSConnection(HOST)


	def get_rgb_values_http(self, rgb_id = 1):
		path = '/rgb_values/' + str(rgb_id)

		dict = self.execute_http_request("GET", path)

		return [dict['rgb'], dict['patternId']]

	def update_rgb_values_http(self, red=0, green=0, blue=0, pattern=0, rgb_id=1):
		path = '/rgb_values/' + str(rgb_id)
		headers = {'Content-type': 'application/json'}

		content = {'rgb' : [red, green, blue], 'patternId': pattern}
		json_data = json.dumps(content)

		dict = self.execute_http_request("PATCH", path, json_data, headers)
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
		print('executing: ' + method + " " + path)

		if json_data is None:
			self.connection.request(method, path)
		else:
			self.connection.request(method, path, json_data, headers)

		response = self.connection.getresponse()

		return json.loads(response.read())

def convert_pattern(pattern):
	conv_pattern = []

	for color in pattern:
		conv_pattern.append([[color[0], color[1], color[2]], color[3]])
	print(conv_pattern)
	return conv_pattern
