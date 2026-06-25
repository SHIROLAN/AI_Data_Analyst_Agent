import os
import pandas as pd

def get_schema(df):
    """Get the schema of a DataFrame as a dictionary."""

    schema = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "data_types": {
            col: str(dtype)
            for col, dtype in df.dtypes.items()
        }
    }

    return schema

