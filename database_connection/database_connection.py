import psycopg2
from configparser import ConfigParser
import time

def config(filename='database_connection/database.ini', section='postgresql'):
    # create a parser
	parser = ConfigParser()
    # read config file
	parser.read(filename)

    # get section, default to postgresql
	db = {}
	if parser.has_section(section):
		params = parser.items(section)
		for param in params:
			db[param[0]] = param[1]
	else:
		raise Exception('Section {0} not found in the {1} file'.format(section, filename))

	return db

def setup_connection():
    # read connection parameters
	params = config()

    # connect to the PostgreSQL server
	connection = psycopg2.connect(**params)
	return connection

class DataBase():

	def __init__(self):
		self.connection = setup_connection()


	def execute_query(self, query):
		cur = self.connection.cursor()

		cur.execute(query)
		output = cur.fetchall()

		self.connection.commit()
		cur.close()

		return output

	def get_rgb_values(self, rgb_id=1):
		query = 'SELECT * FROM rgb_values_pattern WHERE rgb_id = {}'.format(rgb_id)
		output = self.execute_query(query)

		print([output[0][1], output[0][2]])
		return [output[0][1], output[0][2]]

	def update_rgb_values(self, red=0, green=0, blue=0, pattern = 1, rgb_id=1):
		query = 'UPDATE rgb_values_pattern SET rgb = \'{{{}, {} ,{}}}\', pattern_id = {} WHERE rgb_id = {} RETURNING *'.format(red, green, blue, pattern, rgb_id)
		output = self.execute_query(query)

		print([output[0][1], output[0][2]])
		return [output[0][1], output[0][2]]

	def get_pattern(self, pattern_id=1):
		query = 'SELECT * FROM pattern Where pattern_id = {}'.format(pattern_id)
		output = self.execute_query(query)
		pattern = output[0][1]

		return convert_pattern(pattern)

def convert_pattern(pattern):
	conv_pattern = []

	for color in pattern:
		conv_pattern.append([[color[0], color[1], color[2]], color[3]])
	print(conv_pattern)
	return conv_pattern
