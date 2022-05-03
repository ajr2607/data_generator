import pandas as pd

from data_generator.utils import clean_flight_data


def row_numbers():
    flight_data = clean_flight_data()
    c_row_list = list(flight_data.value_counts())
    return c_row_list


def get_row_event():
    flight_data = clean_flight_data()
    c_row_df = pd.DataFrame(flight_data.value_counts())
    row_event = c_row_df.index.tolist()
    return row_event


def row_event_perc_finder():
    flight_data = clean_flight_data()
    c_row_list = row_numbers()
    row_event_percs_list = []
    for i in range(len(c_row_list)):
        percs_row = c_row_list[i] / len(flight_data)
        row_event_percs_list.append(percs_row)
    return row_event_percs_list

# c_airport = Counter(flight_data['airport_name'])
# airport_counter = [(airport_name_value, c_airport[airport_name_value] / len(flight_data['airport_name']) * 100.0)
#                    for airport_name_value, count in c_airport.most_common()]
# airport_counter_df = pd.DataFrame.from_records(list(dict(airport_counter).items()), columns=['event', 'percentage'])
# airport_total_percentage = airport_counter_df['percentage'].sum()  # not quite 100
#
# c_city = Counter(flight_data['city_name'])
# city_counter = [(city_name_value, c_city[city_name_value] / len(flight_data['city_name']) * 100.0)
#                 for city_name_value, count in c_city.most_common()]
# city_counter_df = pd.DataFrame.from_records(list(dict(city_counter).items()), columns=['event', 'percentage'])
# city_total_percentage = city_counter_df['percentage'].sum()
#
# c_country = Counter(flight_data['country_name'])
# country_counter = [(country_name_value, c_country[country_name_value] / len(flight_data['country_name']) * 100.0)
#                    for country_name_value, count in c_country.most_common()]
# country_counter_df = pd.DataFrame.from_records(list(dict(country_counter).items()), columns=['event', 'percentage'])
# country_total_percentage = country_counter_df['percentage'].sum()
#
# c_timezone = Counter(flight_data['timezone'])
# timezone_counter = [(timezone_value, (c_timezone[timezone_value] / len(flight_data['timezone']) * 100.0))
#                     for timezone_value, count in c_timezone.most_common()]
# timezone_counter_df = pd.DataFrame.from_records(list(dict(timezone_counter).items()), columns=['event', 'percentage'])
# timezone_total_percentage = timezone_counter_df['percentage'].sum()
#
# c_port = Counter(flight_data['type_of_port'])
# port_counter = [(port_value, (c_port[port_value] / len(flight_data['type_of_port']) * 100.0))
#                 for port_value, count in c_port.most_common()]
# port_counter_df = pd.DataFrame.from_records(list(dict(port_counter).items()), columns=['event', 'percentage'])
# port_total_percentage = port_counter_df['percentage'].sum()


# def timezone_percentage_limit_finder():
#     percentage_limits_timezone = []
#     for i in range(len(timezone_counter_df)):
#         percentage_limit = (timezone_counter_df.iloc[i, 1] / 100)
#         percentage_limits_timezone.append(percentage_limit)
#     return percentage_limits_timezone
#
#
# def port_type_percentage_limit_finder():
#     percentage_limits_port_type = []
#     for i in range(len(port_counter_df)):
#         percentage_limit = port_counter_df.iloc[i, 1] / 100
#         percentage_limits_port_type.append(percentage_limit)
#     return percentage_limits_port_type
#
#
# def airport_name_percentage_limit_finder():
#     percentage_limits_airport_name = []
#     for i in range(len(airport_counter_df)):
#         percentage_limit = airport_counter_df.iloc[i, 1] / 100
#         percentage_limits_airport_name.append(percentage_limit)
#     return percentage_limits_airport_name
#
#
# def country_percentage_limit_finder():
#     percentage_limits_country = []
#     for i in range(len(country_counter_df)):
#         percentage_limit = country_counter_df.iloc[i, 1] / 100
#         percentage_limits_country.append(percentage_limit)
#     return percentage_limits_country
#
#
# def city_percentage_limit_finder():
#     percentage_limits_city = []
#     for i in range(len(city_counter_df)):
#         percentage_limit = city_counter_df.iloc[i, 1] / 100
#         percentage_limits_city.append(percentage_limit)
#     return percentage_limits_city
