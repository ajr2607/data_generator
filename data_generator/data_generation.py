import numpy as np
import pandas as pd

import variable_file


def generate_placeholder_data(row_event, number_of_rows_to_generate, new_rows_percs):
    row_event_initial = list(range(0, len(row_event)))  # won't let me put a list as the row_event so using
    # row_event_initial as a placeholder and replacing with the list later
    # generating integers to be used as index for 2d list to replace integers with lists
    return list(np.random.choice(row_event_initial, size=number_of_rows_to_generate, p=new_rows_percs))


def replace_placeholder_num_with_event(placeholder_data, row_event, df_column_names):
    gen_list_final = []
    for i in range(len(placeholder_data)):
        gen_list_final.append(row_event[placeholder_data[i]])
        # using generated integers as the index, append list from 2d list to gen_list_final_maybe
    return pd.DataFrame(gen_list_final, columns=df_column_names)


def gen_data_to_csv(how_many_datasets, placeholder_data, row_events, save_loc_for_gen_data):
    # path_name = Path('generated_files')
    for number in range(how_many_datasets):
        file_name = 'gen_data_' + str(number) + '.csv'
        df = replace_placeholder_num_with_event(placeholder_data, row_events, variable_file.df_column_names)
        with open(save_loc_for_gen_data.joinpath(file_name), 'w') as f:
            f.write(str(df.to_csv()))
            f.close()
    return
