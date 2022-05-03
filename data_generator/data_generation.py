import numpy as np
import pandas as pd

from analysis import row_event_perc_finder, get_row_event


# TODO: function


def convert_seq_to_list():
    row_event = get_row_event()
    for item in range(len(row_event)):
        row_event[item] = list(row_event[item])
    return row_event


def generate_placeholder_data():
    row_event = convert_seq_to_list()
    row_event_initial = list(range(0, len(row_event)))  # won't let me put a list as the row_event so using
    # row_event_initial as a placeholder and replacing with the list later
    new_rows_percs = row_event_perc_finder()
    new_rows_list = list(np.random.choice(row_event_initial, size=10000, p=new_rows_percs))
    # generating integers to be used as index for 2d list to replace integers with lists
    return new_rows_list


def replace_placeholder_num_with_event():
    row_event = convert_seq_to_list()
    new_rows_list = generate_placeholder_data()
    gen_list_final_maybe = []
    for i in range(len(new_rows_list)):
        gen_list_final_maybe.append(row_event[new_rows_list[
            i]])  # using generated integers as the index, append list from 2d list to gen_list_final_maybe
    generated_data_final = replace_placeholder_num_with_event()
    generated_data_final_df = pd.DataFrame(generated_data_final, columns=['airport_name', 'city_name', 'country_name',
                                                                          'timezone', 'type_of_port'])
    return generated_data_final_df

# print(new_rows_list[0])
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
