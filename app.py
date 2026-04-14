import streamlit as st
import pandas as pd
import pickle

# 1. Load the saved model from your folder
with open('water_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("💧 Water Quality Analyzer")
st.write("Enter the water metrics below:")

# 2. Create the user inputs
ph = st.number_input('pH Level', value=7.0)
hardness = st.number_input('Hardness', value=150.0)
solids = st.number_input('Total Dissolved Solids', value=20000.0)
chloramines = st.number_input('Chloramines', value=7.0)
sulfate = st.number_input('Sulfate', value=300.0)
conductivity = st.number_input('Conductivity', value=400.0)
organic_carbon = st.number_input('Organic Carbon', value=15.0)
trihalomethanes = st.number_input('Trihalomethanes', value=60.0)
turbidity = st.number_input('Turbidity', value=4.0)

# 3. Create the prediction button
if st.button("Check Water Safety"):
    
    # Bundle the user inputs into a format the model understands
    input_data = pd.DataFrame([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]], 
                              columns=['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity'])
    
    # Make the prediction using the loaded model
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.success("✅ SAFE: This water is potable.")
    else:
        st.error("🚨 UNSAFE: This water is NOT potable.")