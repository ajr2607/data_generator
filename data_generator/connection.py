import snowflake.connector
import decouple


def get_connection():
    ctx = snowflake.connector.connect(
        user=decouple.config('SNOWFLAKE_USER'),
        password=decouple.config('SNOWFLAKE_PASSWORD'),
        account=decouple.config('SNOWFLAKE_ACCOUNT'),
        database='SANDBOX',
        schema=decouple.config('SNOWFLAKE_USER')
    )

    return ctx
