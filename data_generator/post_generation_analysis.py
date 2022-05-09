import os.path
import statistics
from collections import Counter
from pathlib import Path

import pandas as pd

import analysis
import utils
import variable_file

# TODO: functions!

# sample data analysis
flight_file = Path(variable_file.sample_file_name)
raw_flight_data = utils.flight_data_to_df(variable_file.sample_file_name)
flight_data = utils.clean_flight_data(raw_flight_data, variable_file.column_indexes_to_keep,
                                      variable_file.unwanted_list_airport_names,
                                      variable_file.wanted_list_type_of_port,
                                      variable_file.df_column_names)

number_of_unique_flight_rows = flight_data.drop_duplicates()

flight_data = flight_data.astype({'timezone': float})

flight_data_timezone_mean = statistics.fmean(flight_data['timezone'])

port_event = Counter(flight_data['type_of_port'])

timezone_event = Counter(flight_data['timezone'])

c_row_list_flight = list(flight_data.value_counts())
percentages_of_rows_flight = analysis.row_event_perc_finder(c_row_list_flight, flight_data)
flight_num_rows_gen_to_give_all_poss_rows = 1 / percentages_of_rows_flight[-1]

# generated data
folder_location_generated_data = Path('generated_files')

for number in range(len([name for name in os.listdir('generated_files')])):
    file_name = 'gen_data_' + str(number) + '.csv'
    generated_data = pd.read_csv('generated_files', './', file_name)  # TODO: not working yet but surely not far off
    generated_data = generated_data.drop(generated_data.columns[[0]], axis=1, inplace=True)
    generated_data_unique_rows = generated_data.drop_duplicated()
    generated_data = generated_data.astype({'timezone': float})
    generated_data_timezone_mean = statistics.fmean(generated_data['timezone'])
    generated_port_event = Counter(generated_data['type_of_port'])
    generated_timezone_event = Counter(generated_data['timezone'])
    c_row_list_gen = list(generated_data.value_counts())
    percentages_of_rows_gen = analysis.row_event_perc_finder(c_row_list_gen, generated_data)
    generated_num_rows_gen_to_give_all_poss_rows = 1 / percentages_of_rows_gen[-1]

# gen_data_analysis = pd.read_csv('/home/amyrymer/PycharmProjects/data_generator/data_generator/generated_files/'
#                                 'gen_data_0.csv')
# gen_data_analysis.drop(gen_data_analysis.columns[[0]], axis=1, inplace=True)

# unique_generated_data_rows = gen_data_analysis.drop_duplicates()

# gen_data_analysis = gen_data_analysis.astype({'timezone': float})

# gen_data_timezone_mean = statistics.fmean(gen_data_analysis['timezone'])

# gen_port_event = Counter(gen_data_analysis['type_of_port'])

# gen_timezone_event = Counter(gen_data_analysis['timezone'])

# c_row_list_gen = list(gen_data_analysis.value_counts())
# percentages_of_rows_gen = analysis.row_event_perc_finder(c_row_list_gen, gen_data_analysis)
# generated_num_rows_gen_to_give_all_poss_rows = 1 / percentages_of_rows_gen[-1]

# analyse

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
