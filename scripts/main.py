import pandas as pd
import os
import json
from json import dumps


def load_data(filter1, filter2):
    output = {}
    # Import the world internet data from world bank and rename columns for merging with location data
    data_path = os.path.join(os.path.dirname(
        __file__), '..', 'data', 'world_bank_internet_data.csv')
    world_data = pd.read_csv(data_path, skipfooter=446, engine="python")
    world_data = world_data.replace("..", 0)
    # Rename the Country and Country Codes column to allow merging later on
    world_data.rename(
        columns={'Country Name': 'Country', 'Country Code': 'Codes'}, inplace=True)
    # Remove the brackets and it the duplicated value in the Year columns
    world_data = world_data.rename(
        columns={col: col.split('[')[0] for col in world_data.columns})
    world_data.columns = world_data.columns.str.strip()
    cols = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    world_data.drop(world_data.columns[cols], axis=1, inplace=True)

    # Import the coordinate csv file, rename columns for merging with each other later on
    data_path = os.path.join(os.path.dirname(
        __file__), '..', 'data', "world_country.csv")
    coordinates = pd.read_csv(data_path)
    # Rename the Country Codes column to allow merging later on and long/lat for clarity
    coordinates.rename(
        columns={'iso_con': 'Codes', 'lat': 'Latitude', 'lon': 'Longitude'}, inplace=True)
    # Drop unnecessary columns
    coordinates.drop(columns=['Unnamed: 0', 'country'], inplace=True)
    # Merge the world_data with the coordinates
    final_world = pd.merge(world_data, coordinates, on="Codes", how="left")

    # Turn the Year columns into Rows
    data = pd.melt(final_world, id_vars=[
                   'Country', 'Codes', 'Series Name', 'Longitude', 'Latitude'], var_name='Year', value_name='Values')
    data.rename(columns={'Series Name': 'SeriesName'},inplace=True)
    data['Year']=data['Year'].astype(int)
    data['Values']=data['Values'].astype(float)


    # Reading the ITU excel file age and gender sheet to clean and turn into json object
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data',
                             'ITU_regional_global_Key_ICT_indicator_aggregates_rev1_Jan_2022.xlsx')
    gender_df = pd.read_excel(data_path, skiprows=(0,1), sheet_name="Internet use by sex & age")
    # Get the gender tables
    gender_df=gender_df.iloc[0:16,0:18] 
    #Drop unnecessary columns
    cols = [1,2,3,4,5,6,7,8]
    gender_df.drop(gender_df.columns[cols],axis=1,inplace=True)
    # # Drop unnecessary rows
    gender_df = gender_df.drop(0)
    gender_df = gender_df.drop(1)
    gender_df = gender_df.drop(3)
    gender_df = gender_df.drop(4)
    gender_df = gender_df.drop(5)
    gender_df = gender_df.drop(6)
    gender_df = gender_df.drop(7)
    gender_df = gender_df.drop(8)
    gender_df = gender_df.drop(9)
    gender_df.columns=['Percentage of individuals using the Internet, by sex', '% Total 2020','% Female 2020','% Male 2020']
    gender_df.reset_index(inplace=True, drop=True)  

    data_path = os.path.join(os.path.dirname(__file__), '..', 'data',
                             'ITU_regional_global_Key_ICT_indicator_aggregates_rev1_Jan_2022.xlsx')
    age_df = pd.read_excel(data_path, skiprows=range(0,19),skipfooter=10 , sheet_name="Internet use by sex & age")
    age_table_name=age_df.iloc[0,0]
    # Get the age tables from the gender_age excel file
    age_df=age_df.iloc[3:17,0:8]
    age_df = age_df.drop(4)
    age_df = age_df.drop(5)
    age_df = age_df.drop(6)
    age_df = age_df.drop(7)
    age_df = age_df.drop(8)
    age_df = age_df.drop(9)
    age_df = age_df.drop(10)
    cols= [1,2,3,4]
    age_df.drop(age_df.columns[cols],axis=1,inplace=True)
    age_df.columns=[age_table_name,'% Total 2020','% Youth(15-24) 2020','% Rest of Population 2020']
    age_df.reset_index(inplace=True, drop=True)    


    # Reading the ITU excel file region sheet to clean and turn into json object
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data',
                             'ITU_regional_global_Key_ICT_indicator_aggregates_rev1_Jan_2022.xlsx')
    temp_df = pd.read_excel(data_path, header=None, sheet_name="By BDT region")
    # Getting the first table
    temp_df.iloc[3:10, 0:18]
    # Getting the first column names
    table_name = temp_df.iloc[2, 0]

    # dictionary of tables with key as table name and value as dataframe
    table_list = {}
    # year list
    year_list = list(range(2005, 2022))
    # range start at 4(3), all the way to row 92 with a step of 9
    for i in range(4, 92, 9):
        # table name, 2 rows from where the table start at 0 (1st) column
        table_name = temp_df.iloc[i-2, 0]
        # selecting range of rows and range of columns to extract a table into a dataframe
        region_df = temp_df.iloc[i:i+6, 0:18]
        region_df.reset_index(drop=True, inplace=True)
        # column names (year)
        column_names = [table_name] + year_list
        # using the year list and table names as column names
        region_df.columns = column_names
        table_list[table_name] = region_df


# Empty dict to store the data cleaned in main.py for use in index.html and app.js
    output = {}
    # filter for world countries bar chart and world map
    output['filter1list'] = list(world_data['Series Name'].unique())
    output['filter1'] = filter1
    output['filter2list'] = list(world_data['Country'].unique())
    output['filter2'] = filter2
    world_data = world_data.loc[world_data['Series Name'] == filter1]
    world_data = world_data.loc[world_data['Country'] == filter2]
    # x, y variables for the countries bar chart
    output['x'] = list(world_data.columns.values)[4:]
    output['y'] = world_data.values.tolist()[0]
    # Variables for the Gender and Age charts 
    output['genderData']= gender_df.to_json(orient='index', indent=4)
    output['ageData']= age_df.to_json(orient='index', indent=4)


 # World regions internet usage excel sheet
    tracedata = {}
    table_list_keys = list(table_list.keys())
    for i in range(len(table_list_keys)):
        tempdf = table_list[table_list_keys[i]]
        regions = tempdf[table_list_keys[i]].tolist()
        tempregions = {}
        for j in range(len(regions)):
            tempregions[regions[j]] = tempdf.values.tolist()[j][1:]
        tracedata[table_list_keys[i]] = tempregions
    output['tracedata'] = tracedata
    output['dataWorld']=data.to_json(orient='index', indent=4)



    return output
# print (region_df)
# def main():
