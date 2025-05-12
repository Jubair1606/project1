import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Yearly Impact Summary")

df = pd.read_excel("data/cleaning_data.xlsx")
df['year'] = pd.to_datetime(df['grant_req_date']).dt.year

summary = df.groupby('year').agg(
    total_granted=('amount', 'sum'),
    unique_patients=('patient_id', 'nunique')
).reset_index()

fig = px.bar(summary, x='year', y='total_granted', title="Total Support by Year")
st.plotly_chart(fig, use_container_width=True)
st.dataframe(summary)
