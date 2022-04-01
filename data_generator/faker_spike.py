import pandas as pd
import snowflake.connector
from decouple import config
from faker import Faker
from snowflake.connector.pandas_tools import write_pandas

fake = Faker('en_GB')

exp = Faker(['en_GB'])
data = [exp.profile() for i in range(100)]
df = pd.DataFrame(data)

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
    write_pandas(ctx, df, table_name='reference_data_generator', database='SANDBOX', schema=config('SNOWFLAKE_USER'))
ctx.close()
