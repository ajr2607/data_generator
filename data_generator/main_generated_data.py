from pathlib import Path

import analysis
import data_generation as dg
import utils
import variable_file

if __name__ == '__main__':
    flight_file = Path('/home/amyrymer/PycharmProjects/most_recent_data_generator/data_generator')

    raw_flight_data = utils.flight_data_to_df('gen_data_0.csv')

    keep = []

    flight_data = utils.clean_flight_data(raw_flight_data, keep,
                                          variable_file.unwanted_list_airport_names,
                                          variable_file.wanted_list_type_of_port,
                                          variable_file.df_column_names)

    c_row_list = list(flight_data.value_counts())

    row_events = analysis.get_row_event(flight_data)

    new_rows_percs = analysis.row_event_perc_finder(c_row_list, flight_data)

    placeholder_data = dg.generate_placeholder_data_for_multiple_sets(variable_file.how_many_datasets, row_events,
                                                                      variable_file.number_of_rows_to_generate,
                                                                      new_rows_percs)

    replace_placeholder0 = dg.replace_placeholder_num_with_event(0, variable_file.number_of_rows_to_generate,
                                                                 placeholder_data, row_events,
                                                                 variable_file.df_column_names)
    replace_placeholder1 = dg.replace_placeholder_num_with_event(1, variable_file.number_of_rows_to_generate,
                                                                 placeholder_data, row_events,
                                                                 variable_file.df_column_names)
    replace_placeholder2 = dg.replace_placeholder_num_with_event(2, variable_file.number_of_rows_to_generate,
                                                                 placeholder_data, row_events,
                                                                 variable_file.df_column_names)
    replace_placeholder3 = dg.replace_placeholder_num_with_event(3, variable_file.number_of_rows_to_generate,
                                                                 placeholder_data, row_events,
                                                                 variable_file.df_column_names)
    replace_placeholder4 = dg.replace_placeholder_num_with_event(4, variable_file.number_of_rows_to_generate,
                                                                 placeholder_data, row_events,
                                                                 variable_file.df_column_names)
    replace_placeholder5 = dg.replace_placeholder_num_with_event(5, variable_file.number_of_rows_to_generate,
                                                                 placeholder_data, row_events,
                                                                 variable_file.df_column_names)
    replace_placeholder6 = dg.replace_placeholder_num_with_event(6, variable_file.number_of_rows_to_generate,
                                                                 placeholder_data, row_events,
                                                                 variable_file.df_column_names)
    replace_placeholder7 = dg.replace_placeholder_num_with_event(7, variable_file.number_of_rows_to_generate,
                                                                 placeholder_data, row_events,
                                                                 variable_file.df_column_names)
    replace_placeholder8 = dg.replace_placeholder_num_with_event(8, variable_file.number_of_rows_to_generate,
                                                                 placeholder_data, row_events,
                                                                 variable_file.df_column_names)
    replace_placeholder9 = dg.replace_placeholder_num_with_event(9, variable_file.number_of_rows_to_generate,
                                                                 placeholder_data, row_events,
                                                                 variable_file.df_column_names)

    save_loc_for_gen_data = Path('generated_files')

    dg.gen_data_to_csv(0, save_loc_for_gen_data, replace_placeholder0)
    dg.gen_data_to_csv(1, save_loc_for_gen_data, replace_placeholder1)
    dg.gen_data_to_csv(2, save_loc_for_gen_data, replace_placeholder2)
    dg.gen_data_to_csv(3, save_loc_for_gen_data, replace_placeholder3)
    dg.gen_data_to_csv(4, save_loc_for_gen_data, replace_placeholder4)
    dg.gen_data_to_csv(5, save_loc_for_gen_data, replace_placeholder5)
    dg.gen_data_to_csv(6, save_loc_for_gen_data, replace_placeholder6)
    dg.gen_data_to_csv(7, save_loc_for_gen_data, replace_placeholder7)
    dg.gen_data_to_csv(8, save_loc_for_gen_data, replace_placeholder8)
    dg.gen_data_to_csv(9, save_loc_for_gen_data, replace_placeholder9)
