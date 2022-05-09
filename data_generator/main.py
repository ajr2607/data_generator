from pathlib import Path

import analysis
import data_generation as dg
import utils
import variable_file

if __name__ == '__main__':
    # gen_data_to_csv(variable_file.how_many_datasets)

    flight_file = Path(variable_file.sample_file_name)

    raw_flight_data = utils.flight_data_to_df(variable_file.sample_file_name)

    flight_data = utils.clean_flight_data(raw_flight_data, variable_file.column_indexes_to_keep,
                                          variable_file.unwanted_list_airport_names,
                                          variable_file.wanted_list_type_of_port,
                                          variable_file.df_column_names)

    c_row_list = list(flight_data.value_counts())

    row_events = analysis.get_row_event(flight_data)

    new_rows_percs = analysis.row_event_perc_finder(c_row_list, flight_data)

    # row_events = analysis.convert_seq_to_list(row_events)

    placeholder_data = dg.generate_placeholder_data(row_events, variable_file.number_of_rows_to_generate,
                                                    new_rows_percs)

    save_loc_for_gen_data = Path('generated_files')

    dg.gen_data_to_csv(variable_file.how_many_datasets, placeholder_data, row_events, save_loc_for_gen_data)
