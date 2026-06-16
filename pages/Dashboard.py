import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Healthcare Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load dataset
df = pd.read_excel("healthcare_ml_step6_completed.xlsx")

st.title("📊 Healthcare Analytics Dashboard")

st.write("Overview of healthcare billing and patient statistics")

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Patients",
        df.shape[0]
    )

with col2:
    st.metric(
        "Average Billing",
        f"₹ {df['billed_amount_inr'].mean():,.0f}"
    )

with col3:
    st.metric(
        "Average LOS",
        round(df['length_of_stay_days'].mean(), 2)
    )

with col4:
    st.metric(
        "Total Revenue",
        f"₹ {df['billed_amount_inr'].sum():,.0f}"
    )
import plotly.express as px

st.markdown("---")

st.subheader("Billing Amount Distribution")

fig = px.histogram(
    df,
    x='billed_amount_inr',
    nbins=30,
    title="Distribution of Billing Amount"
)

st.plotly_chart(fig, use_container_width=True)
st.markdown("---")

st.subheader("Top Medical Conditions")

condition_counts = (
    df['medical_condition']
    .value_counts()
    .reset_index()
)

condition_counts.columns = ['Medical Condition', 'Count']

fig = px.bar(
    condition_counts,
    x='Medical Condition',
    y='Count',
    title='Most Common Medical Conditions'
)

st.plotly_chart(fig, use_container_width=True)
st.markdown("---")

st.subheader("Most Used Services")

service_counts = (
    df['service_type']
    .value_counts()
    .reset_index()
)

service_counts.columns = ['Service Type', 'Count']

fig = px.bar(
    service_counts,
    x='Service Type',
    y='Count',
    title='Most Frequently Used Services'
)

st.plotly_chart(fig, use_container_width=True)
st.markdown("---")

st.subheader("Length of Stay Distribution")

fig = px.histogram(
    df,
    x='length_of_stay_days',
    nbins=15,
    title='Distribution of Hospital Stay Duration'
)

st.plotly_chart(fig, use_container_width=True)
st.markdown("---")

st.subheader("Billing Amount vs Length of Stay")

fig = px.scatter(
    df,
    x='length_of_stay_days',
    y='billed_amount_inr',
    title='Relationship between LOS and Billing Amount'
)

st.plotly_chart(fig, use_container_width=True)
