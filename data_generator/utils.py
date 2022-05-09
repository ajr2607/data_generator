import pandas as pd


def flight_data_to_df(flight_file):
    initial_flight_data = pd.read_csv(flight_file, sep=",", header=None)
    initial_flight_data.drop(initial_flight_data.columns[0], axis=1, inplace=True)
    return initial_flight_data


def clean_flight_data(raw_flight_data, column_indexes_to_keep, unwanted_list_airport_names,
                      wanted_list_type_of_port, df_column_names):
    flight_data = raw_flight_data.drop(raw_flight_data.columns[column_indexes_to_keep], axis=1)
    flight_data.columns = range(flight_data.shape[1])
    flight_data = flight_data[-flight_data.iloc[:, 0].isin(unwanted_list_airport_names)]
    flight_data = flight_data[flight_data.iloc[:, 4].isin(wanted_list_type_of_port)]
    flight_data = flight_data[-flight_data.iloc[:, :].isin(['\\N'])]
    flight_data = flight_data.dropna()
    flight_data.columns = df_column_names
    return flight_data
