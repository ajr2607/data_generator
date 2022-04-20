from data_generator.utils import flight_data_to_df
from collections import Counter

flight_data = flight_data_to_df()

airport_name = flight_data.iloc[:, 0].tolist()
city_name = flight_data.iloc[:, 1].tolist()
country_name = flight_data.iloc[:, 2].tolist()
iata = flight_data.iloc[:, 3].tolist()
icao = flight_data.iloc[:, 4].tolist()
latitude = flight_data.iloc[:, 5].tolist()
longitude = flight_data.iloc[:, 6].tolist()
altitude = flight_data.iloc[:, 7].tolist()
timezone = flight_data.iloc[:, 8].tolist()
dst = flight_data.iloc[:, 9].tolist()
tz_database_timezone = flight_data.iloc[:, 10].tolist()
type_of_port = flight_data.iloc[:, 11].tolist()
source = flight_data.iloc[:, 12].tolist()

print(len(set(Counter(airport_name))))
