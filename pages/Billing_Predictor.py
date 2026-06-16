import streamlit as st
st.set_page_config(
    page_title="Billing Predictor",
    page_icon="🔮",
    layout="wide"
)
import pandas as pd
import numpy as np
import joblib

# Set page config
st.set_page_config(
    page_title="Healthcare Billing Predictor",
    page_icon="🏥",
    layout="wide"
)

# Load model
@st.cache_resource
def load_model():
    return joblib.load('simple_healthcare_model.pkl')

model = load_model()

# App title and description
st.title("🏥 Healthcare Billing Amount Prediction")
st.markdown("""
This application predicts the estimated billing amount for hospital services based on patient details.
Enter the patient information below and click **Predict Billing Amount** to get the estimated cost.
""")

# Create two columns for better layout
col1, col2 = st.columns(2)

# Left column
with col1:
    st.subheader("Patient Information")
    
    age = st.number_input(
        "Age (years)",
        min_value=0,
        max_value=120,
        value=30,
        step=1
    )
    
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )
    
    length_of_stay = st.number_input(
        "Length of Stay (Days)",
        min_value=0,
        max_value=365,
        value=1,
        step=1
    )

# Right column
with col2:
    st.subheader("Medical Details")
    
    medical_condition = st.selectbox(
        "Medical Condition",
        [
            "Asthma",
            "Cancer",
            "Diabetes",
            "Heart Disease",
            "Hypertension"
        ]
    )
    
    service_type = st.selectbox(
        "Service Type",
        [
            "Consultation",
            "Emergency",
            "ICU",
            "Radiology",
            "Surgery"
        ]
    )

# Prediction button
st.markdown("---")
if st.button("🔮 Predict Billing Amount", use_container_width=True):
    # Prepare input data
    input_data = pd.DataFrame({
        'age': [age],
        'length_of_stay_days': [length_of_stay],
        'gender_Male': [1 if gender == "Male" else 0],
        'medical_condition_Asthma': [1 if medical_condition == "Asthma" else 0],
        'medical_condition_Cancer': [1 if medical_condition == "Cancer" else 0],
        'medical_condition_Diabetes': [1 if medical_condition == "Diabetes" else 0],
        'medical_condition_Heart Disease': [1 if medical_condition == "Heart Disease" else 0],
        'medical_condition_Hypertension': [1 if medical_condition == "Hypertension" else 0],
        'service_type_Consultation': [1 if service_type == "Consultation" else 0],
        'service_type_Emergency': [1 if service_type == "Emergency" else 0],
        'service_type_ICU': [1 if service_type == "ICU" else 0],
        'service_type_Radiology': [1 if service_type == "Radiology" else 0],
        'service_type_Surgery': [1 if service_type == "Surgery" else 0],
    })
    
    # Ensure all expected columns exist
    expected_columns = model.feature_names_in_
    for col in expected_columns:
        if col not in input_data.columns:
            input_data[col] = 0
    
    # Reorder columns to match training data
    input_data = input_data[expected_columns]
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display result
    st.markdown("---")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric(
            "Predicted Billing Amount",
            f"₹{prediction:,.2f}",
            delta=None
        )
    
    with col2:
        st.success(
            f"**Estimated Total Cost: ₹{prediction:,.2f}**\n\n"
            f"This is an estimate based on:\n"
            f"- Age: {age} years\n"
            f"- Condition: {medical_condition}\n"
            f"- Service: {service_type}\n"
            f"- Length of Stay: {length_of_stay} days"
        )

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
    <p>This tool provides estimates based on historical data. Actual billing may vary.</p>
    <p>Built with Streamlit | Healthcare Prediction Model</p>
    </div>
    """,
    unsafe_allow_html=True
)
