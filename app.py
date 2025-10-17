# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 09:48:29 2025

@author: user
"""

import numpy as np
import streamlit as st
import pickle

# Load the trained model
with open('cancer_risk_factor_prediction.sav', 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Cancer Risk Factor Prediction")
st.write("Fill the following information to get a prediction:")

# User Inputs
pat = st.number_input("Patient_ID", value=0.0)
can = st.number_input("Cancer_Type", value=0.0)
ag = st.number_input("Age", value=0.0)
gen = st.number_input("Gender", value=0.0)
smo = st.number_input("Smoking", value=0.0)
obe = st.number_input("Obesity", value=0.0)
fam = st.number_input("Family_History", value=0.0)
drm = st.number_input("Diet_Red_Meat", value=0.0)
phy = st.number_input("Physical_Activity", value=0.0)
air = st.number_input("Air_Pollution", value=0.0)
occ = st.number_input("Occupational_Hazards", value=0.0)
hpy = st.number_input("H_Pylori_Infection", value=0.0)
cal = st.number_input("Calcium_Intake", value=0.0)
ovar = st.number_input("Overall_Risk_Score", value=0.0)
bmi = st.number_input("BMI", value=0.0)
pal = st.number_input("Physical_Activity_Level", value=0.0)
brc = st.number_input("BRCA_Mutation", value=0.0)
dsp = st.number_input("Diet_Salted_Processed", value=0.0)
alu = st.number_input("Alcohol_Use", value=0.0)
nun = st.number_input("Life style", value=0.0)

# Prediction on button click
if st.button("Predict"):
    # Create input in correct order and shape
    Input = np.array([[alu, dsp, brc, pal, bmi, ovar, cal, hpy, occ, air,
                       phy, drm, fam, pat, can, ag, gen, smo, obe,nun]])
    
    # Predict
    prediction = model.predict(Input)
    
    # Show result
    st.success(f"Predicted Risk Score: {prediction[0]:.2f}")
