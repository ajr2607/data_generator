import pandas as pd
import snowflake.connector
from decouple import config
from faker import Faker

def generate_fake_sample_data():
    fake = Faker('en_GB')
    data = [fake.profile() for i in range(100)]
    df = pd.DataFrame(data)

def get_connection():
    ctx = snowflake.connector.connect(
        user=config('SNOWFLAKE_USER'),
        password=config('SNOWFLAKE_PASSWORD'),
        account=config('SNOWFLAKE_ACCOUNT'),
        database='SANDBOX',
        schema=config('SNOWFLAKE_USER')
    )
