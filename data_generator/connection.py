import pandas as pd
import snowflake.connector
from decouple import config
from faker import Faker
from snowflake.connector.pandas_tools import write_pandas

fake = Faker('en_GB')

data = [fake.profile() for i in range(100)]
df = pd.DataFrame(data)

ctx = snowflake.connector.connect(
    user=config('SNOWFLAKE_USER'),
    password=config('SNOWFLAKE_PASSWORD'),
    account=config('SNOWFLAKE_ACCOUNT')
)
cs = ctx.cursor()

sql = "USE DATABASE SANDBOX"
cs.execute(sql)

sql = "USE SCHEMA AMY_RYMER"
cs.execute(sql)

cs = ctx.cursor()
sql = "CREATE OR REPLACE TABLE reference_data_generator (job TEXT, company TEXT, ssn TEXT, residence TEXT, " \
      "current_location TEXT, blood_group TEXT, website TEXT, username TEXT, name TEXT, sex TEXT, address TEXT, " \
      "mail TEXT, birthdate TEXT)"
cs.execute(sql)

write_pandas(ctx, df, table_name='REFERENCE_DATA_GENERATOR', database='SANDBOX', schema=config('SNOWFLAKE_USER'),
             quote_identifiers=False)
