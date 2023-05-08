import pandas as pd
import streamlit as st

def list_of_df(*args):

    list_of_df = []
    
    for i in args:
        df = pd.read_csv(i)
        list_of_df.append(df)

    result = pd.concat(list_of_df)

    return result

def combiner(*args, dest_path):

    result = list_of_df(*args) 
    result = result.fillna(0)
    df = result.drop_duplicates()
    df.to_csv(f"{dest_path}", index=False)

if __name__ == "__main__":
    combiner("data/shallaberlin_electronic_1.csv",
            "data/shallaberlin_electronic_2.csv",
             dest_path="results/res1.csv")