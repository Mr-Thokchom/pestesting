import streamlit as st
import pickle
import numpy as np

st.title("Check the environment")

#Input data
carbon_emission=st.number_input("Carbon emission Amount: ",min_value=0.0,format="%f")
energy_output=st.number_input("Energy Output Value: ",min_value=0.0,format="%f")
renewability_index=st.number_input("Renewability_index Amount: ",min_value=0.0,format="%f")
Cost_efficiency=st.number_input("Cost_efficiency Amount: ",min_value=0.0,format="%f")

#Model IMporting
with open('lrmodel_sustainable.pkl','rb') as file:
    model=pickle.load(file)
#predict
if st.button("Predict"):
    input_data=np.array([[carbon_emission,energy_output,renewability_index,Cost_efficiency]])

    prediction=model.predict(input_data)
    #Display the result
    if prediction[0]==1:
        st.success("Congrats, This environment is sustainable")
    else:
        st.info("It is not sustainable")