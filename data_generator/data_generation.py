from random import random
from collections import Counter

# TODO: generate data in proportion with sample data
generated_data_2d_list = [[], [], [], [], []]

# Port data generation
port_generated_list = generated_data_2d_list[0]


def port_type_dist():
    x = random()
    if x < 0.84:  # limits are from analysis counter dataframes. change to reference to those instead of values.
        return port_generated_list.append('airport')
    elif 0.84 < x <= 0.99:
        return port_generated_list.append('station')
    elif 0.99 < x:
        return port_generated_list.append('port')


def generate_port_type(how_many):
    for i in range(how_many):
        port_type_dist()
    return port_generated_list


# TODO: make configurable: use variables instead of values for percentage limits. TEST.
test_generate = generate_port_type(1000)  # example


# TODO: airport, city, country, timezone
# timezones



# TODO: link data together: airport, city, country, timezone
