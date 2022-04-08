from snowflake.connector.pandas_tools import write_pandas

def data_into_table():
    get_connection()
    cs = ctx.cursor()
    cs.execute(load_data_into_table_sql)
    write_pandas(ctx, df, table_name='REFERENCE_DATA_GENERATOR', database='SANDBOX', schema=config('SNOWFLAKE_USER'),
             quote_identifiers=False)