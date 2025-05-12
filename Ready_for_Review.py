import streamlit as st
import pandas as pd

st.title("📋 Applications Ready for Review")

df = pd.read_excel("data/cleaning_data.xlsx")

# Filter where request is approved
ready_df = df[df['request_status'].str.lower() == 'approved']

# Checkbox: filter signed apps
if 'application_signed' in ready_df.columns:
    signed_only = st.checkbox("Only show signed applications", value=False)
    if signed_only:
        ready_df = ready_df[ready_df['application_signed'] == True]

st.dataframe(ready_df)
st.markdown(f"✅ Total Applications: {len(ready_df)}")
