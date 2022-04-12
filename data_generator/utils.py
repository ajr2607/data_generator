import pandas as pd
from faker import Faker
from snowflake.connector.pandas_tools import write_pandas


def generate_sample_data_with_faker():
    if 'faker_data' not in locals():
        fake = Faker('en_GB')
        faker_data = [fake.profile() for i in range(100)]
        faker_df = pd.DataFrame(faker_data)


def flight_data_to_df():
    flight_df = pd.DataFrame('airports_extended.txt')  # TODO: relative path????


def faker_data_into_table():
    get_connection()
    create_faker_table()
    cs = ctx.cursor()
    cs.execute(create_faker_table())
    write_pandas(ctx, faker_df, table_name='FAKER_REFERENCE_DATA_GENERATOR', database='SANDBOX',
                 schema=config('SNOWFLAKE_USER'),
                 quote_identifiers=False)


def flight_data_into_table():
    get_connection()
    cs = ctx.cursor()
    cs.execute(create_flight_table())
    write_pandas(ctx, flight_df, table_name='FLIGHT_REFERENCE_DATA_GENERATOR', database='SANDBOX',
                 schema=config('SNOWFLAKE_USER'),
                 quote_identifiers=False)
