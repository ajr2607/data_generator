from pathlib import Path

import pandas as pd
from faker import Faker


def generate_sample_data_with_faker():
    if 'faker_data' not in locals():  # TODO: is data in db not locals
        fake = Faker('en_GB')
        faker_data = [fake.profile() for i in range(100)]
        faker_df = pd.DataFrame(faker_data)
        return faker_df


def flight_data_to_df():
    flight_file = Path('airports_extended.txt')  # TODO relative path with data file in sample folder.
    flight_data = pd.read_csv(flight_file, sep=",", header=None)
    flight_data.drop(flight_data.columns[0], axis=1, inplace=True)
    return flight_data


def clean_flight_data():
    flight_data = flight_data_to_df()
    flight_data = flight_data.drop(flight_data.columns[[3, 4, 5, 6, 7, 9, 10, 12]], axis=1)
    flight_data.columns = range(flight_data.columns.size)
    unwanted_list_airport_names = ['All Airports', 'Railway Station', 'Train Station']
    flight_data = flight_data[-flight_data.iloc[:, 0].isin(unwanted_list_airport_names)]
    wanted_list_type_of_port = ['airport', 'station', 'port']
    flight_data = flight_data[flight_data.iloc[:, 4].isin(wanted_list_type_of_port)]
    flight_data = flight_data[-flight_data.iloc[:, :].isin(['\\N'])]
    flight_data = flight_data.dropna()
    flight_data.columns = ['airport_name', 'city_name', 'country_name', 'timezone', 'type_of_port']
    return flight_data

# def faker_data_into_table():
#     ctx = get_connection()
#     create_faker_table_sql = get_faker_table_ddl()
#     faker_df = generate_sample_data_with_faker()
#     cs = ctx.cursor()
#     cs.execute(create_faker_table_sql)
#     pandas_tools.write_pandas(ctx, faker_df, table_name='FAKER_REFERENCE_DATA_GENERATOR',
#                               database='SANDBOX',
#                               schema=decouple.config('SNOWFLAKE_USER'),
#                               quote_identifiers=False)


# def flight_data_into_table():
#     ctx = get_connection()
#     create_flight_table_sql = get_flight_table_ddl()
#     flight_df = flight_data_to_df()
#     cs = ctx.cursor()
#     cs.execute(create_flight_table_sql)
#     pandas_tools.write_pandas(ctx, flight_df, table_name='FLIGHT_REFERENCE_DATA_GENERATOR', database='SANDBOX',
#                               schema=decouple.config('SNOWFLAKE_USER'),
#                               quote_identifiers=False)
#     return flight_table


# def data_into_table(ddl_name, df, sql_table_name):  # TODO general function - in progress
#     ctx = get_connection()
#     cs = ctx.cursor()
#     cs.execute(ddl_name)
#     pandas_tools.write_pandas(ctx, df, table_name=sql_table_name,
#                               database='SANDBOX',
#                               schema=decouple.config('SNOWFLAKE_USER'),
#                               quote_identifiers=False)


# flight_data_into_table()

# data_into_table(get_faker_table_ddl(), flight_data_to_df(), 'FLIGHT_REFERENCE_DATA_GENERATOR')
