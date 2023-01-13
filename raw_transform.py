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

raw = pd.read_excel(path)

# Get date list

dates = np.unique(raw["%Calendar Date"])

print(len(dates))

# get unique states

ostates = np.unique(raw["Origin State"])
dstates = np.unique(raw["Destination State"])

rawstates = np.concatenate((ostates,dstates))

states = np.unique(rawstates)
print(len(states))

# if date and origin/destination keep numbers

agg_date = {}

# Creating a dictionary with the keys being the date and state and the values being a list of 3 zeros.
for i in range(0,len(dates)):
    for j in range(0,len(states)):
        if dates[i]+states[j] not in agg_date:
            agg_date[dates[i]+states[j]] = [0,0,0]

compare = agg_date

for i in range(0,len(raw)):
    concat = raw[i]["%Calendar Date"]+raw[i]["Origin State"]
    concat2 = raw[i]["%Calendar Date"]+raw[i]["Destination State"]
    if concat in agg_date:
        agg_date[concat] += [raw[i]["Avg(Shipper_Rate)"],raw[i]["AVG Cost"],raw[i]["Load Count"],raw[i]["DAT_EST_RATE"]]
    else:
        agg_date[concat] += [raw[i]["Avg(Shipper_Rate)"],raw[i]["AVG Cost"],raw[i]["Load Count"],raw[i]["DAT_EST_RATE"]]
    if concat2 in agg_date:
        agg_date[concat] += [raw[i]["Avg(Shipper_Rate)"],raw[i]["AVG Cost"],raw[i]["Load Count"],raw[i]["DAT_EST_RATE"]]
    else:
        agg_date[concat2] += [raw[i]["Avg(Shipper_Rate)"],raw[i]["AVG Cost"],raw[i]["Load Count"],raw[i]["DAT_EST_RATE"]]

df = pd.DataFrame(agg_date)

df.to_excel('raw_result.xlsx')