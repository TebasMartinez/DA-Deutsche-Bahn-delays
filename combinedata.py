"""
Takes a list of datasets in .parquet format and combines them into a single .csv, storing it in the data directory

Usage: python combinedata.py <input_file> <output_file>
<input_file> must be a .txt file containing a list of paths to the datasets.
<output_file> must be formated as .csv
"""

import pandas as pd
import sys


def main(txtdatalist, csvoutput):
    df = combine(txtdatalist)
    df.to_csv(f"data/{csvoutput}", index=False)

def combine(txtdatalist):
    with open(txtdatalist, "r") as f:
        datalist = [datapath.strip() for datapath in f]
    df = pd.read_parquet(datalist[0])
    for dataset in datalist[1:]:
        df2 = pd.read_parquet(dataset)
        df = pd.concat([df, df2], axis=0)
    return df
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python combinedata.py <input_file> <output_file>")
    else:
        main(sys.argv[1], sys.argv[2])
            
        

