from collections import Counter
import pandas as pd

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
timezone_counter = [(timezone_name_value, c_timezone[timezone_name_value] / len(['timezone']) * 100.0)
                    for timezone_name_value, count in c_timezone.most_common()]
timezone_counter_df = pd.DataFrame.from_records(list(dict(timezone_counter).items()), columns=['event', 'percentage'])
timezone_total_percentage = timezone_counter_df['percentage'].sum()

c_port = Counter(flight_data['type_of_port'])
port_counter = [(port_value, c_port[port_value] / len(flight_data['type_of_port']) * 100.0)
                for port_value, count in c_port.most_common()]
port_counter_df = pd.DataFrame.from_records(list(dict(port_counter).items()), columns=['event', 'percentage'])
port_total_percentage = port_counter_df['percentage'].sum()
