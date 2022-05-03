from collections import Counter
from pathlib import Path

import pandas as pd


def flight_data_to_df():
    flight_file = Path('airports_extended.txt')
    flight_data = pd.read_csv(flight_file, sep=",", header=None)
    flight_data.drop(flight_data.columns[0], axis=1, inplace=True)
    return flight_data


def clean_flight_data():
    flight_data = flight_data_to_df()
    flight_data = flight_data.drop(flight_data.columns[[3, 4, 5, 6, 7, 9, 10, 12]], axis=1)
    flight_data.columns = range(flight_data.columns.size)
    unwanted_list_airport_names = ['All Airports', 'Railway Station', 'Train Station']
    flight_data = flight_data[-flight_data.iloc[:, 0].isin(unwanted_list_airport_names)]
    wanted_list_type_of_port = ['airport', 'station', 'port']
    flight_data = flight_data[flight_data.iloc[:, 4].isin(wanted_list_type_of_port)]
    flight_data = flight_data[-flight_data.iloc[:, :].isin(['\\N'])]
    flight_data = flight_data.dropna()
    flight_data.columns = ['airport_name', 'city_name', 'country_name', 'timezone', 'type_of_port']
    return flight_data
