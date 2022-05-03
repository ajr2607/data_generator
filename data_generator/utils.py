from pathlib import Path

from faker import Faker


def generate_sample_data_with_faker():
    if 'faker_data' not in locals():  # TODO: is data in db not locals
        fake = Faker('en_GB')
        faker_data = [fake.profile() for i in range(100)]
        faker_df = pd.DataFrame(faker_data)
        return faker_df


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


from data_generator.utils import clean_flight_data
from collections import Counter
import pandas as pd

flight_data = clean_flight_data()

c_timezone = Counter(flight_data['timezone'])
timezone_counter = [(timezone_value, c_timezone[timezone_value] / len(flight_data['timezone']) * 100.0)
                   for timezone_value, count in c_timezone.most_common()]
timezone_counter_df = pd.DataFrame.from_records(list(dict(timezone_counter).items()), columns=['event', 'percentage'])
timezone_total_percentage = timezone_counter_df['percentage'].sum()
