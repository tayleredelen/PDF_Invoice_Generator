import pandas as pd
# reads csv and excel data
import glob

filepaths = glob.glob("Invoices/*xlsx")
# this creates a path to all files in Invoices that are .xlsx

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
