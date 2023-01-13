# Turn Raw into usable

# Importing the pandas library and renaming it to pd.
import pandas as pd
import numpy as np

# Select Data File
import tkinter as tk
from tkinter import filedialog

# Importing the data file.
root = tk.Tk()

path = filedialog.askopenfilename()
root.destroy()

raw = pd.read_excel(path)

# Creating a dictionary with the key being the concatenation of the date and state and the value being
# a list of the aggregated values.
agg_date = {}

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
        agg_date[concat][4] += 1
    else:
        agg_date[concat] = [raw.iloc[i].loc["Avg(Shipper_Rate)"],raw.iloc[i].loc["AVG COST"],raw.iloc[i].loc["Load Count"],raw.iloc[i].loc["DAT_EST_RATE"],1]
    if concat2 in agg_date:
        agg_date[concat2][0] += raw.iloc[i].loc["Avg(Shipper_Rate)"]
        agg_date[concat2][1] += raw.iloc[i].loc["AVG COST"]
        agg_date[concat2][2] += raw.iloc[i].loc["Load Count"]
        agg_date[concat2][3] += raw.iloc[i].loc["DAT_EST_RATE"]
        agg_date[concat2][4] += 1
    else:
        agg_date[concat2] = [raw.iloc[i].loc["Avg(Shipper_Rate)"],raw.iloc[i].loc["AVG COST"],raw.iloc[i].loc["Load Count"],raw.iloc[i].loc["DAT_EST_RATE"],1]

# Creating a dataframe from the dictionary.
df = pd.DataFrame.from_dict(agg_date,orient='index')
df.columns = ['SHIPPER','COST','LC','DAT','DATES HIT']
df.index.name = 'Date State'

# Saving the file to the path that the user selects.
try: 
    with filedialog.asksaveasfile(defaultextension=".xlsx") as file: df.to_excel(file.name)
except AttributeError:
    print("Cancelled Save")