import json
import pandas as pd
import numpy as np

json_path = "dataset/secc_data.json"
csv_path = "dataset/poll_station_metadata_all.csv"

# Creating a dictonary from json file
with open(json_path) as f:
    SECC_dictionary = json.load(f)

# Import CSV to a DataFrame and Selecting required Columns
df = pd.read_csv(path, error_bad_lines=False, warn_bad_lines=False, low_memory=False)
sel_cols = ['state_or_ut', 'district', 'ac', 'polling_station', 'lat', 'long']
df = df[sel_cols]
columns = ['State/UT', 'District', 'AC', 'Polling_Station', 'Lat', 'Long']
df.columns = columns

# Collects all the states, districts and block of the dictonary
state_list = []
all_district_list = []
all_block_list = []

for state in SECC_dictionary:
    state_list.append(state)
    for district in SECC_dictionary[state]:
        all_district_list.append(district)
        for block in SECC_dictionary[state][district]:
            all_block_list.append(block)


def Select_State_District(state, district):
    """
    This function converts the selected State and District into a DataFrames.

    The Function Cosists of two blocks:
    1. To group State and District of Polling Stations
    2. To Create a DataFrame from the SECC_dictionary

    Parameters:
    state (str): State to be selected
    district (str) : District to be selected

    Returns:
    DataFrame_1 : Reurns a df_state_dist DataFrame
    DataFrame_2 : Reurns a df_state_dist state_dist_block_df
    """

    # Grouping State and District wise
    df_groupby_state_district = df.groupby(['State/UT', 'District'])
    df_state_dist = df_groupby_state_district.get_group((state, district))
    df_state_dist.reset_index(inplace=True, drop=True)

    # Creating a State_District_Block from the SECC_dictionary
    if state.upper() in state_list:
        state_dict = dict(SECC_dictionary[state.upper()])
        if district.upper() in state_dict.keys():
            state_dist_block = dict(SECC_dictionary[state.upper()][district.upper()])

    # Creating a Dataframe from SECC_dictionary
    state_dist_block_df = pd.DataFrame.from_dict(state_dist_block, orient='index')
    state_dist_block_df = state_dist_block_df.transpose()
    state_dist_block_df.replace(to_replace=[None], value=np.nan, inplace=True)

    return df_state_dist, state_dist_block_df


# Function call
df_1, df_2 = Select_State_District('Telangana', 'Medchal Malkajgiri')

print(df_1.head())
print(df_2.head())

## Writing data to a file

f_string = ""
with open("testFile.csv", "w") as f:
    f.write("PS_Address, Block_Name, Block_Area\n")

for df_4_row in range(len(df_4)):
    y = df_4.iloc[df_4_row][3]
    for df_5_cols in df_5:
        for df_5_rows in df_5[df_5_cols]:
            if str(df_5_rows) != 'nan':
                if str(df_5_rows) in y:
                    f_string = str(y) + ","+str(df_5_cols)+"," + str(df_5_rows)+"\n"
                    with open("testFile.csv", "a") as f:
                        f.write(f_string)
                        sleep(.250)

## Writing data to a dataframe                        
for df_4_row in range(len(df_4)):
    y = df_4.iloc[df_4_row][3]
    for df_5_cols in df_5:
        for df_5_rows in df_5[df_5_cols]:
            if str(df_5_rows) != 'nan':
                if str(df_5_rows) in y:
                    df_7[df_4_row] = df_5[df_5_rows]
                else:
                    df_7[df_4_row] = np.nan

## Adding the DataFrame as a new Coloumn
df_6.insert(6, "Block_Area", df_7)

###### Still Need to update the code, Working on Issues

