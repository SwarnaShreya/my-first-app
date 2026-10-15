import streamlit as st

st.title("My First App 👋")

name = st.text_input("What is your name?")

if st.button("Say hello"):
    st.write(f"Hello, {name}! Welcome to my app 😊")