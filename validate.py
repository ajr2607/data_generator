import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from decouple import config

# Gets the version
ctx = snowflake.connector.connect(
    user=config('SNOWFLAKE_USER'),
    password=config('SNOWFLAKE_PASSWORD'),
    account=config('SNOWFLAKE_ACCOUNT')
    )
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()
