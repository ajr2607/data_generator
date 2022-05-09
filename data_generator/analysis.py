import pandas as pd


def get_row_event(input_data):  # how many of each unique row
    c_row_df = pd.DataFrame(input_data.value_counts())
    row_events = c_row_df.index.tolist()
    for item in range(len(row_events)):
        row_events[item] = list(row_events[item])
    return row_events


def row_event_perc_finder(c_row_list, input_data):  # percentage share of total sample for each unique row
    row_event_percs_list = []
    for i in range(len(c_row_list)):
        percs_row = c_row_list[i] / len(input_data)
        row_event_percs_list.append(percs_row)
    return row_event_percs_list
