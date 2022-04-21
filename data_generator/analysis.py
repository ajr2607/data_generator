from data_generator.utils import flight_data_to_df
from collections import Counter

flight_data = flight_data_to_df()
flight_data = flight_data.drop(flight_data.columns[[3, 4, 5, 6, 7, 9, 10, 12]], axis=1)
flight_data.columns = range(flight_data.columns.size)


airport_name = flight_data.iloc[:, 0].tolist()
city_name = flight_data.iloc[:, 1].tolist()
country_name = flight_data.iloc[:, 2].tolist()
timezone = flight_data.iloc[:, 3].tolist()
type_of_port = flight_data.iloc[:, 4].tolist()

# flight_data = flight_data[flight_data.iloc[:, 0].str.contains("unknown|\\N")==False]
# flight_data = flight_data[flight_data.iloc[:, 1].str.contains("unknown|\\N")==False]
# flight_data = flight_data[flight_data.iloc[:, 2] != 'unknown']
# flight_data = flight_data[flight_data.iloc[:, 3] != 'unknown']
# flight_data = flight_data[flight_data.iloc[:, 4] != 'unknown']

print(Counter(type_of_port))
