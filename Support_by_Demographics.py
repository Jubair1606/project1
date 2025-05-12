import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Support by Demographics")

df = pd.read_excel("data/cleaning_data.xlsx")

group_field = st.selectbox("Group by demographic:", [
    "gender", "insurance_type", "assistance_type", "marital_status", "race"
])

if group_field in df.columns:
    grouped = df.groupby(group_field)['amount'].sum().reset_index()
    fig = px.bar(grouped, x=group_field, y='amount', title=f"Support by {group_field.title()}")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("That column is not available.")
