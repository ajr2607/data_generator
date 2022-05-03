from utils import flight_data_to_df, clean_flight_data
from analysis import row_numbers, get_row_event, row_event_perc_finder
from data_generation import convert_seq_to_list, generate_placeholder_data, replace_placeholder_num_with_event

if __name__ == '__main__':

    flight_data_to_df()

    clean_flight_data()

    row_numbers()

    get_row_event()

    row_event_perc_finder()

    convert_seq_to_list()

    generate_placeholder_data()

    replace_placeholder_num_with_event()
