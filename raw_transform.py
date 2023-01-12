# Turn Raw into usable

import pandas as pd

# Select Data File
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

path = filedialog.askopenfilename()

raw = pd.read_excel(path)

