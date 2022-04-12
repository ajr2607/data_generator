from connection import get_connection
from SQL_input import create_flight_table
from utils import flight_data_into_table

if __name__ == '__main__':
    get_connection()

    create_flight_table()

    flight_data_into_table()
