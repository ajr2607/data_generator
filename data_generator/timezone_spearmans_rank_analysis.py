import os.path
import statistics
from collections import Counter
from pathlib import Path
from scipy import stats
import numpy as np

import pandas as pd

import analysis
import utils
import variable_file

flight_file = Path(variable_file.sample_file_name)
raw_flight_data = utils.flight_data_to_df(variable_file.sample_file_name)
flight_data = utils.clean_flight_data(raw_flight_data, variable_file.column_indexes_to_keep,
                                      variable_file.unwanted_list_airport_names,
                                      variable_file.wanted_list_type_of_port,
                                      variable_file.df_column_names)

timezone_event = Counter(flight_data['timezone']).most_common()
flight_timezone_split = sorted(timezone_event, key=lambda t: (t[1], t[0]), reverse=True)
flight_timezone_order = []
for x in flight_timezone_split:
    flight_timezone_order.append(x[0])


gen_timezone_all = []
timezone_split = []
correlations = []
generated_timezone_order = []
for number in range(len([name for name in os.listdir('generated_files')])):
    generated_data = pd.read_csv(os.path.join('generated_files', 'gen_data_' + str(number) + '.' + 'csv'))
    generated_data = generated_data.drop(['Unnamed: 0'], axis=1)
    generated_timezone_event = Counter(generated_data['timezone']).most_common()
    generated_timezone_split = sorted(generated_timezone_event, key=lambda t: (t[1], t[0]), reverse=True)
    generated_timezone_order = []
    for x in generated_timezone_split:
        generated_timezone_order.append(x[0])
    gen_timezone_all.append(generated_timezone_order)


timezone_one = gen_timezone_all[0]


for i in range(len(gen_timezone_all)):
    timezone_one = gen_timezone_all[i]
    max_number = len(timezone_one)
    if max_number == len(flight_timezone_order):
        correlation_ranking = stats.spearmanr(flight_timezone_order, timezone_one)
    elif max_number < len(flight_timezone_order):
        correlation_ranking = stats.spearmanr(flight_timezone_order[:max_number], timezone_one)
    correlations.append(correlation_ranking[0])

print(correlations)

# correlation_ranking = stats.spearmanr(flight_timezone_order[:len(gen_timezone_all[0])], timezone_one)

# correlation_ranking = stats.spearmanr(flight_timezone_order_list[:36], generated_timezone_order)
# correlations.append(correlation_ranking[0])

