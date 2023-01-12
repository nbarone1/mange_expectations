# Turn Raw into usable

# Importing the pandas library and renaming it to pd.
import pandas as pd

# Select Data File
import tkinter as tk
from tkinter import filedialog

# Importing the data file.
root = tk.Tk()

path = filedialog.askopenfilename()

raw = pd.read_excel(path)

# Get date list

raw_dates = raw["%Calendar Date"]

dates = []

for i in range(0,len(raw_dates)):
    if raw_dates[i] not in dates:
        dates.append(raw_dates[i])

print(len(dates))
print(dates)