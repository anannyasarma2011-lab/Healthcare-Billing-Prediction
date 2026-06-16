import streamlit as st

st.set_page_config(
    page_title="Healthcare Analytics Platform",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Healthcare Analytics Platform")

st.markdown("""
Welcome to the Healthcare Analytics Platform.

This application consists of:

- 📊 Healthcare Analytics Dashboard
- 🔮 Billing Amount Prediction Model

Use the sidebar to navigate.
""")

st.sidebar.success("Select a page above.")
