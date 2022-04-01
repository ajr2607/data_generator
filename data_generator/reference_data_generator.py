from pathlib import Path

import pandas as pd

dir_to_scan = "./sample_data.csv"
p = Path(dir_to_scan)

# read in sample data - generate from faker/mimesis?
sample_data = pd.read_csv(p)
column_names_to_generate_data_for = ["name", "job", "company", "residence", "sex", "mail", "birthdate"]
# potential for user input here
sample_data = sample_data[column_names_to_generate_data_for]

# analysis
number_of_men = len(sample_data[sample_data.sex.isin(['M'])])
number_of_women = len(sample_data[sample_data.sex.isin(['F'])])
print(number_of_men)
print(number_of_women)


# stratify data


# generate more data
