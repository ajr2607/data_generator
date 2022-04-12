def get_faker_table_ddl():
    create_faker_table_sql = "CREATE OR REPLACE TABLE faker_reference_data_generator (job TEXT, company TEXT, " \
                       "ssn TEXT, residence TEXT, current_location TEXT, blood_group TEXT, website TEXT, " \
                       "username TEXT, name TEXT, sex TEXT, address TEXT, mail TEXT, birthdate TEXT)"
    return create_faker_table_sql


def get_flight_table_ddl():
    create_flight_table_sql = "CREATE OR REPLACE TABLE flight_reference_data_generator (Airport_ID TEXT, Name TEXT, " \
                              "City TEXT, Country TEXT, IATA TEXT, ICAO TEXT, Latitude TEXT, Longitude TEXT, " \
                              "Altitude TEXT, Timezone TEXT, DST TEXT, Tz_database_time_zone	 TEXT, Type TEXT, " \
                              "Source TEXT)"
    return create_flight_table_sql
