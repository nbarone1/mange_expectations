# Turn Raw into usable
# idea is to use this plus managerial input for new map

# Importing the pandas library and renaming it to pd.
import pandas as pd

# Select Data File
import tkinter as tk
from tkinter import filedialog

# Importing the data file.
def f_open():
    """
    It opens a file dialog, gets the path of the file you selected, and returns a pandas dataframe of
    the file you selected
    :return: A dataframe
    """
    root = tk.Tk()

    path = filedialog.askopenfilename()
    root.destroy()
    return pd.read_excel(path)

def data_transform(raw):
    """
    The function takes in a dataframe and returns a dataframe with the average shipper rate, average
    cost, load count, dat estimated rate, and 1 for each date and state
    
    :param raw: The raw dataframe that is being transformed
    :return: A dataframe with the following columns:
    SHIPPER, COST, LC, DAT, DATES HIT, Date, State
    """
    # Creating a dictionary with the key being the concatenation of the date and state and the value being
    # a list of the aggregated values.
    agg_date = {}
    dast = []

    # Creating a dictionary with the key being the concatenation of the date and the state. The value is a
    # list of the average shipper rate, average cost, load count, dat estimated rate, and 1.
    for i in range(0,len(raw)):
        concat = str(raw.iloc[i].loc["%Calendar Date"])[0:10]+raw.iloc[i].loc["Origin State"]
        concat2 = str(raw.iloc[i].loc["%Calendar Date"])[0:10]+raw.iloc[i].loc["Origin State"]
        if concat in agg_date:
            agg_date[concat][0] += raw.iloc[i].loc["Avg(Shipper_Rate)"]
            agg_date[concat][1] += raw.iloc[i].loc["AVG COST"]
            agg_date[concat][2] += raw.iloc[i].loc["Load Count"]
            agg_date[concat][3] += raw.iloc[i].loc["DAT_EST_RATE"]
            agg_date[concat][4] += raw.iloc[i].loc["Carrier Count"]
            agg_date[concat][5] += raw.iloc[i].loc["Shipper Count"]
            agg_date[concat][6] += 1
        else:
            dast.append(concat)
            agg_date[concat] = [raw.iloc[i].loc["Avg(Shipper_Rate)"],raw.iloc[i].loc["AVG COST"],raw.iloc[i].loc["Load Count"],raw.iloc[i].loc["DAT_EST_RATE"],raw.iloc[i].loc["Carrier Count"],raw.iloc[i].loc["Shipper Count"],1]
        if concat2 in agg_date:
            agg_date[concat2][0] += raw.iloc[i].loc["Avg(Shipper_Rate)"]
            agg_date[concat2][1] += raw.iloc[i].loc["AVG COST"]
            agg_date[concat2][2] += raw.iloc[i].loc["Load Count"]
            agg_date[concat2][3] += raw.iloc[i].loc["DAT_EST_RATE"]
            agg_date[concat2][4] += raw.iloc[i].loc["Carrier Count"]
            agg_date[concat2][5] += raw.iloc[i].loc["Shipper Count"]
            agg_date[concat2][6] += 1
        else:
            dast.append(concat2)
            agg_date[concat2] = [raw.iloc[i].loc["Avg(Shipper_Rate)"],raw.iloc[i].loc["AVG COST"],raw.iloc[i].loc["Load Count"],raw.iloc[i].loc["DAT_EST_RATE"],raw.iloc[i].loc["Carrier Count"],raw.iloc[i].loc["Shipper Count"],1]

    # Creating a dataframe from the dictionary.
    df = pd.DataFrame.from_dict(agg_date,orient='index')
    df.columns = ['SHIPPER','COST','LC','DAT','Carriers','Shippers','DATES HIT']
    df['SHIPPER'] = df['SHIPPER']/df['LC']
    df['COST'] = df['COST']/df['LC']
    df['DAT'] = df['DAT']/df['LC']
    df.index.name = 'Date State'

    # Clean Date and State values up
    date = []
    state = []
    for i in range(0,len(dast)):
        date.append(dast[i][:-2])
        state.append(dast[i][10:12])
    df['Date'] = date
    df['State'] = state
    return df

def f_save(df):
    """
    It saves the dataframe to the path that the user selects
    
    :param df: The dataframe that you want to save
    """
# Saving the file to the path that the user selects.
    try: 
        with filedialog.asksaveasfile(defaultextension=".xlsx") as file: df.to_excel(file.name)
    except AttributeError:
        print("Cancelled Save")