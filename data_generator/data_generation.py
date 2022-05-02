import numpy as np
import pandas as pd

from analysis import country_percentage_limit_finder, port_type_percentage_limit_finder, \
    timezone_percentage_limit_finder, airport_name_percentage_limit_finder, city_percentage_limit_finder
from analysis import port_counter_df, timezone_counter_df, airport_counter_df, city_counter_df, country_counter_df
from data_generator.utils import clean_flight_data

flight_data = clean_flight_data()

# TODO: function
# all
generated_data_2d_list = []

# port type
port_event = list(port_counter_df['event'])
port_percentage = port_type_percentage_limit_finder()
df_port_type_list = list(np.random.choice(port_event, size=100, p=port_percentage))
generated_data_2d_list.append(df_port_type_list)

# airport
airport_event = list(airport_counter_df['event'])
airport_percentage = airport_name_percentage_limit_finder()
df_airport_name_list = list(np.random.choice(airport_event, size=100, p=airport_percentage))
generated_data_2d_list.append(df_airport_name_list)

# city
city_event = list(city_counter_df['event'])
city_percentage = city_percentage_limit_finder()
df_city_list = list(np.random.choice(city_event, size=100, p=city_percentage))
generated_data_2d_list.append(df_city_list)

# country
country_event = list(country_counter_df['event'])
country_percentage = country_percentage_limit_finder()
df_country_list = list(np.random.choice(country_event, size=100, p=country_percentage))
generated_data_2d_list.append(df_country_list)

# timezone
timezone_event = list(timezone_counter_df['event'])
timezone_percentage = timezone_percentage_limit_finder()
df_timezone_list = list(np.random.choice(timezone_event, size=100, p=timezone_percentage))
generated_data_2d_list.append(df_timezone_list)

generated_df = pd.DataFrame.from_records(generated_data_2d_list)
generated_df = generated_df.transpose()
generated_df.columns = ["Port", "Airport", "City", "Country", "Timezone"]

# TODO: link data together: airport, city, country, timezone
