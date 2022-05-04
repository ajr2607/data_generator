import variable_file
from utils import flight_data_to_df, clean_flight_data
from analysis import row_numbers, get_row_event, row_event_perc_finder
from data_generation import convert_seq_to_list, generate_placeholder_data, replace_placeholder_num_with_event

if __name__ == '__main__':

    raw_flight_data = flight_data_to_df(variable_file.sample_file_name)

    flight_data = clean_flight_data(raw_flight_data, variable_file.column_indexes_to_keep,
                                    variable_file.unwanted_list_airport_names, variable_file.wanted_list_type_of_port,
                                    variable_file.df_column_names)

    row_numbers()

    get_row_event()

    row_event_perc_finder()

    convert_seq_to_list()

    generate_placeholder_data(variable_file.number_of_rows_to_generate)

    replace_placeholder_num_with_event(variable_file.number_of_rows_to_generate, variable_file.df_column_names)
