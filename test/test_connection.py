import snowflake.connector
from decouple import config
import pytest
from unittest import mock

ctx = snowflake.connector.connect(
    user=config('SNOWFLAKE_USER'),
    password=config('SNOWFLAKE_PASSWORD'),
    account=config('SNOWFLAKE_ACCOUNT')
)
cs = ctx.cursor()


@mock.patch('snowflake.connector.connect')
def test_connection(mock_snowflake_connector):
    test_creds = {'username': 'test_user',
                  'password': 'test_password',
                  'account': 'test_account',
                  'role': 'test_role',
                  'warehouse': 'test_warehouse'}

    mock_con = mock_snowflake_connector.return_value
    mock_cur = mock_con.cursor.return_value
    mock_snowflake_connector.assert_called_once_with(**test_creds)
