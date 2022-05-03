import numpy as np
import pandas as pd

from analysis import country_percentage_limit_finder, port_type_percentage_limit_finder, \
    timezone_percentage_limit_finder, airport_name_percentage_limit_finder, city_percentage_limit_finder
from analysis import port_counter_df, timezone_counter_df, airport_counter_df, city_counter_df, country_counter_df
from data_generator.utils import clean_flight_data

flight_data = clean_flight_data()

# TODO: function
# # all
# generated_data_2d_list = []



# # port type
# port_event = list(port_counter_df['event'])
# port_percentage = port_type_percentage_limit_finder()
# df_port_type_list = list(np.random.choice(port_event, size=10000, p=port_percentage))
# generated_data_2d_list.append(df_port_type_list)
#
# # country
# country_event = list(country_counter_df['event'])
# country_percentage = country_percentage_limit_finder()
# df_country_list = list(np.random.choice(country_event, size=10000, p=country_percentage))
# generated_data_2d_list.append(df_country_list)
#
# # city
# city_event = list(city_counter_df['event'])
# city_percentage = city_percentage_limit_finder()
# df_city_list = list(np.random.choice(city_event, size=10000, p=city_percentage))
# generated_data_2d_list.append(df_city_list)
#
# # timezone
# timezone_event = list(timezone_counter_df['event'])
# timezone_percentage = timezone_percentage_limit_finder()
# df_timezone_list = list(np.random.choice(timezone_event, size=10000, p=timezone_percentage))
# generated_data_2d_list.append(df_timezone_list)
#
# # airport
# airport_event = list(airport_counter_df['event'])
# airport_percentage = airport_name_percentage_limit_finder()
# df_airport_name_list = list(np.random.choice(airport_event, size=10000, p=airport_percentage))
# generated_data_2d_list.append(df_airport_name_list)
#
# generated_df = pd.DataFrame.from_records(generated_data_2d_list)
# generated_df = generated_df.transpose()
# generated_df.columns = ["Port", "Country", "City", "Timezone", "Airport"]

# TODO: link data together: airport, city, country, timezone

# generated_df_sort = generated_df.sort_values('Port')
#
# airports_only = generated_df[generated_df['Port'].str.contains('airport')]
# airports_only_sort_country = generated_df.sort_values('Country')
#
#
# ports_only = generated_df[~generated_df['Port'].str.contains('air|station')]
#
# stations_only = generated_df[generated_df['Port'].str.contains('station')]
#
# generated_df_no_dups = generated_df[~generated_df.duplicated()]
# # print(len(generated_df_no_dups))
# # print(len(generated_df))
#
# # print(generated_df.groupby('Country').mean())
#
# some_gen_data = generated_df.loc[:, ["Port", "Country", "Timezone"]]
# sort_some_gen_data = some_gen_data.sort_values('Country')
# print(sort_some_gen_data)
#
# data = clean_flight_data()
#
#
# data_sorted = data.sort_values('type_of_port')
#
# data_airports_only = data[data['type_of_port'].str.contains('airport')]
# ports_only = data[~data['type_of_port'].str.contains('air|station')]
# stations_only = data[data['type_of_port'].str.contains('station')]
#
# sorted_data_airports_only = data_airports_only.sort_values('country_name')
# sorted_data_ports_only = ports_only.sort_values('country_name')
# sorted_data_stations_only = stations_only.sort_values('city_name')

