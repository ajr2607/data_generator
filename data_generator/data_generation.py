import numpy as np
import pandas as pd


# def generate_placeholder_data(row_event, number_of_rows_to_generate, new_rows_percs):
#     row_event_initial = list(range(0, len(row_event)))  # won't let me put a list as the row_event so using
#     # row_event_initial as a placeholder and replacing with the list later
#     # generating integers to be used as index for 2d list to replace integers with lists
#     return list(np.random.choice(row_event_initial, size=number_of_rows_to_generate, p=new_rows_percs))


def generate_placeholder_data_for_multiple_sets(how_many_datasets, row_event, number_of_rows_to_generate,
                                                new_rows_percs):
    dataframes_for_multiple_sets = []
    row_event_initial = list(range(0, len(row_event)))
    for number in range(how_many_datasets):
        placeholder_data = list(np.random.choice(row_event_initial, size=number_of_rows_to_generate, p=new_rows_percs))
        dataframes_for_multiple_sets.append(placeholder_data)
    return dataframes_for_multiple_sets


def replace_placeholder_num_with_event(which_df_changing, number_of_rows_to_generate, placeholder_data, row_event,
                                       df_column_names):
    generated_list_of_rows = []
    for num in range(number_of_rows_to_generate):
        generated_list_of_rows.append(list(row_event[int(placeholder_data[which_df_changing][num])]))
    return pd.DataFrame(generated_list_of_rows, columns=df_column_names)


def gen_data_to_csv(which_df_changing, save_loc_for_gen_data, df_to_change):
    file_name = 'gen_data_' + str(which_df_changing) + '.csv'
    with open(save_loc_for_gen_data.joinpath(file_name), 'w') as f:
        f.write(str(df_to_change.to_csv()))
        f.close()
    return
