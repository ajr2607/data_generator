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
flight_file = Path('/home/amyrymer/PycharmProjects/most_recent_data_generator/data_generator')
raw_flight_data = utils.flight_data_to_df('gen_data_0.csv')

keep = []

flight_data = utils.clean_flight_data(raw_flight_data, keep,
                                      variable_file.unwanted_list_airport_names,
                                      variable_file.wanted_list_type_of_port,
                                      variable_file.df_column_names)

# generated data
number_of_rows = []
number_of_unique_rows = []
mean_timezone = []
port_type_split = []
timezone_split = []
how_many_timezones = []
number_generated_rows_needed_for_all_poss_rows = []

number_of_rows.append(len(flight_data))
number_of_unique_flight_rows = flight_data.drop_duplicates()
number_of_unique_rows.append(len(number_of_unique_flight_rows))
flight_data = flight_data.astype({'timezone': float})
flight_data_timezone_mean = statistics.fmean(flight_data['timezone'])
mean_timezone.append(round(flight_data_timezone_mean, 3))
port_event = Counter(flight_data['type_of_port'])
port_type_split.append([v for k, v in port_event.most_common()])
timezone_event = Counter(flight_data['timezone'])
timezone_split.append(sorted(timezone_event.items(), key=lambda t: (t[1], t[0]), reverse=True))
how_many_timezones.append(len(timezone_event))
c_row_list_flight = list(flight_data.value_counts())
percentages_of_rows_flight = analysis.row_event_perc_finder(c_row_list_flight, flight_data)
flight_num_rows_gen_to_give_all_poss_rows = 1 / percentages_of_rows_flight[-1]
number_generated_rows_needed_for_all_poss_rows.append(round(flight_num_rows_gen_to_give_all_poss_rows))

for number in range(len([name for name in os.listdir('generated_files')])):
    generated_data = pd.read_csv(os.path.join('generated_files', 'gen_data_' + str(number) + '.' + 'csv'))
    generated_data = generated_data.drop(['Unnamed: 0'], axis=1)
    number_of_rows.append(len(generated_data))
    generated_data_unique_rows = generated_data.drop_duplicates()
    number_of_unique_rows.append(len(generated_data_unique_rows))
    generated_data = generated_data.astype({'timezone': float})
    generated_data_timezone_mean = statistics.fmean(generated_data['timezone'])
    mean_timezone.append(round(generated_data_timezone_mean, 3))
    generated_port_event = Counter(generated_data['type_of_port'])
    port_type_split.append([v for k, v in generated_port_event.most_common()])
    port_percs = [[round(item * 100 / number_of_rows[0], 2) for item in subl] for subl in port_type_split]
    generated_timezone_event = Counter(generated_data['timezone'])
    timezone_split.append(sorted(generated_timezone_event.items(), key=lambda t: (t[1], t[0]), reverse=True))
    how_many_timezones.append(len(generated_timezone_event))
    c_row_list_gen = list(generated_data.value_counts())
    percentages_of_rows_gen = analysis.row_event_perc_finder(c_row_list_gen, generated_data)
    rows_gen_to_give_all_poss_rows = 1 / percentages_of_rows_gen[-1]
    number_generated_rows_needed_for_all_poss_rows.append(round(rows_gen_to_give_all_poss_rows))

print(number_of_rows)
print(number_of_unique_rows)
print(mean_timezone)
print(port_percs)
print(how_many_timezones)
print(number_generated_rows_needed_for_all_poss_rows)
