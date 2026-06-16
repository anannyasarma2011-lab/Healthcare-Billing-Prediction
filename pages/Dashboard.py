import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="Healthcare Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

df = pd.read_excel("healthcare_ml_step6_completed.xlsx")

# ---------------------------------------------------
# Sidebar Filters
# ---------------------------------------------------

st.sidebar.header("Filters")

condition = st.sidebar.selectbox(
    "Medical Condition",
    ["All"] + sorted(
        df["medical_condition"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )
)

service = st.sidebar.selectbox(
    "Service Type",
    ["All"] + sorted(
        df["service_type"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )
)

gender = st.sidebar.selectbox(
    "Gender",
    ["All"] + sorted(
        df["gender"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )
)

# ---------------------------------------------------
# Apply Filters
# ---------------------------------------------------

filtered_df = df.copy()

if condition != "All":
    filtered_df = filtered_df[
        filtered_df["medical_condition"] == condition
    ]

if service != "All":
    filtered_df = filtered_df[
        filtered_df["service_type"] == service
    ]

if gender != "All":
    filtered_df = filtered_df[
        filtered_df["gender"] == gender
    ]

# ---------------------------------------------------
# Dashboard Title
# ---------------------------------------------------

st.title("📊 Healthcare Analytics Dashboard")

st.write(
    "Overview of healthcare billing and patient statistics"
)

# ---------------------------------------------------
# KPI Cards
# ---------------------------------------------------

# KPI Cards

st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
with col1:

    st.metric(
        label="👥 Total Patients",
        value=f"{filtered_df.shape[0]:,}"
    )

with col2:
    st.metric(
        label="💰 Average Billing",
        value=f"₹ {filtered_df['billed_amount_inr'].mean():,.0f}"
    )

with col3:
    st.metric(
        label="🛏 Average LOS",
        value=f"{filtered_df['length_of_stay_days'].mean():.2f} Days"
    )

with col4:
    st.metric(
        label="🏥 Total Revenue",
        value=f"₹ {filtered_df['billed_amount_inr'].sum():,.0f}"
    )

st.markdown("---")
st.caption(
    f"Showing data for "
    f"{condition} | {service} | {gender}"
)

# ---------------------------------------------------
# Billing Distribution
# ---------------------------------------------------

st.markdown("---")

st.subheader("Billing Amount Distribution")

fig = px.histogram(
    filtered_df,
    x='billed_amount_inr',
    nbins=30,
    title="Distribution of Billing Amount"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# Top Medical Conditions
# ---------------------------------------------------

st.markdown("---")

st.subheader("Top Medical Conditions")

condition_counts = (
    filtered_df['medical_condition']
    .value_counts()
    .reset_index()
)

condition_counts.columns = [
    'Medical Condition',
    'Count'
]

fig = px.bar(
    condition_counts,
    x='Medical Condition',
    y='Count',
    title='Most Common Medical Conditions'
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# Most Used Services
# ---------------------------------------------------

st.markdown("---")

st.subheader("Most Used Services")

service_counts = (
    filtered_df['service_type']
    .value_counts()
    .reset_index()
)

service_counts.columns = [
    'Service Type',
    'Count'
]

fig = px.bar(
    service_counts,
    x='Service Type',
    y='Count',
    title='Most Frequently Used Services'
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# LOS Distribution
# ---------------------------------------------------

st.markdown("---")

st.subheader("Length of Stay Distribution")

fig = px.histogram(
    filtered_df,
    x='length_of_stay_days',
    nbins=15,
    title='Distribution of Hospital Stay Duration'
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# Billing vs LOS
# ---------------------------------------------------

st.markdown("---")

st.subheader("Billing Amount vs Length of Stay")

fig = px.scatter(
    filtered_df,
    x='length_of_stay_days',
    y='billed_amount_inr',
    title='Relationship between LOS and Billing Amount'
)

st.plotly_chart(fig, use_container_width=True)
st.markdown("---")

st.subheader("Gender Distribution")

gender_counts = (
    filtered_df["gender"]
    .value_counts()
    .reset_index()
)

gender_counts.columns = ["Gender", "Count"]

fig = px.pie(
    gender_counts,
    names="Gender",
    values="Count",
    title="Patient Distribution by Gender",
    hole=0.4      # Makes it a donut chart (looks nicer)
)

fig.update_traces(
    textposition="inside",
    textinfo="percent+label"
)

st.plotly_chart(fig, use_container_width=True)
st.markdown("---")

st.subheader("Age Group Distribution")

# Create age groups
filtered_df["Age Group"] = pd.cut(
    filtered_df["age"],
    bins=[0, 20, 40, 60, 100],
    labels=["0-20", "21-40", "41-60", "60+"]
)

age_counts = (
    filtered_df["Age Group"]
    .value_counts()
    .reset_index()
)

age_counts.columns = ["Age Group", "Count"]

fig = px.bar(
    age_counts,
    x="Age Group",
    y="Count",
    color="Age Group",
    title="Patient Distribution by Age Group"
)

fig.update_layout(
    title_x=0.3,
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)
