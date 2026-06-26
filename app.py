import streamlit as st
import pandas as pd
from tools.schema_tools import get_schema
from tools.pandas_tools import get_basic_statistics



st.set_page_config(
    page_title="AI Data Analyst Agent",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Data Analyst Agent")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Rows:", df.shape[0])

    with col2:
        st.write("Columns:", df.shape[1])

    st.subheader("Column Names")
    st.write(list(df.columns))

    st.subheader("Data Types")

    dtype_df = pd.DataFrame({
    "Column": df.columns,
    "Type": df.dtypes.astype(str) })

    st.dataframe(dtype_df)

    schema = get_schema(df)
    stats = get_basic_statistics(df)

    st.subheader("Basic Statistics")
    st.json(stats)
    

    st.subheader("Schema Information")
    st.json(schema)

    