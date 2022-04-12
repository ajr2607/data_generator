from connection import get_connection
from sql_input import get_flight_table_ddl
from utils import flight_data_into_table

if __name__ == '__main__':
    get_connection()

    get_flight_table_ddl()

    flight_data_into_table()
