import snowflake.connector
from decouple import config

ctx = snowflake.connector.connect(
    user=config('SNOWFLAKE_USER'),
    password=config('SNOWFLAKE_PASSWORD'),
    account=config('SNOWFLAKE_ACCOUNT')
)
cs = ctx.cursor()

sql = "USE TABLE reference_data_generator"
cs.execute(sql)

sql = "SELECT 1"
cs.execute(sql)




