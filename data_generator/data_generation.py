from random import random

from analysis import port_counter_df
from analysis import port_type_percentage_limit_finder
from data_generator.utils import clean_flight_data

flight_data = clean_flight_data()

# TODO: generate data in proportion with sample data
generated_data_2d_list = [[], [], [], [], []]

# Port data generation
port_generated_list = generated_data_2d_list[0]

percentage = port_type_percentage_limit_finder()


def port_type_dist():
    x = random()
    if percentage[0] < x <= percentage[1]:
        return port_generated_list.append(port_counter_df.iloc[0, 0])
    elif percentage[1] < x <= percentage[2]:
        return port_generated_list.append(port_counter_df.iloc[1, 0])
    elif percentage[2] < x:
        return port_generated_list.append(port_counter_df.iloc[2, 0])


# def timezone_dist():
#     x = random()
#     if percentage[0] < x <= percentage[1]:
#         return port_generated_list.append('airport')
#     elif percentage[1] < x <= percentage[2]:
#         return port_generated_list.append('station')
#     elif percentage[2] < x:
#         return port_generated_list.append('port')


def generate_port_type(how_many):
    for i in range(how_many):
        port_type_dist()
    return port_generated_list


test_generate = generate_port_type(100)  # example

# TODO: airport, city, country, timezone
# timezones


# TODO: link data together: airport, city, country, timezone
