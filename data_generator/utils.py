from pathlib import Path

import pandas as pd

import variable_file


def flight_data_to_df(sample_file_name):
    flight_file = Path(sample_file_name)
    initial_flight_data = pd.read_csv(flight_file, sep=",", header=None)
    initial_flight_data.drop(initial_flight_data.columns[0], axis=1, inplace=True)
    return initial_flight_data


def clean_flight_data(raw_flight_data, column_indexes_to_keep, unwanted_list_airport_names,
                      wanted_list_type_of_port, df_column_names):
    flight_data = raw_flight_data.drop(raw_flight_data.columns[column_indexes_to_keep], axis=1)
    flight_data.columns = range(flight_data.columns.size())
    flight_data = flight_data[-flight_data.iloc[:, 0].isin(unwanted_list_airport_names)]
    flight_data = flight_data[flight_data.iloc[:, 4].isin(wanted_list_type_of_port)]
    flight_data = flight_data[-flight_data.iloc[:, :].isin(['\\N'])]
    flight_data = flight_data.dropna()
    flight_data.columns = df_column_names
    return flight_data

raw_flight_data = flight_data_to_df(variable_file.sample_file_name)

print(clean_flight_data(raw_flight_data, variable_file.column_indexes_to_keep, variable_file.unwanted_list_airport_names,
                      variable_file.wanted_list_type_of_port, variable_file.df_column_names))