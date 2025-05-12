import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hope Foundation Dashboard", layout="wide")
st.title("🏥 Hope Foundation Dashboard")

# Use cleaned data
df = pd.read_excel("data/cleaning_data.xlsx")

st.subheader("Cleaned Data Preview")
st.dataframe(df.head())
