import streamlit as st
import pandas as pd
import plotly.express as px
from scripts.db_connection import get_connection

st.set_page_config(
    page_title="Bank Customer Churn Analysis",
    layout="wide"
)

conn = get_connection()

query = "SELECT * FROM customers"

df = pd.read_sql(query, conn)

conn.close()

st.title("🏦 Bank Customer Churn Analysis Dashboard")



total_customers = len(df)
churn_rate = round(df["Exited"].mean() * 100, 2)
avg_age = round(df["Age"].mean(), 1)

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", total_customers)
col2.metric("Churn Rate", f"{churn_rate}%")
col3.metric("Average Age", avg_age)



st.subheader("Churn by Geography")

geo = (
    df.groupby("Geography")["Exited"]
    .mean()
    .reset_index()
)

fig = px.bar(
    geo,
    x="Geography",
    y="Exited",
    title="Churn Rate by Geography"
)

st.plotly_chart(fig, use_container_width=True)
st.subheader("Churn by Gender")

gender = (
    df.groupby("Gender")["Exited"]
      .mean()
      .reset_index()
)

fig_gender = px.bar(
    gender,
    x="Gender",
    y="Exited",
    title="Churn Rate by Gender"
)

st.plotly_chart(fig_gender, use_container_width=True)



st.subheader("Churn by Gender")

gender = (
    df.groupby("Gender")["Exited"]
    .mean()
    .reset_index()
)

fig2 = px.pie(
    gender,
    names="Gender",
    values="Exited",
    title="Gender Churn Distribution"
)

st.plotly_chart(fig2, use_container_width=True)



st.subheader("Active vs Inactive Members")

activity = (
    df.groupby("IsActiveMember")["Exited"]
    .mean()
    .reset_index()
)

fig3 = px.bar(
    activity,
    x="IsActiveMember",
    y="Exited",
    title="Churn by Activity Status"
)

st.plotly_chart(fig3, use_container_width=True)


st.subheader("Age Distribution")

fig4 = px.histogram(
    df,
    x="Age",
    color="Exited",
    nbins=30
)

st.plotly_chart(fig4, use_container_width=True)
st.subheader("Age vs Churn")

fig_age = px.box(
    df,
    x="Exited",
    y="Age",
    title="Age Distribution of Churned Customers"
)

st.plotly_chart(fig_age, use_container_width=True)
st.subheader("Credit Score Distribution")

fig_credit = px.histogram(
    df,
    x="CreditScore",
    color="Exited",
    nbins=30
)

st.plotly_chart(fig_credit, use_container_width=True)
st.header("Root Cause Analysis")

st.markdown("""
### Key Findings

- Germany has the highest churn rate.
- Inactive customers churn almost twice as much as active customers.
- Female customers churn more than male customers.
- Older customers show higher churn tendencies.

### Recommended Actions

1. Send reminders to inactive customers.
2. Assign relationship managers to high-value customers.
3. Create retention campaigns for customers over 40.
4. Offer loyalty benefits to long-term customers.
""")