import pandas as pd
from decouple import config
from faker import Faker
from snowflake.connector import pandas_tools
from pathlib import Path

from data_generator.SQL_input import get_faker_table_ddl, get_flight_table_ddl
from data_generator.connection import get_connection


def generate_sample_data_with_faker():
    if 'faker_data' not in locals():  # TODO: is data in db not locals
        fake = Faker('en_GB')
        faker_data = [fake.profile() for i in range(100)]
        faker_df = pd.DataFrame(faker_data)
        return faker_df


def flight_data_to_df():
    flight_data_path = Path('airports_extended.txt')
    read_flight_data_in = flight_data_path.read_text()
    flight_df = pd.DataFrame(read_flight_data_in)  # TODO: relative path????
    return flight_df


def faker_data_into_table():
    ctx = get_connection()
    create_faker_table_sql = get_faker_table_ddl()
    faker_df = generate_sample_data_with_faker()
    cs = ctx.cursor()
    cs.execute(create_faker_table_sql)
    pandas_tools.write_pandas(ctx, faker_df, table_name='FAKER_REFERENCE_DATA_GENERATOR', database='SANDBOX',
                              schema=config('SNOWFLAKE_USER'),
                              quote_identifiers=False)


def flight_data_into_table():
    ctx = get_connection()
    create_flight_table_sql = get_flight_table_ddl()
    flight_df = flight_data_to_df()
    cs = ctx.cursor()
    cs.execute(create_flight_table_sql)
    pandas_tools.write_pandas(ctx, flight_df, table_name='FLIGHT_REFERENCE_DATA_GENERATOR', database='SANDBOX',
                              schema=config('SNOWFLAKE_USER'),
                              quote_identifiers=False)
