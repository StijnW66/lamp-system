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
        query = 'SELECT * FROM rgb_values WHERE rgb_id = {}'.format(rgb_id)
        output = self.execute_query(query)

        return convert_to_rgb(output)

    def update_rgb_values(self, red=0, green=0, blue=0, rgb_id=1):
        query = 'UPDATE rgb_values SET red = {}, green = {}, blue = {} WHERE rgb_id = {} RETURNING *'.format(red, green, blue, rgb_id)
        output = self.execute_query(query)

        return convert_to_rgb(output)

def convert_to_rgb(output):
    rgb = []
    rgb.append(output[0][1])
    rgb.append(output[0][2])
    rgb.append(output[0][3])

    return rgb
