import psycopg2
from configparser import ConfigParser

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

def connect(query='SELECT * FROM rgb_values'):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

	    # execute a statement
        cur.execute(query)
        output = cur.fetchall()

	    # close the communication with the PostgreSQL
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return output

def convert_to_rgb(output):
    rgb = []
    rgb.append(output[0][1])
    rgb.append(output[0][2])
    rgb.append(output[0][3])

    return rgb


def get_rgb_values(rgb_id=1):
    query = 'SELECT * FROM rgb_values WHERE rgb_id = {}'.format(rgb_id)
    output = connect(query)

    return convert_to_rgb(output)

def update_rgb_values(red=0, green=0, blue=0, rgb_id=1):
    query = 'UPDATE rgb_values SET red = {}, green = {}, blue = {} WHERE rgb_id = {} RETURNING *'.format(red, green, blue, rgb_id)
    output = connect(query)

    return convert_to_rgb(output)
