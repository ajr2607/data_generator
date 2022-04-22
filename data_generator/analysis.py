from collections import Counter
import pandas as pd
import numpy as np

from data_generator.utils import clean_flight_data

flight_data = clean_flight_data()

# TODO: put above in utils?

c_airport = Counter(flight_data['airport_name'])  # TODO: general function for these
airport_counter = [(airport_name_value, c_airport[airport_name_value] / len(flight_data['airport_name']) * 100.0)
                   for airport_name_value, count in c_airport.most_common()]
airport_counter_df = pd.DataFrame.from_records(list(dict(airport_counter).items()), columns=['event', 'percentage'])
airport_total_percentage = airport_counter_df['percentage'].sum()  # not quite 100

c_city = Counter(flight_data['city_name'])
city_counter = [(city_name_value, c_city[city_name_value] / len(flight_data['city_name']) * 100.0)
                for city_name_value, count in c_city.most_common()]
city_counter_df = pd.DataFrame.from_records(list(dict(city_counter).items()), columns=['event', 'percentage'])
city_total_percentage = city_counter_df['percentage'].sum()  # TODO: maybe only top 100 most common countries

c_country = Counter(flight_data['country_name'])
country_counter = [(country_name_value, c_country[country_name_value] / len(flight_data['country_name']) * 100.0)
                   for country_name_value, count in c_country.most_common()]
country_counter_df = pd.DataFrame.from_records(list(dict(country_counter).items()), columns=['event', 'percentage'])
country_total_percentage = country_counter_df['percentage'].sum()

c_timezone = Counter(flight_data['timezone'])
timezone_counter = [(timezone_value, round((c_timezone[timezone_value] / len(flight_data['timezone']) * 100.0)))
                    for timezone_value, count in c_timezone.most_common()]
timezone_counter_df = pd.DataFrame.from_records(list(dict(timezone_counter).items()), columns=['event', 'percentage'])
timezone_total_percentage = timezone_counter_df['percentage'].sum()

c_port = Counter(flight_data['type_of_port'])
port_counter = [(port_value, round((c_port[port_value] / len(flight_data['type_of_port']) * 100.0)))
                for port_value, count in c_port.most_common()]
port_counter_df = pd.DataFrame.from_records(list(dict(port_counter).items()), columns=['event', 'percentage'])
port_total_percentage = port_counter_df['percentage'].sum()


def timezone_percentage_limit_finder():  # TODO: repeat for other columns
    percentage_limits_timezone = [0]  # TODO: general function needed
    for i in range(len(timezone_counter_df)):
        percentage_limit = (timezone_counter_df.iloc[i, 1] / 100)
        percentage_limits_timezone.append(percentage_limit)
    cumulative_percentage_limits_timezone = np.cumsum(percentage_limits_timezone)
    return cumulative_percentage_limits_timezone


def port_type_percentage_limit_finder():
    percentage_limits_port_type = [0]
    for i in range(len(port_counter_df)):
        percentage_limit = port_counter_df.iloc[i, 1] / 100
        percentage_limits_port_type.append(percentage_limit)
    cumulative_percentage_limits_port_type = np.cumsum(percentage_limits_port_type)
    return cumulative_percentage_limits_port_type

def airport_name_percentage_limit_finder():
    percentage_limits_airport_name = [0]
    for i in range(len(airport_counter_df)):
        percentage_limit = airport_counter_df.iloc[i, 1] / 100
        percentage_limits_airport_name.append(percentage_limit)
    cumulative_percentage_limits_airport_name = np.cumsum(percentage_limits_airport_name)
    return cumulative_percentage_limits_airport_name

def country_percentage_limit_finder():
    percentage_limits_country = [0]
    for i in range(len(country_counter_df)):
        percentage_limit = country_counter_df.iloc[i, 1] / 100
        percentage_limits_country.append(percentage_limit)
    cumulative_percentage_limits_country = np.cumsum(percentage_limits_country)
    return cumulative_percentage_limits_country

def city_percentage_limit_finder():
    percentage_limits_city = [0]
    for i in range(len(city_counter_df)):
        percentage_limit = city_counter_df.iloc[i, 1] / 100
        percentage_limits_city.append(percentage_limit)
    cumulative_percentage_limits_city = np.cumsum(percentage_limits_city)
    return cumulative_percentage_limits_city


print(len(timezone_percentage_limit_finder()))
print(len(port_type_percentage_limit_finder()))

print(port_counter_df.iloc[1,0])
