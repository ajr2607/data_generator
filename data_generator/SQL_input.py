def create_faker_table():
    create_table_sql = "CREATE OR REPLACE TABLE faker_reference_data_generator (job TEXT, company TEXT, " \
                       "ssn TEXT, residence TEXT, current_location TEXT, blood_group TEXT, website TEXT, " \
                       "username TEXT, name TEXT, sex TEXT, address TEXT, mail TEXT, birthdate TEXT)"


def create_flight_table():
    create_flight_table_sql = "CREATE OR REPLACE TABLE flight_reference_data_generator (Airport_ID TEXT, Name TEXT, " \
                              "City TEXT, Country TEXT, IATA TEXT, ICAO TEXT, Latitude TEXT, Longitude TEXT, " \
                              "Altitude TEXT, Timezone TEXT, DST TEXT, Tz_database_time_zone	 TEXT, Type TEXT, " \
                              "Source TEXT)"
