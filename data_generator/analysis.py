from random import random
from collections import Counter

import pandas as pd

from data_generator.utils import flight_data_to_df

flight_data = flight_data_to_df()
flight_data = flight_data.drop(flight_data.columns[[3, 4, 5, 6, 7, 9, 10, 12]], axis=1)
flight_data.columns = range(flight_data.columns.size)

unwanted_list_airport_names = ['All Airports', 'Railway Station', 'Train Station']
flight_data = flight_data[-flight_data.iloc[:, 0].isin(unwanted_list_airport_names)]
wanted_list_type_of_port = ['airport', 'station', 'port']
flight_data = flight_data[flight_data.iloc[:, 4].isin(wanted_list_type_of_port)]
flight_data = flight_data[-flight_data.iloc[:, :].isin(['\\N'])]
flight_data = flight_data.dropna()

# TODO: put above in utils?

airport_name = flight_data.iloc[:, 0].tolist()
city_name = flight_data.iloc[:, 1].tolist()  # linked to airport and country
country_name = flight_data.iloc[:, 2].tolist()  # linked to airport and city
timezone = flight_data.iloc[:, 3].tolist()  # linked to above
type_of_port = flight_data.iloc[:, 4].tolist()  # airport, station or port

# c_airport = Counter(airport_name)  # TODO: general function for these
# airport_counter = [(airport_name_value, c_airport[airport_name_value] / len(airport_name) * 100.0)
#                    for airport_name_value, count in c_airport.most_common()]
# airport_counter_df = pd.DataFrame.from_records(list(dict(airport_counter).items()), columns=['event', 'percentage'])
# airport_total_percentage = airport_counter_df['percentage'].sum()  # not quite 100
#
# c_city = Counter(city_name)
# city_counter = [(city_name_value, c_city[city_name_value] / len(city_name) * 100.0)
#                 for city_name_value, count in c_city.most_common()]
# city_counter_df = pd.DataFrame.from_records(list(dict(city_counter).items()), columns=['event', 'percentage'])
# city_total_percentage = city_counter_df['percentage'].sum()  # TODO: maybe only top 100 most common countries
#
# c_country = Counter(country_name)
# country_counter = [(country_name_value, c_country[country_name_value] / len(country_name) * 100.0)
#                    for country_name_value, count in c_country.most_common()]
# country_counter_df = pd.DataFrame.from_records(list(dict(country_counter).items()), columns=['event', 'percentage'])
# country_total_percentage = country_counter_df['percentage'].sum()
#
# c_timezone = Counter(timezone)
# timezone_counter = [(timezone_name_value, c_timezone[timezone_name_value] / len(timezone) * 100.0)
#                     for timezone_name_value, count in c_timezone.most_common()]
# timezone_counter_df = pd.DataFrame.from_records(list(dict(timezone_counter).items()), columns=['event', 'percentage'])
# timezone_total_percentage = timezone_counter_df['percentage'].sum()
#
# c_port = Counter(type_of_port)
# port_counter = [(port_value, c_port[port_value] / len(type_of_port) * 100.0)
#                 for port_value, count in c_port.most_common()]
# port_counter_df = pd.DataFrame.from_records(list(dict(port_counter).items()), columns=['event', 'percentage'])
# port_total_percentage = port_counter_df['percentage'].sum()

# TODO: generate data in proportion with sample data

port_generated_list = []

def port_type_dist():
    x = random()
    if x < 0.85:
        return port_generated_list.append('airport')
    elif 0.85 < x < 0.99:
        return port_generated_list.append('station')
    else:
        return port_generated_list.append('port')

def generate_port_type(how_many):
    for i in range(how_many):
        port_generated_list.append(port_type_dist())




# TODO: link data together: airport, city, country, timezone
