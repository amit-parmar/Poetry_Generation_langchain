import streamlit as st
from palm2_model import generate_shayaris

st.title("Want you be a Poet!")

shayar = st.sidebar.selectbox("Choose your favorite Shayar", ("faiz ahmed faiz", "Javed Akhtar", "Gulzar", "Mazruh Sultanpuri", "Shahir Ludhiyanvi"))

if shayar:
    shayari = generate_shayaris(shayar)
    
    st.header('Generated Shayari')

    st.write(shayari)