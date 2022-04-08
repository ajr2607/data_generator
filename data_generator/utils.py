from snowflake.connector.pandas_tools import write_pandas
from faker import Faker
import pandas as pd


def generate_sample_data_with_faker():
    if 'data' not in locals():
        fake = Faker('en_GB')
        data = [fake.profile() for i in range(100)]
        df = pd.DataFrame(data)


def data_into_table():
    get_connection()
    create_table()
    generate_sample_data_with_faker()
    cs = ctx.cursor()
    cs.execute(load_data)
    write_pandas(ctx, df, table_name='REFERENCE_DATA_GENERATOR', database='SANDBOX', schema=config('SNOWFLAKE_USER'),
                 quote_identifiers=False)
