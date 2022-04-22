from random import random

from analysis import port_counter_df, timezone_counter_df
from analysis import port_type_percentage_limit_finder
from data_generator.utils import clean_flight_data

flight_data = clean_flight_data()

# TODO: generate data in proportion with sample data
generated_data_2d_list = [[], [], [], [], []]

# Port data generation
port_generated_list = generated_data_2d_list[0]
timezone_generated_list = generated_data_2d_list[1]

percentage = port_type_percentage_limit_finder()


def port_type_dist():
    x = random()
    if percentage[0] < x <= percentage[1]:
        return port_generated_list.append(port_counter_df.iloc[0, 0])
    elif percentage[1] < x <= percentage[2]:
        return port_generated_list.append(port_counter_df.iloc[1, 0])
    elif percentage[2] < x:
        return port_generated_list.append(port_counter_df.iloc[2, 0])


def timezone_dist(): # TODO: finish all percentages - must be a way to use for loop to iterate through all 40 %s.
    x = random()
    if percentage[0] < x <= percentage[1]:
        return timezone_generated_list.append(timezone_counter_df.iloc[0, 0])
    elif percentage[1] < x <= percentage[2]:
        return timezone_generated_list.append(timezone_counter_df.iloc[1, 0])
    elif percentage[2] < x <= percentage[3]:
        return timezone_generated_list.append(timezone_counter_df.iloc[2, 0])
    elif percentage[3] < x <= percentage[4]:
        return timezone_generated_list.append(timezone_counter_df.iloc[3, 0])
    elif percentage[4] < x <= percentage[5]:
        return timezone_generated_list.append(timezone_counter_df.iloc[4, 0])
    elif percentage[5] < x <= percentage[6]:
        return timezone_generated_list.append(timezone_counter_df.iloc[5, 0])
    elif percentage[6] < x <= percentage[7]:
        return timezone_generated_list.append(timezone_counter_df.iloc[6, 0])
    elif percentage[7] < x <= percentage[8]:
        return timezone_generated_list.append(timezone_counter_df.iloc[7, 0])
    elif percentage[8] < x <= percentage[9]:
        return timezone_generated_list.append(timezone_counter_df.iloc[8, 0])


def generate_port_type(how_many):
    for i in range(how_many):
        port_type_dist()
    return port_generated_list


def generate_timezone(how_many):
    for i in range(how_many):
        timezone_dist()
    return timezone_generated_list


test_generate = generate_port_type(100)  # example

test_generate_2 = generate_timezone(100)

# TODO: airport, city, country, timezone
# timezones


# TODO: link data together: airport, city, country, timezone
