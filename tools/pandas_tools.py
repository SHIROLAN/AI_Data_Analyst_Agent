import pandas as pd

def get_basic_statistics(df):
    stats:{
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing values": df.isnull().sum().to_dict(),
        "numeric_summary": df.describe().to_dict()
    }