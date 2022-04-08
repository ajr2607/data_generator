import snowflake.connector
from decouple import config


def get_connection():
    ctx = snowflake.connector.connect(
        user=config('SNOWFLAKE_USER'),
        password=config('SNOWFLAKE_PASSWORD'),
        account=config('SNOWFLAKE_ACCOUNT'),
        database='SANDBOX',
        schema=config('SNOWFLAKE_USER')
    )
