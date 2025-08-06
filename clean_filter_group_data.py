"""
Uses functions from functions.py to clean, filter, and group data from combineddata.csv, and outputs clean_grouped_combineddata.csv, storing it in the data directory. The new file can be used to create Tableau dashboards.
"""

import functions
import pandas as pd

def main():
    df = pd.read_csv("data/combineddata.csv")
    df = functions.filter(df)
    df = functions.clean(df)
    df = functions.group_west_east(df)
    df = functions.group_dates_seasons(df)
    df = functions.group_puctuality(df)
    df.to_csv("data/clean_grouped_combineddata.csv")

main()