from data_generator.utils import flight_data_to_df
from collections import Counter

flight_data = flight_data_to_df()
print(flight_data.shape)

# print(Counter(flight_data.iloc[:,0]))
