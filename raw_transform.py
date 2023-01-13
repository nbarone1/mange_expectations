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

for i in range(0,len(dates)):
    